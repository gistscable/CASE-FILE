"""A rebuilt guide timeline must satisfy its own draft validator.

Gap cards deliberately repeat the cue's exact reviewed crop (renderer.py's loop
rule). They therefore need the cue's source/date disclosure, and the bounds
check must validate the crop rather than the looped scene duration.
"""

import episode
from test_episode import prepared


def rebuilt():
    p = prepared()
    episode.build(p, True, inspection=True)
    return p


def asset_gaps(p):
    return [s for s in p["scenes"] if s.get("guide_gap") and s.get("asset_id")]


def test_gap_cards_keep_the_cue_source_label():
    p = rebuilt()
    gaps = asset_gaps(p)
    assert gaps, "fixture should contain a gap that repeats a cue crop"
    cues = {
        c["id"]: episode.resolve_cue(p, c)
        for c in episode.state(p)["guide"]["cues"]
    }
    for scene in gaps:
        assert scene["source_label"] == cues[scene["guide_cue_id"]]["label"]
    assert "episode_source_label" not in [
        i["code"] for i in episode.issues(p) if i["blocks_draft"]
    ]


def test_repeated_crop_is_not_reported_as_out_of_bounds():
    p = rebuilt()
    video_gap = next(
        s for s in asset_gaps(p) if s.get("source_crop_end") is not None
    )
    window = episode.inspection_candidate(
        p, episode.state(p)["guide"]["cues"][0]
    )["window"]
    # The crop stays inside the reviewed window even though the gap loops it.
    assert video_gap["trim_start"] >= window["in"]
    assert video_gap["source_crop_end"] <= window["out"]
    assert video_gap["trim_start"] + video_gap["duration"] > window["out"]
    assert "episode_source_bounds" not in [
        i["code"] for i in episode.issues(p) if i["blocks_draft"]
    ]


def test_rebuilt_plan_has_no_blocking_issues():
    p = rebuilt()
    assert [i["code"] for i in episode.issues(p) if i["blocks_draft"]] == []
