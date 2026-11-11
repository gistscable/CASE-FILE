"""Base-image fill: naming, hints, relevance, variety, safety, build and render.

Synthetic, fictional material only. Nothing is downloaded and no real case is used.
"""

import io
import subprocess

import pytest
from PIL import Image

import app as server
import basefill
import editorial
import episode
import renderer
import storage
from test_episode import local_project, tone_bytes

SCRIPT = """HOOK

Alex Rivers was a fictional student who loved painting. Everyone in the fictional town of Harbor Vale knew his name.

CHAPTER 1

On a quiet evening a camera at the end of Mill Street caught movement near the old tracks. Officers arrived within minutes and sealed the area.

His mother Dana stood before the cameras and asked for answers. The family held a vigil on Friday evening and neighbors brought candles.

Months later Sam Drake appeared before the judge in the county courthouse. The hearing lasted less than an hour.
"""

GUIDE = """# Synthetic base-fill guide

**Standing boundaries:** Fictional test only. Keep narration unchanged; mute source audio.

## Project setup

- Case: Synthetic Harbor Vale test
- Victim: Alex Rivers
- Suspect: Sam Drake
- Avoid tags: graphic
- Avoid in CHAPTER 1: residential

## Script-by-script placement

### HOOK

1. **At:** “Alex Rivers was a fictional student” **Fill:** V / portrait **Show:** Portrait of the victim.

### CHAPTER 1

2. **At:** “On a quiet evening a camera” **Show:** Synthetic clip. **Preview:** `S03` [Preview](https://example.org/synthetic-video), around 0:01–0:03. **Label:** SYNTHETIC CLIP | 2026 **Care:** Technical fixture. **Fill:** C / location

3. **At:** “His mother Dana stood” **Fill:** V / family **Show:** The family.

4. **At:** “The family held a vigil” **Fill:** V / memorial **Show:** The vigil.

5. **At:** “Months later Sam Drake” **Fill:** S / court **Show:** The hearing.

## Source library

- **S03 — [Synthetic video](https://example.org/synthetic-video)**
  Test clip. **Rights:** Test-created pattern only.

## File checklist

| Save as | What it shows | Where | Tag |
|---|---|---|---|
| `BASE-V--portrait--01.jpg` | victim portrait | test | portrait |
| `BASE-V--memorial--01.jpg` | vigil | test | memorial |
| `BASE-S--court--01.jpg` | hearing | test | court |
| `BASE-C--location--01.mp4` | street | test | location |
"""


def make_project(duration=60.0, guide=GUIDE, script=SCRIPT):
    p = local_project()
    episode.import_document(p, "script", script, "base-script.md")
    episode.import_document(p, "guide", guide, "base-guide.md")
    v = {
        "id": storage.uid(),
        "name": "SYNTHETIC voice.wav",
        "kind": "audio",
        "duration": duration,
        "has_audio": True,
        "license": "Test tone.",
    }
    p["assets"].append(v)
    p["narration_id"] = v["id"]
    return p


def add_asset(p, name, kind="image", duration=0.0):
    a = {
        "id": storage.uid(),
        "name": name,
        "kind": kind,
        "duration": duration,
        "has_audio": kind == "video",
        "license": "Synthetic test fixture.",
    }
    p["assets"].append(a)
    return a


def full_pool(p, per=3):
    for bucket, tags in (
        ("V", ["portrait", "family", "memorial"]),
        ("S", ["court", "custody"]),
        ("C", ["location", "night"]),
    ):
        for tag in tags:
            for n in range(1, per + 1):
                add_asset(p, f"BASE-{bucket}--{tag}--{n:02d}.jpg")
    add_asset(p, "BASE-C--location--90.mp4", "video", 40)


def link_clip(p):
    a = add_asset(p, "S03.mp4", "video", 10)
    episode.bind_source(p, "S03", {"asset_id": a["id"], "rights_confirmed": True})
    episode.review_cue(p, "C02", {"reviewed": True, "in": 1, "out": 3})
    return a


def base_scenes(p):
    return [s for s in p["scenes"] if s.get("base_fill")]


# ---------------------------------------------------------------- naming / hints


@pytest.mark.parametrize(
    "name,bucket,tags",
    [
        ("BASE-V--portrait--01.jpg", "V", ["portrait"]),
        ("BASE-V--memorial+family--02.mp4", "V", ["memorial", "family"]),
        ("BASE-S--court--01.jpg", "S", ["court"]),
        ("BASE-C--location--01.mp4", "C", ["location"]),
        ("BASE-V-3.jpg", "V", []),
        ("base-c-1.JPG", "C", []),
        ("BASE-V--Vigil--07 (1).jpg", "V", ["memorial"]),
        ("BASE-V--daily life--2.jpg", "V", ["daily-life"]),
        ("BASE-V--portrait--smiling--03.png", "V", ["portrait"]),
    ],
)
def test_base_filenames_give_bucket_and_tags(name, bucket, tags):
    meta = basefill.parse_name(name)
    assert meta == {"bucket": bucket, "tags": tags}


@pytest.mark.parametrize("name", ["S01.mp4", "BASE-X-1.jpg", "my BASE-V photo.jpg", ""])
def test_other_files_are_not_base_images(name):
    assert basefill.parse_name(name) is None


def test_many_files_can_share_a_bucket_and_tag_without_name_clashes():
    p = make_project()
    for n in range(1, 13):
        add_asset(p, f"BASE-V--portrait--{n:02d}.jpg")
    items = basefill.pool(p)
    assert len(items) == 12 and len({i["id"] for i in items}) == 12
    assert {i["bucket"] for i in items} == {"V"}


@pytest.mark.parametrize(
    "raw,bucket,tags",
    [
        ("V / memorial", "V", ["memorial"]),
        ("S: court", "S", ["court"]),
        ("victim - family, memorial", "V", ["family", "memorial"]),
        ("C", "C", []),
        ("Scene / night", "C", ["night"]),
        ("V + family + funeral", "V", ["family", "memorial"]),
    ],
)
def test_fill_hints(raw, bucket, tags):
    hint = basefill.parse_hint(raw)
    assert hint["bucket"] == bucket and hint["tags"] == tags


def test_empty_hints_are_none():
    assert basefill.parse_hint("") is None
    assert basefill.parse_hint("none") is None
    assert basefill.parse_hint("auto") is None


def test_guide_parses_setup_base_files_and_fill_only_cards():
    p = make_project()
    guide = p["episode"]["guide"]
    setup = guide["setup"]
    assert setup["present"] and setup["victims"] == ["Alex Rivers"]
    assert setup["suspects"] == ["Sam Drake"]
    assert setup["avoid_tags"] == ["graphic"]
    assert setup["avoid_by_chapter"] == {"chapter-1": ["residential"]}
    assert "BASE-V--portrait--01.jpg" in guide["base_files"]
    assert len(guide["base_files"]) == 4
    fill_only = [c for c in guide["cues"] if c.get("fill_only")]
    assert [c["id"] for c in fill_only] == ["C01", "C03", "C04", "C05"]
    assert fill_only[1]["fill"]["tags"] == ["family"]
    # No fake source entry is created for fill-only cards.
    assert "BASE" not in {s["id"] for s in guide["sources"]}
    assert [c["id"] for c in guide["cues"] if not c.get("fill_only")] == ["C02"]


def test_card_without_source_or_fill_is_still_an_error():
    bad = GUIDE.replace("**Fill:** V / portrait ", "")
    with pytest.raises(ValueError, match="no source ID"):
        episode.parse_guide(bad)


# ---------------------------------------------------------------- segments


def test_short_stretch_is_one_shot_and_long_stretch_splits_on_phrase_starts():
    fps = 24
    assert basefill.plan_segments(0, 6 * fps, [], fps) == [(0, 6 * fps)]
    cuts = [int(x * fps) for x in (5.8, 12.3, 18.1, 24.2, 30.4, 36.0)]
    segs = basefill.plan_segments(0, 40 * fps, cuts, fps, 6, 8)
    assert segs[0][0] == 0 and segs[-1][1] == 40 * fps
    assert all(b == c for (_, b), (c, _) in zip(segs, segs[1:]))
    assert all((b - a) / fps <= 8.01 for a, b in segs)
    assert any(b in cuts for _, b in segs[:-1])  # snapped to a phrase start


def test_snapping_never_exceeds_the_hold_limit():
    fps = 24
    # Phrase starts placed so that a naive snap would create a 9+ second shot.
    cuts = [int(x * fps) for x in (3.0, 11.9, 12.4, 20.5, 28.7, 33.5)]
    for total in (20, 25, 31, 47, 63):
        segs = basefill.plan_segments(0, total * fps, cuts, fps, 6, 8)
        assert sum(b - a for a, b in segs) == total * fps
        assert all((b - a) / fps <= 8.0 + 1e-9 for a, b in segs), segs


def test_even_split_without_captions_stays_within_the_hold():
    segs = basefill.plan_segments(0, 100 * 24, [], 24, 6, 8)
    assert sum(b - a for a, b in segs) == 100 * 24
    assert all((b - a) / 24 <= 8.01 and (b - a) / 24 >= 4 for a, b in segs)


# ---------------------------------------------------------------- picker


def pool_items(spec):
    items = []
    for n, (bucket, tags, kind, duration) in enumerate(spec):
        items.append(
            {
                "id": f"id{n:02d}",
                "name": f"BASE-{bucket}-{n}.jpg",
                "kind": kind,
                "duration": duration,
                "bucket": bucket,
                "tags": tags,
            }
        )
    return items


SETUP = {
    "present": True,
    "victims": ["Alex Rivers"],
    "suspects": ["Sam Drake"],
    "avoid_tags": [],
    "avoid_by_chapter": {},
}


def planner(spec, **kw):
    return basefill.Planner(pool_items(spec), kw.pop("setup", SETUP), **kw)


def test_hint_tags_win_and_randomness_stays_among_relevant_images():
    spec = [("V", ["memorial"], "image", 0)] * 3 + [("V", ["portrait"], "image", 0)] * 3
    pl = planner(spec, seed=7)
    hint = basefill.parse_hint("V / memorial")
    for k in range(3):
        pick = pl.choose("They lit candles.", hint, "chapter-1", k * 100.0, 6)
        assert "memorial" in pick["meta"]["tags"]


def test_least_used_first_then_no_repeat_inside_spacing():
    spec = [("V", [], "image", 0)] * 4
    pl = planner(spec, seed=3, spacing=90)
    seen = []
    for k in range(4):
        pick = pl.choose("Alex Rivers loved painting.", None, "hook", k * 20.0, 6)
        seen.append(pick["asset_id"])
    assert len(set(seen)) == 4  # every image once before any repeats


def test_scarce_tag_repeats_before_wrong_topic_but_never_past_limit():
    spec = [
        ("V", ["memorial"], "image", 0),
        ("V", ["portrait"], "image", 0),
        ("C", ["location"], "image", 0),
        ("C", ["location"], "image", 0),
    ]
    pl = planner(spec, seed=1, max_uses=4)
    memorial = basefill.parse_hint("V / memorial")
    street = basefill.parse_hint("C / location")
    tags = []
    for k in range(5):
        # Another shot always sits between memorial shots (no back-to-back repeat).
        tags.append(pl.choose("The vigil.", memorial, "chapter-1", k * 20.0, 6)["meta"]["tags"])
        pl.choose("The street.", street, "chapter-1", k * 20.0 + 10, 6)
    assert tags[:4] == [["memorial"]] * 4  # relevance first, even inside the 90 s spacing
    assert tags[4] == ["portrait"]  # then bucket-wide, never a 5th memorial use
    assert max(pl.uses.values()) <= 4


def test_same_image_is_never_shown_twice_in_a_row_when_another_matches():
    spec = [("V", ["memorial"], "image", 0), ("V", ["portrait"], "image", 0)]
    pl = planner(spec, seed=1)
    memorial = basefill.parse_hint("V / memorial")
    first = pl.choose("The vigil.", memorial, "chapter-1", 0, 6)
    second = pl.choose("The vigil.", memorial, "chapter-1", 6, 6)
    assert first["meta"]["tags"] == ["memorial"] and second["meta"]["tags"] == ["portrait"]


def test_suspect_image_is_never_used_under_a_victim_family_line():
    spec = [("S", ["court"], "image", 0), ("V", [], "image", 0), ("C", [], "image", 0)]
    pl = planner(spec, seed=2)
    hint = basefill.parse_hint("S / court")
    pick = pl.choose("His mother wept at the funeral.", hint, "chapter-1", 0, 6)
    assert pick["meta"]["bucket"] == "V"
    assert any("safety" in n for n in pick["meta"]["notes"])
    ok = pl.choose("Sam Drake stood before the judge.", hint, "chapter-1", 200, 6)
    assert ok["meta"]["bucket"] == "S"


def test_without_hint_suspect_bucket_needs_the_suspect_named():
    spec = [("S", [], "image", 0), ("V", [], "image", 0), ("C", [], "image", 0)]
    pl = planner(spec, seed=2)
    named = pl.choose("Sam Drake was charged.", None, "chapter-1", 0, 6)
    assert named["meta"]["bucket"] == "S"
    for k in range(1, 7):
        neutral = pl.choose("Rain fell on the town.", None, "chapter-1", k * 300.0, 6)
        assert neutral["meta"]["bucket"] in ("V", "C")
    victim = pl.choose("Alex Rivers loved painting.", None, "chapter-1", 5000, 6)
    assert victim["meta"]["bucket"] == "V"


def test_neutral_lines_alternate_victim_and_scene():
    spec = [("V", [], "image", 0)] * 3 + [("C", [], "image", 0)] * 3
    pl = planner(spec, seed=5)
    buckets = [
        pl.choose("Nothing special here.", None, "chapter-1", k * 200.0, 6)["meta"]["bucket"]
        for k in range(6)
    ]
    assert buckets == ["C", "V", "C", "V", "C", "V"]


def test_suspect_with_no_suspect_images_falls_back_to_scene_not_victim():
    spec = [("V", [], "image", 0), ("C", [], "image", 0)]
    pl = planner(spec, seed=2)
    pick = pl.choose("Sam Drake appeared.", basefill.parse_hint("S"), "chapter-1", 0, 6)
    assert pick["meta"]["bucket"] == "C"


def test_chapter_restricted_tags_are_never_used():
    setup = {**SETUP, "avoid_by_chapter": {"chapter-3": ["residential"]}, "avoid_tags": ["graphic"]}
    spec = [("C", ["residential"], "image", 0), ("C", ["graphic"], "image", 0), ("C", ["location"], "image", 0)]
    pl = planner(spec, seed=4, setup=setup)
    for k in range(6):
        pick = pl.choose("The street.", basefill.parse_hint("C"), "chapter-3", k * 300.0, 6)
        assert pick is not None and pick["meta"]["tags"] == ["location"]
    assert pl.summary(1)["unfilled"] == 0 and pl.summary(1)["over_limit"] >= 1 and pl.summary(1)["back_to_back"] >= 1
    other = pl.choose("The street.", basefill.parse_hint("C / residential"), "chapter-2", 9000, 6)
    assert other["meta"]["tags"] == ["residential"]


def test_clips_shorter_than_the_shot_are_never_chosen_and_never_loop():
    spec = [("C", ["location"], "video", 3), ("C", ["location"], "video", 30)]
    pl = planner(spec, seed=9)
    for k in range(4):
        pick = pl.choose("The street.", basefill.parse_hint("C"), "chapter-1", k * 300.0, 6)
        assert pick["asset_id"] == "id01"
        assert pick["trim"] + 6 <= pick["source_crop_end"] + 1e-6 <= 30
        assert pick["motion"] == "none"


def test_same_seed_repeats_exactly_and_a_new_seed_shuffles():
    spec = [("V", [], "image", 0)] * 6 + [("C", [], "image", 0)] * 6

    def run(seed):
        pl = planner(spec, seed=seed)
        return [
            pl.choose("Quiet.", None, "chapter-1", k * 120.0, 6)["asset_id"]
            for k in range(12)
        ]

    assert run(1) == run(1)
    assert run(1) != run(2)


def test_stills_get_varied_motion_with_no_back_to_back_repeat():
    spec = [("V", ["portrait"], "image", 0)] * 3 + [("C", ["location"], "image", 0)] * 3
    pl = planner(spec, seed=6)
    motions = []
    for k in range(10):
        hint = basefill.parse_hint("V / portrait" if k % 2 == 0 else "C / location")
        pick = pl.choose("x", hint, "chapter-1", k * 200.0, 6)
        motions.append(pick["motion"])
    assert all(m in basefill.MOTIONS for m in motions)
    assert all(a != b for a, b in zip(motions, motions[1:]))
    assert {"slow-zoom", "slow-zoom-out"} <= set(motions)


def test_empty_pool_returns_none_and_logs_unfilled():
    pl2 = basefill.Planner([], SETUP, seed=1)
    assert pl2.choose("Anything.", None, "chapter-1", 0, 6) is None
    assert pl2.summary(1)["unfilled"] == 1


# ---------------------------------------------------------------- build


def test_no_base_files_leaves_the_plan_unchanged():
    p = make_project()
    link_clip(p)
    plan = episode.build(p, True)
    assert "base_fill" not in plan
    assert not base_scenes(p)
    # Legacy behaviour kept: the clip loops inside its own cue span.
    assert any(s.get("guide_source_id") == "S03" for s in p["scenes"])


def test_gaps_and_clip_tails_are_filled_from_the_pool_without_looping():
    p = make_project()
    link_clip(p)
    full_pool(p)
    plan = episode.build(p, True)
    scenes = p["scenes"]
    assert plan["gap_seconds"] == 0
    assert sum(round(s["duration"] * 24) for s in scenes) == round(plan["duration"] * 24)
    clip = [s for s in scenes if s.get("guide_source_id") == "S03"]
    # The 2 second approved window plays exactly once.
    assert len(clip) == 1 and clip[0]["duration"] == pytest.approx(2.0)
    tails = [s for s in base_scenes(p) if s["base_fill"]["reason"] == "clip-tail"]
    assert tails and all(s["guide_cue_id"] == "C02" for s in tails)
    # No scene repeats a clip: base videos start inside their file and end before it.
    for s in base_scenes(p):
        if s.get("source_crop_end") is not None:
            assert s["trim_start"] + s["duration"] <= s["source_crop_end"] + 1e-6
    assert all(s["duration"] <= 8.01 for s in base_scenes(p))
    assert plan["base_fill"]["fills"] == len(base_scenes(p))
    assert plan["base_fill"]["unfilled"] == 0


def test_hints_pick_matching_images_and_safety_keeps_suspect_out_of_grief_lines():
    p = make_project()
    link_clip(p)
    full_pool(p)
    episode.build(p, True)
    for s in base_scenes(p):
        fill = s["base_fill"]
        text = s["narration"].lower()
        if fill["reason"] == "fill-card" and "vigil" in text:
            assert fill["bucket"] == "V"
        if fill["bucket"] == "S":
            assert "sam drake" in text or "judge" in text or "hearing" in text
            assert "mother" not in text and "vigil" not in text
    courtroom = [
        s
        for s in base_scenes(p)
        if s["base_fill"]["reason"] == "fill-card" and "sam drake" in s["narration"].lower()
    ]
    assert courtroom and all(s["base_fill"]["bucket"] == "S" for s in courtroom)
    assert all("court" in s["base_fill"]["tags"] for s in courtroom)
    memorial = [s for s in base_scenes(p) if "vigil" in s["narration"].lower()]
    assert memorial and all("memorial" in s["base_fill"]["tags"] for s in memorial)


def test_fill_scenes_are_labelled_as_archive_images_and_keep_guide_links():
    p = make_project()
    link_clip(p)
    full_pool(p)
    episode.build(p, True)
    fills = base_scenes(p)
    assert fills and all("not footage of the narrated event" in s["source_label"] for s in fills)
    assert all(s["guide_gap"] is False and s["asset_id"] for s in fills)
    assert all(s["guide_source_id"] is None for s in fills)


def test_label_can_be_switched_off_but_scenes_still_carry_the_marker():
    p = make_project()
    link_clip(p)
    full_pool(p)
    p["episode"]["base_label"] = False
    episode.build(p, True)
    assert all(s["source_label"] == "" and s["base_fill"] for s in base_scenes(p))


def test_issues_do_not_block_a_plan_made_of_fills_and_report_stand_ins():
    p = make_project()
    link_clip(p)
    full_pool(p)
    episode.build(p, True)
    issues = episode.issues(p)
    assert not [i for i in issues if i["code"] == "episode_unguided_visual"]
    assert not [i for i in issues if i["code"] == "episode_source_choice_changed"]
    # A guide clip with no file is covered by a stand-in and called out.
    p["episode"]["bindings"]["S03"]["asset_id"] = None
    episode.build(p, True)
    codes = {i["code"] for i in episode.issues(p)}
    assert "episode_base_missing_clips" in codes
    assert p["episode"]["plan"]["base_fill"]["missing_clips"] == ["C02"]


def test_small_pool_is_reported_with_how_many_more_to_add():
    p = make_project(duration=600)
    link_clip(p)
    add_asset(p, "BASE-V--portrait--01.jpg")
    add_asset(p, "BASE-C--location--01.jpg")
    episode.build(p, True)
    details = " ".join(i["detail"] for i in episode.issues(p) if i["code"].startswith("episode_base"))
    assert "uploaded" in details and "more" in details
    codes = {i["code"] for i in episode.issues(p)}
    assert "episode_base_pool_small" in codes
    assert codes & {
        "episode_base_repeats",
        "episode_base_overused",
        "episode_base_back_to_back",
        "episode_base_unfilled",
    }


def test_missing_base_files_from_the_guide_checklist_are_listed():
    p = make_project()
    link_clip(p)
    add_asset(p, "BASE-V--portrait--01.jpg")
    episode.build(p, True)
    detail = next(
        i["detail"] for i in episode.issues(p) if i["code"] == "episode_base_files_missing"
    )
    assert "BASE-S--court--01.jpg" in detail and "BASE-V--portrait--01.jpg" not in detail


def test_same_seed_gives_an_identical_plan_and_reshuffle_changes_it():
    p = make_project(duration=300)
    link_clip(p)
    full_pool(p, per=4)
    first = episode.build(p, True)["timeline_digest"]
    again = episode.build(p, True)["timeline_digest"]
    assert first == again
    p["episode"]["base_seed"] = 2
    assert episode.build(p, True)["timeline_digest"] != first


def test_scene_limit_is_met_by_lengthening_fill_shots():
    p = make_project(duration=2600)
    full_pool(p, per=4)
    plan = episode.build(p, True)
    assert plan["scene_count"] <= 400
    assert plan["base_fill"]["hold"] > basefill.DEFAULT_MAX_HOLD
    assert plan["gap_seconds"] == 0


def test_disabling_base_fill_restores_marked_gaps():
    p = make_project()
    full_pool(p)
    p["episode"]["base_fill"] = False
    plan = episode.build(p, True)
    assert "base_fill" not in plan and plan["gap_seconds"] > 0


def test_plan_report_lists_every_fill():
    p = make_project()
    link_clip(p)
    full_pool(p)
    episode.build(p, True)
    text = episode.markdown(p)
    assert "## Base-image fills" in text and "BASE-" in text
    assert "base-image fill" in text  # fill-only cards are described


def test_every_word_and_second_survive_filling():
    p = make_project()
    link_clip(p)
    full_pool(p)
    plan = episode.build(p, True)
    ts = episode.tokens(p["episode"]["script"]["text"])
    spoken = [t[3] for t in episode.tokens(" ".join(s["narration"] for s in p["scenes"]))]
    assert spoken == [t[3] for t in ts]
    assert sum(s["duration"] for s in p["scenes"]) == pytest.approx(plan["duration"], abs=0.05)


# ---------------------------------------------------------------- API / sanitiser


def test_scene_sanitiser_keeps_new_motions_and_the_fill_marker():
    scene = {
        "id": "a" * 16,
        "title": "x",
        "chapter": "c",
        "narration": "n",
        "duration": 3,
        "motion": "slow-zoom-out",
        "guide_gap": False,
        "base_fill": {"bucket": "V", "tags": ["portrait"], "asset_name": "BASE-V-1.jpg", "reason": "gap"},
    }
    out = server.sanitize_scene(scene, set())
    assert out["motion"] == "slow-zoom-out"
    assert out["base_fill"]["bucket"] == "V" and out["base_fill"]["tags"] == ["portrait"]
    assert server.sanitize_scene({**scene, "motion": "pan-right"}, set())["motion"] == "pan-right"
    assert server.sanitize_scene({**scene, "motion": "spin"}, set())["motion"] == "slow-zoom"


def test_options_reshuffle_and_report_endpoint(isolated):
    c, _root = isolated
    p = c.post("/api/projects", json={"title": "Base API", "mode": "narration"}).json()
    url = "/api/projects/" + p["id"]
    for role, text in (("script", SCRIPT), ("guide", GUIDE)):
        assert c.post(
            url + "/episode/import", json={"role": role, "text": text, "filename": role + ".md"}
        ).status_code == 200
    pics = []
    for name in ("BASE-V--portrait--01.jpg", "BASE-V--memorial--01.jpg", "BASE-S--court--01.jpg", "BASE-C--location--01.jpg"):
        buf = io.BytesIO()
        Image.new("RGB", (320, 180), "#334455").save(buf, format="JPEG")
        pics.append(("files", (name, buf.getvalue(), "image/jpeg")))
    assert c.post(url + "/upload", data={"episode_role": "sources"}, files=pics).status_code == 200
    r = c.get(url + "/episode/base-report").json()
    assert r["enabled"] and r["pool"] == {"V": 2, "S": 1, "C": 1}
    assert r["setup"]["victims"] == ["Alex Rivers"] and len(r["guide_base_files"]) == 4
    assert not r["findings"] or all("code" in f for f in r["findings"])
    r = c.patch(url + "/episode/options", json={"reshuffle": True})
    assert r.status_code == 200
    assert c.get(url + "/episode/base-report").json()["seed"] == 2
    assert c.patch(url + "/episode/options", json={"base_fill": False}).status_code == 200
    assert c.get(url + "/episode/base-report").json()["enabled"] is False
    bad = c.patch(url + "/episode/options", json={"base_hold": 99})
    assert bad.status_code == 422


# ---------------------------------------------------------------- real render


def test_fills_render_with_zoom_out_pan_and_base_clips_without_looping(isolated, monkeypatch, tmp_path):
    c, _root = isolated
    p = c.post("/api/projects", json={"title": "Base render", "mode": "narration"}).json()
    url = "/api/projects/" + p["id"]
    for role, text in (("script", SCRIPT), ("guide", GUIDE)):
        assert c.post(
            url + "/episode/import", json={"role": role, "text": text, "filename": role + ".md"}
        ).status_code == 200
    clip = tmp_path / "BASE-C--location--02.mp4"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "color=c=0x445566:s=320x180:r=24:d=12",
         "-c:v", "libx264", "-threads", "1", "-pix_fmt", "yuv420p", str(clip)],
        check=True, capture_output=True,
    )
    files = []
    for name in ("BASE-V--portrait--01.jpg", "BASE-V--memorial--01.jpg", "BASE-V--family--01.jpg", "BASE-S--court--01.jpg"):
        buf = io.BytesIO()
        Image.new("RGB", (640, 360), "#2a3d49").save(buf, format="JPEG")
        files.append(("files", (name, buf.getvalue(), "image/jpeg")))
    files.append(("files", (clip.name, clip.read_bytes(), "video/mp4")))
    assert c.post(url + "/upload", data={"episode_role": "sources"}, files=files).status_code == 200
    r = c.post(url + "/upload", data={"episode_role": "narration"},
               files={"files": ("voice.wav", tone_bytes(24.0), "audio/wav")})
    assert r.status_code == 200
    voice_id = r.json()["assets"][-1]["id"]
    assert c.patch(url + "/episode/options", json={"narration_id": voice_id}).status_code == 200
    built = c.post(url + "/episode/build", json={"allow_placeholders": True})
    assert built.status_code == 200, built.text
    proj = built.json()["project"]
    fills = [s for s in proj["scenes"] if s.get("base_fill")]
    assert fills, "expected base-image scenes"
    motions = {s["motion"] for s in fills}
    assert motions & {"slow-zoom", "slow-zoom-out", "pan-left", "pan-right"}
    calls = []
    run = renderer.run

    def capture(command, cancelled=None):
        calls.append(command[:])
        return run(command, cancelled)

    monkeypatch.setattr(renderer, "run", capture)
    record = server.write_export(
        proj, {"resolution": "480p", "draft": True, "captions": True}, lambda *_: None, lambda: False
    )
    out = storage.DATA / "exports" / record["id"] / "documentary.mp4"
    info = renderer.probe(out)
    assert info["has_audio"] and info["width"] == 854
    assert abs(info["duration"] - 24.0) < 0.2
    assert all("-stream_loop" not in cmd for cmd in calls)
    joined = " ".join(" ".join(str(v) for v in cmd) for cmd in calls)
    assert "zoompan" in joined
    plan_text = (storage.DATA / "exports" / record["id"] / "episode-plan.md").read_text()
    assert "Base-image fills" in plan_text
    assert editorial.inspect(proj)["ready_for_draft"]


# ---------------------------------------------------------------- shipped example


def test_shipped_example_guide_matches_its_script_and_builds_with_its_own_file_list():
    folder = storage.ROOT / "examples/base-fill"
    p = {
        "id": storage.uid(),
        "title": "Example",
        "mode": "narration",
        "is_demo": False,
        "script": "",
        "sources": [],
        "assets": [],
        "scenes": [],
        "narration_id": None,
        "music_id": None,
        "music_volume": 0.12,
        "captions": True,
        "look": "noir",
        "review": {"facts": False, "picture": False, "rights": False, "disclosure": False},
    }
    episode.import_document(p, "script", (folder / "narration-script.md").read_text(), "script.md")
    episode.import_document(p, "guide", (folder / "editing-guide-example.md").read_text(), "guide.md")
    v = {
        "id": storage.uid(),
        "name": "voice.wav",
        "kind": "audio",
        "duration": 60.0,
        "has_audio": True,
        "license": "Test tone.",
    }
    p["assets"].append(v)
    p["narration_id"] = v["id"]
    report = episode.analyze(p)
    assert not report["errors"] and report["matched_cues"] == report["cue_count"] == 5
    listed = p["episode"]["guide"]["base_files"]
    assert len(listed) == 7
    for name in listed:
        kind = "video" if name.endswith(".mp4") else "image"
        add_asset(p, name, kind, 12 if kind == "video" else 0)
    clip = add_asset(p, "S01.mp4", "video", 10)
    episode.bind_source(p, "S01", {"asset_id": clip["id"], "rights_confirmed": True})
    episode.review_cue(p, "C02", {"reviewed": True, "in": 10 - 9, "out": 5})
    plan = episode.build(p, True)
    assert plan["gap_seconds"] == 0 and plan["base_fill"]["unfilled"] == 0
    assert not any(i["code"] == "episode_base_files_missing" for i in episode.issues(p))
    court = [s for s in base_scenes(p) if s["base_fill"]["bucket"] == "S"]
    assert court and all("court" in s["base_fill"]["tags"] for s in court)


# ---------------------------------------------------------------- dates, exclusions, sign-off


def test_year_tags_and_exclusions_parse():
    assert basefill.parse_name("BASE-S--court+2024--01.jpg") == {"bucket": "S", "tags": ["court", "2024"]}
    assert basefill.parse_name("BASE-S--court--2026--02.jpg")["tags"] == ["court", "2026"]
    assert basefill.parse_name("BASE-V--portrait--01.jpg")["tags"] == ["portrait"]
    for raw in ("S / court+2024 / !2026", "S / court+2024 / not 2026", "S: court+2024 except 2026"):
        hint = basefill.parse_hint(raw)
        assert hint["bucket"] == "S" and hint["tags"] == ["court", "2024"] and hint["exclude"] == ["2026"]


def test_excluded_year_is_never_used_even_when_nothing_else_fits():
    spec = [
        ("S", ["court", "2026"], "image", 0),
        ("S", ["court", "2026"], "image", 0),
        ("C", ["location"], "image", 0),
    ]
    pl = planner(spec, seed=3)
    hint = basefill.parse_hint("S / court+2024 / !2026")
    for k in range(5):
        pick = pl.choose("Sam Drake at the pretrial hearing.", hint, "chapter-4", k * 300.0, 6)
        # The only suspect images are from 2026, so the scene bucket is used instead.
        assert pick["meta"]["bucket"] == "C"


def test_images_matching_every_requested_tag_win_over_partial_matches():
    spec = [
        ("S", ["court", "2026"], "image", 0),
        ("S", ["court", "2024"], "image", 0),
        ("S", ["custody"], "image", 0),
    ]
    pl = planner(spec, seed=8)
    hint = basefill.parse_hint("S / court+2024")
    first = pl.choose("Sam Drake at the hearing.", hint, "chapter-4", 0, 6)
    assert first["meta"]["tags"] == ["court", "2024"]
    assert first["meta"]["tier"] == "tag-match"


def test_signoff_records_the_reuse_note_on_base_images(isolated):
    c, _root = isolated
    p = c.post("/api/projects", json={"title": "Base signoff", "mode": "narration"}).json()
    url = "/api/projects/" + p["id"]
    for role, text in (("script", SCRIPT), ("guide", GUIDE)):
        assert c.post(
            url + "/episode/import", json={"role": role, "text": text, "filename": role + ".md"}
        ).status_code == 200
    files = []
    for name in ("BASE-V--portrait--01.jpg", "BASE-S--court--01.jpg"):
        buf = io.BytesIO()
        Image.new("RGB", (320, 180), "#334455").save(buf, format="JPEG")
        files.append(("files", (name, buf.getvalue(), "image/jpeg")))
    assert c.post(url + "/upload", data={"episode_role": "sources"}, files=files).status_code == 200
    before = c.get(url).json()
    assert all(not a["license"] for a in before["assets"])
    assert c.post(url + "/signoff", json={"confirmed": True}).status_code == 200
    after = c.get(url).json()
    notes = {a["name"]: a["license"] for a in after["assets"]}
    assert notes["BASE-V--portrait--01.jpg"].startswith("Producer sign-off")
    assert notes["BASE-S--court--01.jpg"].startswith("Producer sign-off")


# ---------------------------------------------------------------- clips as base images


def test_guide_windows_for_base_clips_are_read_from_table_rows():
    raw = (
        "| `BASE-C--location--02.mp4` | street | news report, 0:40–0:52 | location |\n"
        "| `BASE-V--portrait--01.jpg` | portrait | police | portrait |\n"
        "| `BASE-S--court--03.mov` | hearing | court feed 1:02:10 - 1:02:25 | court |\n"
        "| `BASE-C--night--04.mp4` | night | no window here | night |\n"
    )
    assert basefill.parse_base_windows(raw) == {
        "base-c--location--02.mp4": (40.0, 52.0),
        "base-s--court--03.mov": (3730.0, 3745.0),
    }


def window_project(file_duration, window_line):
    guide = GUIDE.replace("## File checklist", window_line + "\n\n## File checklist", 1)
    p = make_project(duration=120, guide=guide)
    add_asset(p, "BASE-C--location--02.mp4", "video", file_duration)
    return p


def test_base_clip_plays_only_inside_the_guide_window_and_never_loops():
    p = window_project(600, "| `BASE-C--location--02.mp4` | street | news report, 0:40–0:52 | location |")
    item = [i for i in basefill.pool(p) if i["kind"] == "video"][0]
    assert item["window"] == (40.0, 52.0)
    pl = basefill.Planner([item], SETUP, seed=4)
    for k in range(6):
        pick = pl.choose("The street.", basefill.parse_hint("C"), "chapter-1", k * 300.0, 5)
        assert 40.0 <= pick["trim"] and pick["source_crop_end"] <= 52.0 + 1e-6
        assert pick["source_crop_end"] - pick["trim"] == pytest.approx(5.0)


def test_window_shorter_than_the_shot_makes_the_clip_ineligible():
    p = window_project(600, "| `BASE-C--location--02.mp4` | street | news report, 0:40–0:43 | location |")
    item = [i for i in basefill.pool(p) if i["kind"] == "video"][0]
    pl = basefill.Planner([item], SETUP, seed=4)
    assert pl.choose("The street.", basefill.parse_hint("C"), "chapter-1", 0, 5) is None


def test_a_clip_you_already_trimmed_is_used_whole_even_if_the_guide_names_a_window():
    p = window_project(12, "| `BASE-C--location--02.mp4` | street | news report, 0:40–0:52 | location |")
    item = [i for i in basefill.pool(p) if i["kind"] == "video"][0]
    assert item["window"] is None  # 12 s file cannot contain 0:40–0:52
    pl = basefill.Planner([item], SETUP, seed=4)
    pick = pl.choose("The street.", basefill.parse_hint("C"), "chapter-1", 0, 5)
    assert 0 <= pick["trim"] and pick["source_crop_end"] <= 12 + 1e-6


def test_long_clip_without_a_window_is_flagged():
    p = make_project()
    add_asset(p, "BASE-C--location--05.mp4", "video", 600)
    add_asset(p, "BASE-C--location--06.mp4", "video", 20)
    findings = basefill.pool_warnings(basefill.pool(p))
    assert [f["code"] for f in findings] == ["base_long_uncropped"]
    assert "BASE-C--location--05.mp4" in findings[0]["detail"]
    assert "BASE-C--location--06.mp4" not in findings[0]["detail"]
    link_clip(p)
    episode.build(p, True)
    assert any(i["code"] == "episode_base_long_uncropped" for i in episode.issues(p))
