"""Mode O: original-audio breaks (narration pauses, the clip plays with its own sound).

Synthetic, fictional material only.
"""

import io
import subprocess
import wave

import numpy as np
import pytest
from PIL import Image

import app as server
import audiobreak
import editorial
import episode
import renderer
import storage
from test_basefill import GUIDE, SCRIPT, add_asset, base_scenes, full_pool, link_clip, make_project

BREAK_GUIDE = GUIDE.replace(
    "**Fill:** C / location",
    "**Fill:** C / location **Audio break:** 0:02–0:06",
    1,
)


def project(guide=BREAK_GUIDE, duration=60.0):
    return make_project(duration=duration, guide=guide)


def cleared_project(**kw):
    p = project(**kw)
    link_clip(p)
    episode.bind_source(p, "S03", {"audio_cleared": True})
    return p


def inserts(p):
    return [s for s in p["scenes"] if s.get("insert_audio")]


# ---------------------------------------------------------------- parsing


@pytest.mark.parametrize(
    "text,window",
    [
        ("0:20–0:32", {"in": 20.0, "out": 32.0}),
        ("0:20-0:32", {"in": 20.0, "out": 32.0}),
        ("1:02:10 to 1:02:25", {"in": 3730.0, "out": 3745.0}),
        ("20s–32s", {"in": 20.0, "out": 32.0}),
        ("window 0:05.5–0:09", {"in": 5.5, "out": 9.0}),
        ("", None),
        ("none", None),
    ],
)
def test_audio_break_windows(text, window):
    assert audiobreak.parse(text) == window


@pytest.mark.parametrize("text", ["0:20", "soon", "0:20–0:21", "0:00–0:45"])
def test_bad_windows_are_refused(text):
    with pytest.raises(ValueError):
        audiobreak.parse(text)


def test_guide_reads_the_break_and_names_the_card_when_it_is_wrong():
    cue = next(c for c in episode.parse_guide(BREAK_GUIDE)["cues"] if c["id"] == "C02")
    assert cue["audio_break"] == {"in": 2.0, "out": 6.0}
    bad = GUIDE.replace("**Fill:** C / location", "**Fill:** C / location **Audio break:** 0:02–0:03", 1)
    with pytest.raises(ValueError, match="Placement 2"):
        episode.parse_guide(bad)
    plain = next(c for c in episode.parse_guide(GUIDE)["cues"] if c["id"] == "C02")
    assert plain["audio_break"] is None


# ---------------------------------------------------------------- clearance


def test_clearing_audio_needs_the_reuse_basis_first_and_resets_with_the_notes():
    p = project()
    clip = add_asset(p, "S03.mp4", "video", 10)
    episode.bind_source(p, "S03", {"asset_id": clip["id"]})
    with pytest.raises(ValueError, match="reuse basis"):
        episode.bind_source(p, "S03", {"audio_cleared": True})
    episode.bind_source(p, "S03", {"rights_confirmed": True})
    episode.bind_source(p, "S03", {"audio_cleared": True})
    assert p["episode"]["bindings"]["S03"]["audio_cleared"] is True
    episode.bind_source(p, "S03", {"license": "Changed notes."})
    assert "audio_cleared" not in p["episode"]["bindings"]["S03"]
    episode.bind_source(p, "S03", {"rights_confirmed": True})
    episode.bind_source(p, "S03", {"audio_cleared": True})
    episode.bind_source(p, "S03", {"rights_confirmed": False})
    assert "audio_cleared" not in p["episode"]["bindings"]["S03"]


def test_a_file_without_sound_cannot_be_cleared():
    p = project()
    clip = add_asset(p, "S03.mp4", "video", 10)
    clip["has_audio"] = False
    episode.bind_source(p, "S03", {"asset_id": clip["id"]})
    episode.bind_source(p, "S03", {"rights_confirmed": True})
    with pytest.raises(ValueError, match="no audio"):
        episode.bind_source(p, "S03", {"audio_cleared": True})


# ---------------------------------------------------------------- build


def test_cleared_break_is_inserted_before_its_card_and_narration_is_untouched():
    p = cleared_project()
    plan = episode.build(p, True)
    breaks = inserts(p)
    assert len(breaks) == 1 and breaks[0]["duration"] == pytest.approx(4.0)
    index = p["scenes"].index(breaks[0])
    after = p["scenes"][index + 1]
    assert after["guide_cue_id"] == "C02" and after["guide_source_id"] == "S03"
    assert breaks[0]["trim_start"] == pytest.approx(2.0)
    assert breaks[0]["source_crop_end"] == pytest.approx(6.0)
    assert breaks[0]["narration"] == "" and breaks[0]["captions"] == []
    # Narration length is unchanged; the video is longer by the break.
    assert plan["duration"] == pytest.approx(60.0, abs=0.05)
    assert plan["insert_seconds"] == pytest.approx(4.0)
    assert plan["total_duration"] == pytest.approx(64.0, abs=0.05)
    assert sum(s["duration"] for s in p["scenes"]) == pytest.approx(64.0, abs=0.05)
    # Every word still appears in order, and the narration cursor skips the break.
    cursor = 0.0
    for s in p["scenes"]:
        if s.get("insert_audio"):
            continue
        assert s["audio_start"] == pytest.approx(cursor, abs=0.003)
        cursor += round(s["duration"] * 24) / 24
    assert cursor == pytest.approx(60.0, abs=0.05)
    spoken = [t[3] for t in episode.tokens(" ".join(s["narration"] for s in p["scenes"]))]
    assert spoken == [t[3] for t in episode.tokens(p["episode"]["script"]["text"])]
    assert plan["audio_breaks"][0]["cue"] == "C02" and plan["source_audio"].startswith("muted except")


def test_a_break_does_not_trip_the_continuity_or_plan_checks():
    p = cleared_project()
    episode.build(p, True)
    codes = {i["code"] for i in episode.issues(p)}
    assert "episode_narration_continuity" not in codes
    assert "episode_audio_break_invalid" not in codes
    assert "episode_timeline_changed" not in codes
    assert "episode_unguided_visual" not in codes


def test_the_break_window_never_becomes_the_cards_muted_window_or_its_loop():
    p = cleared_project()
    episode.build(p, True)
    scenes = [s for s in p["scenes"] if s.get("guide_cue_id") == "C02" and not s.get("insert_audio")]
    assert scenes
    for s in scenes:
        # The muted window approved for the card is 1–3 s; the break is 2–6 s.
        assert s["trim_start"] == pytest.approx(1.0)
        assert s["source_crop_end"] == pytest.approx(3.0)


def test_with_base_images_the_card_after_a_break_is_covered_normally():
    p = cleared_project()
    full_pool(p)
    plan = episode.build(p, True)
    assert plan["gap_seconds"] == 0 and len(inserts(p)) == 1
    assert base_scenes(p)


def test_uncleared_break_is_left_out_with_a_notice_that_does_not_block_drafts():
    p = project()
    link_clip(p)
    plan = episode.build(p, True)
    assert not inserts(p)
    assert plan["audio_breaks_skipped"][0]["cue"] == "C02"
    assert plan["total_duration"] == pytest.approx(plan["duration"])
    notice = [i for i in episode.issues(p) if i["code"] == "episode_audio_break_waiting"]
    assert notice and not notice[0]["blocks_draft"] and "C02" in notice[0]["detail"]


def test_break_is_skipped_when_the_file_has_no_sound_or_the_window_is_too_long():
    p = cleared_project()
    clip = next(a for a in p["assets"] if a["name"] == "S03.mp4")
    clip["duration"] = 5  # the 2–6 s window now runs past the end of the file
    plan = episode.build(p, True)
    assert not inserts(p) and "past the end" in plan["audio_breaks_skipped"][0]["reason"]


def test_a_hand_edited_break_is_caught():
    p = cleared_project()
    episode.build(p, True)
    brk = inserts(p)[0]
    brk["trim_start"] = 3.0
    brk["source_crop_end"] = 7.0
    codes = {i["code"] for i in episode.issues(p)}
    assert "episode_audio_break_invalid" in codes
    assert "episode_timeline_changed" in codes


def test_removing_the_clearance_makes_the_old_plan_stale_and_invalid():
    p = cleared_project()
    episode.build(p, True)
    episode.bind_source(p, "S03", {"audio_cleared": False})
    codes = {i["code"] for i in episode.issues(p)}
    assert "episode_audio_break_invalid" in codes and "episode_plan_stale" in codes


def test_spacing_and_count_guidance_is_a_note_not_an_error():
    breaks = [{"cue": f"C{n:02d}", "at": n * 60.0} for n in range(1, 11)]
    notes = audiobreak.notes(breaks)
    assert any("10 audio breaks" in n for n in notes)
    assert any("apart" in n for n in notes)
    assert audiobreak.notes([{"cue": "C01", "at": 10.0}, {"cue": "C02", "at": 400.0}]) == []


def test_plan_report_lists_the_break_and_the_ripple():
    p = cleared_project()
    episode.build(p, True)
    text = episode.markdown(p)
    assert "## Audio breaks (original sound)" in text
    assert "| C02 |" in text and "Total added: 4.0s" in text
    assert "moves later" in text


# ---------------------------------------------------------------- end to end


def sweep_wav(seconds, rate=16000):
    t = np.arange(round(seconds * rate)) / rate
    samples = (np.sin(2 * np.pi * (300 * t + 25 * t * t)) * 9000).astype("<i2")  # f = 300 + 50 t Hz
    out = io.BytesIO()
    with wave.open(out, "wb") as w:
        w.setparams((1, 2, rate, 0, "NONE", "not compressed"))
        w.writeframes(samples.tobytes())
    return out.getvalue()


def tone_wav(hz, seconds, rate=16000):
    t = np.arange(round(seconds * rate)) / rate
    samples = (np.sin(2 * np.pi * hz * t) * 9000).astype("<i2")
    out = io.BytesIO()
    with wave.open(out, "wb") as w:
        w.setparams((1, 2, rate, 0, "NONE", "not compressed"))
        w.writeframes(samples.tobytes())
    return out.getvalue()


def dominant(path, start, length):
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", str(start), "-t", str(length), "-i", str(path), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
        check=True,
        capture_output=True,
    ).stdout
    data = np.frombuffer(raw, dtype="<i2").astype(float)
    spectrum = np.abs(np.fft.rfft(data * np.hanning(len(data))))
    return float(np.argmax(spectrum) * 16000 / len(data))


@pytest.mark.parametrize("with_music", [False, True])
def test_the_break_plays_the_clips_own_sound_and_narration_resumes_at_the_same_word(isolated, monkeypatch, tmp_path, with_music):
    c, _root = isolated
    p = c.post("/api/projects", json={"title": "Mode O render", "mode": "narration"}).json()
    url = "/api/projects/" + p["id"]
    for role, text in (("script", SCRIPT), ("guide", BREAK_GUIDE)):
        assert c.post(url + "/episode/import", json={"role": role, "text": text, "filename": role + ".md"}).status_code == 200
    clip = tmp_path / "S03.mp4"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "color=c=0x445566:s=320x180:r=24:d=10",
         "-f", "lavfi", "-i", "sine=frequency=1500:duration=10", "-c:v", "libx264", "-threads", "1",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(clip)],
        check=True, capture_output=True,
    )
    files = [("files", (clip.name, clip.read_bytes(), "video/mp4"))]
    for name in ("BASE-V--portrait--01.jpg", "BASE-C--location--01.jpg", "BASE-S--court--01.jpg"):
        buf = io.BytesIO()
        Image.new("RGB", (640, 360), "#2a3d49").save(buf, format="JPEG")
        files.append(("files", (name, buf.getvalue(), "image/jpeg")))
    assert c.post(url + "/upload", data={"episode_role": "sources"}, files=files).status_code == 200
    r = c.post(url + "/upload", data={"episode_role": "narration"}, files={"files": ("voice.wav", sweep_wav(24.0), "audio/wav")})
    assert r.status_code == 200
    voice_id = r.json()["assets"][-1]["id"]
    assert c.patch(url + "/episode/options", json={"narration_id": voice_id}).status_code == 200
    if with_music:
        # A 220 Hz music bed must duck under the clip's own sound, not replace it.
        m = c.post(url + "/upload", data={"episode_role": "music"}, files={"files": ("bed.wav", tone_wav(220, 40.0), "audio/wav")})
        assert m.status_code == 200
        music_id = m.json()["assets"][-1]["id"]
        assert c.patch(url + "/episode/options", json={"music_id": music_id}).status_code == 200
    assert c.post(url + "/episode/autolink").status_code == 200
    assert c.patch(url + "/episode/source/S03", json={"license": "Synthetic test clip."}).status_code == 200
    assert c.patch(url + "/episode/source/S03", json={"rights_confirmed": True}).status_code == 200
    assert c.patch(url + "/episode/cue/C02", json={"reviewed": True, "in": 1, "out": 3}).status_code == 200
    assert c.patch(url + "/episode/source/S03", json={"audio_cleared": True}).status_code == 200
    built = c.post(url + "/episode/build", json={"allow_placeholders": True})
    assert built.status_code == 200, built.text
    proj = built.json()["project"]
    plan = proj["episode"]["plan"]
    at = plan["audio_breaks"][0]["at"]
    assert plan["insert_seconds"] == pytest.approx(4.0)
    calls = []
    run = renderer.run

    def capture(command, cancelled=None):
        calls.append(command[:])
        return run(command, cancelled)

    monkeypatch.setattr(renderer, "run", capture)
    record = server.write_export(proj, {"resolution": "480p", "draft": True, "captions": True}, lambda *_: None, lambda: False)
    out = storage.DATA / "exports" / record["id"] / "documentary.mp4"
    info = renderer.probe(out)
    assert info["has_audio"]
    assert abs(info["duration"] - 28.0) < 0.25  # 24 s of narration + a 4 s break
    # Before the break: the narration sweep (f = 300 + 50 t). During: the clip's own 1500 Hz tone.
    before = dominant(out, at - 1.2, 0.8)
    during = dominant(out, at + 0.8, 2.4)
    after = dominant(out, at + 4.3, 0.8)
    assert abs(before - (300 + 50 * (at - 0.8))) < 70
    assert abs(during - 1500) < 40
    # After the break narration resumes at the same word, not 4 seconds further on.
    assert abs(after - (300 + 50 * (at + 0.7))) < 70
    assert abs(after - before) < 130  # a 4 s skip would add 200 Hz
    joined = " ".join(" ".join(str(v) for v in cmd) for cmd in calls)
    assert "loudnorm" in joined
    # No picture loops; the only -stream_loop allowed is the music bed's own (existing) loop.
    assert joined.count("-stream_loop") == (1 if with_music else 0)
    plan_text = (storage.DATA / "exports" / record["id"] / "episode-plan.md").read_text()
    assert "Audio breaks (original sound)" in plan_text
    # Sign-off never clears audio on your behalf.
    sign = c.post(url + "/signoff", json={"confirmed": True})
    assert sign.status_code == 200
    c.patch(url + "/episode/source/S03", json={"audio_cleared": False})
    assert c.post(url + "/signoff", json={"confirmed": True}).status_code == 200
    final = c.get(url).json()
    assert not final["episode"]["bindings"]["S03"].get("audio_cleared")


def test_uncleared_break_blocks_the_final_export_but_not_a_draft():
    p = project()
    link_clip(p)
    episode.build(p, True)
    report = editorial.inspect(p, check_files=False)
    waiting = [i for i in report["issues"] if i["code"] == "episode_audio_break_waiting"]
    assert waiting and waiting[0]["blocks_final"] and not waiting[0]["blocks_draft"]
    episode.bind_source(p, "S03", {"audio_cleared": True})
    episode.build(p, True)
    after = editorial.inspect(p, check_files=False)
    assert not [i for i in after["issues"] if i["code"].startswith("episode_audio_break")]
