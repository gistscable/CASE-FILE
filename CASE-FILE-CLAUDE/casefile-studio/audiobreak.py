"""Mode O: original-audio breaks.

A guide card may carry ``**Audio break:** 0:20–0:32``, a window inside that card's
source file (2 to 30 seconds). At the card's ``At:`` phrase the narration pauses, the
clip plays with its own sound and picture, then the narration resumes at the same
word. Everything after the break moves later by the break's length; the narration
itself is never edited.

The break only happens when the producer has explicitly confirmed, for that source
file, that they may play its original audio (``audio_cleared``). Nothing sets that
flag silently, and producer sign-off does not touch it.
"""

import re

MIN_SECONDS = 2.0
MAX_SECONDS = 30.0
RECOMMENDED_MAX_BREAKS = 8
RECOMMENDED_GAP = 120.0  # seconds of narration between breaks

_TIME = r"(?:\d{1,2}:)?\d{1,3}:\d{2}(?:\.\d+)?|\d+(?:\.\d+)?s"


def _seconds(token):
    token = token.lower()
    if token.endswith("s"):
        return float(token[:-1])
    total = 0.0
    for part in token.split(":"):
        total = total * 60 + float(part)
    return total


def parse(text):
    """Return {"in", "out"} for a window like ``0:20–0:32``; None when empty."""
    text = str(text or "").strip().strip("`*_ ")
    if not text or text.lower() in ("none", "no", "n/a", "-"):
        return None
    m = re.search(rf"({_TIME})\s*(?:–|—|-|to)\s*({_TIME})", text, re.I)
    if not m:
        raise ValueError(
            "an audio break needs a time range inside the source file, for example 0:20–0:32."
        )
    start, end = _seconds(m.group(1)), _seconds(m.group(2))
    if not MIN_SECONDS <= end - start <= MAX_SECONDS:
        raise ValueError(
            f"an audio break must be {MIN_SECONDS:g} to {MAX_SECONDS:g} seconds long."
        )
    return {"in": start, "out": end}


def window_error(asset, brk):
    """Why this file cannot play the break, or None when it can."""
    if not asset or asset.get("kind") != "video":
        return "The break needs a linked video file."
    if not asset.get("has_audio"):
        return "The linked file has no audio track."
    duration = float(asset.get("video_duration") or asset.get("duration") or 0)
    if duration and brk["out"] > duration + 0.05:
        return "The break window runs past the end of the linked file."
    return None


def notes(breaks):
    """Plain-language guidance about count and spacing (never blocking)."""
    found = []
    if len(breaks) > RECOMMENDED_MAX_BREAKS:
        found.append(
            f"{len(breaks)} audio breaks; about {RECOMMENDED_MAX_BREAKS} is the usual maximum for one video."
        )
    ordered = sorted(breaks, key=lambda b: b["at"])
    for a, b in zip(ordered, ordered[1:]):
        if b["at"] - a["at"] < RECOMMENDED_GAP:
            found.append(
                f"{a['cue']} and {b['cue']} are only {b['at'] - a['at']:.0f} s of narration apart; about one break every 3 to 4 minutes works best."
            )
    return found
