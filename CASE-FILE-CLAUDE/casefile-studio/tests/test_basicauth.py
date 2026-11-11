"""Public-host password gate: off by default, protects everything when set."""

import base64


def test_no_credentials_env_leaves_app_open(isolated):
    c, _ = isolated
    response = c.get("/api/config")
    assert response.status_code == 200


def test_basic_auth_blocks_anonymous_and_wrong_credentials(isolated, monkeypatch):
    c, _ = isolated
    monkeypatch.setenv("BASIC_AUTH_USER", "producer")
    monkeypatch.setenv("BASIC_AUTH_PASSWORD", "case-file-pass")
    anonymous = c.get("/api/config")
    assert anonymous.status_code == 401
    assert anonymous.headers["www-authenticate"].startswith("Basic")
    wrong = c.get(
        "/api/config",
        headers={"authorization": "Basic " + base64.b64encode(b"producer:nope").decode()},
    )
    assert wrong.status_code == 401


def test_basic_auth_accepts_correct_credentials(isolated, monkeypatch):
    c, _ = isolated
    monkeypatch.setenv("BASIC_AUTH_USER", "producer")
    monkeypatch.setenv("BASIC_AUTH_PASSWORD", "case-file-pass")
    token = base64.b64encode(b"producer:case-file-pass").decode()
    for path in ("/api/config", "/"):
        response = c.get(path, headers={"authorization": f"Basic {token}"})
        assert response.status_code == 200, path
