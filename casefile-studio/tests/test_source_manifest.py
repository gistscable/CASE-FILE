"""The source download manifest must stay truthful to the supplied guide.

No network, no media, no licensing: these checks only prove that every row in
`sources/manifest.json` still points at the exact upload the guide names, that
the canonical file names are unique and stable, and that the 32 BLOCKED beats
are recorded as having no media at all.
"""

import importlib.util
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "examples/the-last-timeline/sources"
GUIDE = ROOT / "examples/the-last-timeline/diverse-revision-guide.md"
MANIFEST = SOURCES / "manifest.json"
CSV = SOURCES / "sources.csv"
WINDOWS = SOURCES / "windows.csv"

NAME_RE = re.compile(r"^C\d\d__\d{4}-\d\d-\d\d__[a-z0-9-]+__[a-z0-9-]+__[A-Za-z0-9_-]{11}\.mp4$")


def tool():
    spec = importlib.util.spec_from_file_location(
        "fetch_youtube_sources", ROOT / "tools/fetch_youtube_sources.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def manifest():
    return json.loads(MANIFEST.read_text())


@pytest.fixture(scope="module")
def guide_text():
    return GUIDE.read_text()


def test_manifest_matches_guide_library(manifest, guide_text):
    """Every source row agrees with the guide's own source-library heading."""
    library = guide_text[
        guide_text.index("## Source library — YouTube only"):
        guide_text.index("### BLOCKED source registry")
    ]
    assert manifest["sources"], "manifest lists no sources"
    for source in manifest["sources"]:
        heading = f'### {source["id"]} — {source["title"]}\n'
        assert heading in library, f'{source["id"]} heading/title drifted from the guide'
        block = library[library.index(heading):]
        block = block[: block.find("\n### ") if "\n### " in block else len(block)]
        assert f'https://www.youtube.com/watch?v={source["video_id"]}' in block, source["id"]
        assert f'**{source["uploader"]}**' in block, source["id"]
        assert f'**{source["upload_date"]}**' in block, source["id"]


def test_counts_and_runtime(manifest):
    guide = manifest["guide"]
    assert guide["source_count"] == 21 == len(manifest["sources"])
    assert [s["id"] for s in manifest["sources"]] == [f"C{i:02d}" for i in range(1, 22)]
    assert guide["blocked_placements"] == 32 == len(manifest["blocked"])
    assert guide["distinct_selected_windows"] == 73
    assert guide["picture_assigned_placements"] == 73
    assert guide["baseline_end"] == "00:31:37,100"
    assert 4000 < sum(s["duration_seconds"] for s in manifest["sources"]) < 4100  # 67½ min


def test_video_ids_and_urls(manifest):
    ids = [s["video_id"] for s in manifest["sources"]]
    assert len(set(ids)) == len(ids) == 21, "each upload must be fetched exactly once"
    for source in manifest["sources"]:
        assert len(source["video_id"]) == 11
        assert source["url"] == f'https://www.youtube.com/watch?v={source["video_id"]}'
        assert re.fullmatch(r"\d{4}-\d\d-\d\d", source["upload_date"])
        assert source["duration_seconds"] > 0
        assert source["role"] in {"picture source", "research/context only"}


def test_file_names_are_canonical_and_unique(manifest):
    names = [s["file_name"] for s in manifest["sources"]]
    assert len(set(names)) == len(names), "two sources would be written to one file"
    builder = tool().build_file_name
    for source in manifest["sources"]:
        assert NAME_RE.match(source["file_name"]), source["file_name"]
        assert source["file_name"] == builder(source), "file name drifted from the naming rule"
        assert source["file_name"].startswith(f'{source["id"]}__{source["upload_date"]}__')
        assert source["video_id"] in source["file_name"]
        assert len(source["file_name"]) <= 150, "keep names portable across filesystems"
    # Rebuilding from a manifest row is idempotent: rename-then-rename cannot churn.
    assert all(builder(s) == s["file_name"] for s in manifest["sources"])


def test_windows_belong_to_their_placements(manifest):
    seen = set()
    for source in manifest["sources"]:
        placed = set(source["placements"])
        for window in source["windows"]:
            assert window["placement"] in placed, (source["id"], window)
            assert window["description"].strip()
            start, end = window["start"], window["end"]
            assert re.fullmatch(r"\d\d:\d\d:\d\d,\d{3}", start)
            assert re.fullmatch(r"\d\d:\d\d:\d\d,\d{3}", end)
            assert start < end
            seen.add(window["placement"])
    assert len(seen) == 73, "the guide assigns picture to 73 placements"


def test_blocked_beats_have_no_media(manifest):
    blocked_ids = {b["registry_id"] for b in manifest["blocked"]}
    assert len(blocked_ids) == 32
    assert all(re.fullmatch(r"G\d{3}", bid) for bid in blocked_ids)
    assert not blocked_ids & {s["id"] for s in manifest["sources"]}
    for entry in manifest["blocked"]:
        assert entry["reason"].strip()
        assert 1 <= entry["placement"] <= 105
        assert "video_id" not in entry and "file_name" not in entry, (
            "a BLOCKED beat must never gain an invented media id"
        )
    # 32 blocked + 73 picture-assigned beats cover the guide's 105 placements.
    assert len({w["placement"] for s in manifest["sources"] for w in s["windows"]}
               | {b["placement"] for b in manifest["blocked"]}) == 105


def test_csv_mirrors_the_manifest(manifest):
    rows = CSV.read_text().strip().splitlines()
    assert len(rows) == 1 + len(manifest["sources"])
    assert rows[0].startswith("source_id,file_name,video_id,url,title")
    for row, source in zip(rows[1:], manifest["sources"]):
        assert row.split(",")[0] == source["id"]
        assert source["file_name"] in row


def test_windows_csv_lists_every_selected_crop(manifest):
    rows = WINDOWS.read_text().strip().splitlines()
    assert len(rows) == 1 + 73
    assert rows[0].startswith("placement,source_id,file_name,source_start,source_end")
    placements = [int(row.split(",", 1)[0]) for row in rows[1:]]
    assert placements == sorted(placements)
    total = sum(len(s["windows"]) for s in manifest["sources"])
    assert total == len(placements) == 73


def test_media_policy_says_not_committed(manifest):
    policy = manifest["media_policy"]
    assert policy["committed_to_git"] is False
    assert "downloads" in policy["reason"]
    assert "not" in policy["rights"].lower()


def test_rename_matching_uses_the_youtube_id(manifest):
    helper = tool()
    ids = {s["video_id"] for s in manifest["sources"]}
    assert helper.match_video_id("Some random name a0NS9AsqdeA.mp4", ids) == "a0NS9AsqdeA"
    assert helper.match_video_id("a0NS9AsqdeA.mp4", ids) == "a0NS9AsqdeA"
    # A substring that merely contains a known id must not hijack another file.
    assert helper.match_video_id("xa0NS9AsqdeAx.mp4", ids) is None
    assert helper.match_video_id("unrelated.mp4", ids) is None


def test_slug_is_ascii_and_bounded():
    helper = tool()
    assert helper.slug("'I feel cheated': Family of murdered 14-year-old") == (
        "i-feel-cheated-family-of-murdered-14-year-old"
    )
    long = helper.slug("word " * 40)
    assert len(long) <= helper.TITLE_SLUG_MAX
    assert not long.endswith("-")
    assert helper.slug("Jahmir Moore sentenced in murder of Tampa 14-year-old") == (
        "jahmir-moore-sentenced-in-murder-of-tampa-14-year-old"
    )


def test_unknown_and_blocked_ids_are_refused(manifest):
    helper = tool()
    with pytest.raises(SystemExit) as blocked:
        helper.select_sources(manifest, "C01,G033")
    assert blocked.value.code == 2
    with pytest.raises(SystemExit) as unknown:
        helper.select_sources(manifest, "C99")
    assert unknown.value.code == 2
    assert [s["id"] for s in helper.select_sources(manifest, "c04, C05")] == ["C04", "C05"]
