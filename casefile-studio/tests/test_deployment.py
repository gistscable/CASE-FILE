"""Deployment contract: the storage root is configurable and health stays cheap.

These pin the assumptions the Render blueprint relies on (persistent disk
mounted outside the checkout, root-owned disk, /healthz probe).
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
from PIL import Image

import renderer
import storage

STUDIO = Path(__file__).resolve().parent.parent


def test_data_root_defaults_to_repo_data(monkeypatch):
    monkeypatch.delenv("CASEFILE_DATA_DIR", raising=False)
    code = (
        "import storage; print(storage.DATA)"
    )
    out = subprocess.run(
        [sys.executable, "-c", code],
        cwd=STUDIO,
        capture_output=True,
        text=True,
        env={k: v for k, v in os.environ.items() if k != "CASEFILE_DATA_DIR"},
        check=True,
    ).stdout.strip()
    assert out == str((STUDIO / "data").resolve())


def test_data_root_honours_env_var(tmp_path):
    code = "import storage; print(storage.DATA)"
    out = subprocess.run(
        [sys.executable, "-c", code],
        cwd=STUDIO,
        capture_output=True,
        text=True,
        env={**os.environ, "CASEFILE_DATA_DIR": str(tmp_path)},
        check=True,
    ).stdout.strip()
    assert out == str(tmp_path.resolve())


def test_asset_paths_outside_root_survive_a_roundtrip(tmp_path, monkeypatch):
    outside = tmp_path / "disk" / "media" / "p1"
    outside.mkdir(parents=True)
    media = outside / "clip.jpg"
    Image.new("RGB", (32, 18), (10, 20, 30)).save(media)

    monkeypatch.setattr(storage, "DATA", tmp_path / "disk")
    monkeypatch.setattr(renderer, "DATA", tmp_path / "disk")

    stored = storage.asset_reference(media)
    assert Path(stored).is_absolute()
    assert storage.resolve_asset(stored) == media.resolve()
    assert renderer.asset_path({"path": stored}) == media.resolve()


def test_asset_paths_inside_root_stay_relative():
    inside = storage.DATA / "media" / "example.jpg"
    stored = storage.asset_reference(inside)
    assert not Path(stored).is_absolute()
    assert stored == str(inside.resolve().relative_to(storage.ROOT))


@pytest.mark.parametrize(
    "bad", ["", "../../../etc/passwd", "/etc/passwd", "/etc/shadow"]
)
def test_resolve_asset_refuses_paths_outside_allowed_roots(bad):
    with pytest.raises(ValueError):
        storage.resolve_asset(bad)


def test_health_endpoint_is_cheap_and_public(isolated):
    client, _ = isolated
    r = client.get("/healthz")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert "version" in body and "render" in body
    assert len(r.content) < 200


def test_uploaded_media_is_stored_under_the_data_root(isolated):
    client, root = isolated
    p = client.post(
        "/api/projects",
        json={"title": "Disk check", "mode": "topic", "target_minutes": 25},
    ).json()
    source = root / "source.png"
    Image.new("RGB", (64, 36), (90, 40, 20)).save(source)
    asset = client.post(
        f"/api/projects/{p['id']}/upload",
        files=[("files", ("S01.png", source.read_bytes(), "image/png"))],
        data={"episode_role": "sources"},
    ).json()["assets"][-1]

    # The stored path points at the bytes inside this test's data root, and it
    # round-trips through the renderer regardless of whether it is stored
    # relative to the checkout or as an absolute path on a mounted disk.
    resolved = renderer.asset_path(asset)
    assert resolved.is_file()
    assert resolved.is_relative_to(root.resolve())
    status = client.get(f"/api/projects/{p['id']}/media-status").json()
    assert [a["exists"] for a in status["assets"]] == [True]


def test_render_yaml_declares_disk_and_matching_storage_root():
    yaml = pytest.importorskip("yaml")
    blueprint = yaml.safe_load((STUDIO.parent / "render.yaml").read_text())
    service = next(
        s for s in blueprint["services"] if s["type"] == "web"
    )
    assert service["runtime"] == "docker"
    assert service["rootDir"] == "casefile-studio"
    # Docker paths are resolved relative to rootDir.
    assert service["dockerfilePath"] == "./Dockerfile"
    assert service["healthCheckPath"] == "/healthz"
    env = {e["key"]: e.get("value") for e in service["envVars"]}
    assert env["CASEFILE_DATA_DIR"] == service["disk"]["mountPath"]
    assert service["disk"]["sizeGB"] >= 1
