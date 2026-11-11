"""Base-image fill: relevant, varied, reproducible cover for stretches with no clip.

A project can hold any number of real "base" images or clips of the victim,
the suspect and the crime scene. Any stretch of narration that has no matching
footage (a gap, or the tail of a clip shorter than its scene) is filled from
that pool instead of showing a gap card or looping the clip.

Naming (the only thing the user has to remember)::

    BASE-V--portrait--01.jpg      victim, tag "portrait"
    BASE-V--memorial+family--02.mp4
    BASE-S--court--01.jpg         suspect
    BASE-C--location--01.mp4      crime scene / location
    BASE-V-3.jpg                  untagged (bucket only) also works

The text after ``BASE-X`` is split on ``--``. A last segment that looks like a
plain counter (``01``, ``2``, ``a3``, ``07 (1)``) is just a unique id; every
other segment is a tag, and ``+`` joins several tags in one segment. The editor
stores every upload under its own internal id, so repeated names never collide.

Relevance comes from meaning: the editing guide may carry ``**Fill:** V / memorial``
on any card (bucket + optional tags). Randomness only ever happens among the
images that match. Hard safety rules always apply.
"""

from __future__ import annotations

import math
import random
import re

BUCKETS = {"V": "victim", "S": "suspect", "C": "scene"}
BUCKET_WORDS = {
    "v": "V",
    "victim": "V",
    "victims": "V",
    "s": "S",
    "suspect": "S",
    "suspects": "S",
    "defendant": "S",
    "accused": "S",
    "c": "C",
    "scene": "C",
    "crime-scene": "C",
    "crimescene": "C",
    "location": "C",
    "place": "C",
}

#: Standard tag list (free-form tags are allowed too). Aliases normalise to these.
STANDARD_TAGS = {
    "V": ["portrait", "family", "memorial", "daily-life"],
    "S": ["portrait", "court", "custody"],
    "C": ["location", "day", "night", "police"],
}
ALIASES = {
    "vigil": "memorial",
    "funeral": "memorial",
    "tribute": "memorial",
    "candles": "memorial",
    "balloons": "memorial",
    "courtroom": "court",
    "hearing": "court",
    "trial": "court",
    "sentencing": "court",
    "mugshot": "custody",
    "booking": "custody",
    "arrest": "custody",
    "jail": "custody",
    "scene": "location",
    "street": "location",
    "exterior": "location",
    "wide": "location",
    "tape": "police",
    "cruiser": "police",
    "officers": "police",
    "everyday": "daily-life",
    "life": "daily-life",
    "smile": "portrait",
    "smiling": "portrait",
    "photo": "portrait",
    "relatives": "family",
}

#: Lines that are about the victim's people / grief. A suspect image is never
#: placed under these unless the suspect is also named in a guide-approved hint.
GRIEF_WORDS = re.compile(
    r"\b(mother|father|mom|dad|parents?|grandfather|grandmother|grandparents?|"
    r"family|families|funeral|vigil|grief|grieving|mourn\w*|memorial|buried|"
    r"burial|loved ones|brother|sister|widow\w*|bereaved|tribute)\b",
    re.I,
)

IMAGE_EXT = (".jpg", ".jpeg", ".png", ".webp")
VIDEO_EXT = (".mp4", ".mov", ".webm", ".mkv")
MEDIA_EXT = IMAGE_EXT + VIDEO_EXT

DEFAULT_MAX_USES = 4
DEFAULT_SPACING = 90.0  # seconds before the same image may return
DEFAULT_TARGET = 6.0  # seconds per fill shot
DEFAULT_MAX_HOLD = 8.0
MOTIONS = ("slow-zoom", "slow-zoom-out", "pan-left", "pan-right")

LABEL_IMAGE = "Archive image, not footage of the narrated event"
LABEL_CLIP = "Archive clip, not footage of the narrated event"


# --------------------------------------------------------------------------
# Names, tags and hints
# --------------------------------------------------------------------------


def norm_tag(value):
    tag = re.sub(r"[\s_]+", "-", str(value).strip().lower()).strip("-")
    return ALIASES.get(tag, tag)


def _idlike(segment):
    if re.fullmatch(r"(?:19|20)\d{2}", segment.strip()):
        return False  # a year is a tag (e.g. 2024), not a counter
    return bool(
        re.fullmatch(r"[a-z]{0,2}\d+(?:\s*\(\d+\))?", segment.strip(), re.I)
        or re.fullmatch(r"copy(?:\s*\d+)?", segment.strip(), re.I)
    )


def parse_name(name):
    """Return {bucket, tags} for a BASE- filename, else None."""
    stem = str(name or "").strip()
    stem = re.sub(r"\.[A-Za-z0-9]{2,5}$", "", stem)
    m = re.match(r"^BASE-([VSC])(?=$|-)", stem, re.I)
    if not m:
        return None
    bucket = m.group(1).upper()
    rest = stem[m.end() :]
    if rest.startswith("--"):
        segments = [s.strip() for s in rest.split("--") if s.strip()]
    else:
        segments = [rest.strip("-").strip()] if rest.strip("-").strip() else []
    if not segments:
        return {"bucket": bucket, "tags": []}
    if len(segments) == 1:
        raw = [] if _idlike(segments[0]) else [segments[0]]
    else:
        raw = segments[:-1] + ([] if _idlike(segments[-1]) else [segments[-1]])
    tags = []
    for segment in raw:
        for part in segment.split("+"):
            tag = norm_tag(part)
            if tag and tag not in tags and not _idlike(tag):
                tags.append(tag)
    return {"bucket": bucket, "tags": tags}


def parse_hint(raw):
    """Parse ``V / memorial``, ``S: court``, ``S / court+2024 / !2026``.

    Returns {bucket|None, tags[], exclude[], raw} or None for no hint at all.
    ``!tag`` or ``not tag`` excludes images carrying that tag (for example a
    year that would break the chronology of the line).
    """
    text = str(raw or "").strip().strip("`*_ ")
    if not text or text.lower() in ("none", "n/a", "-"):
        return None
    bucket = None
    tags = []
    exclude = []
    skip = {"and", "or", "tag", "tags", "bucket", "image", "images", "base", "use", "the", "a", "auto"}
    negate = False
    for bang, token in re.findall(r"(!)?([a-z0-9]+(?:-[a-z0-9]+)*)", text.lower()):
        if token in ("not", "no", "except", "without"):
            negate = True
            continue
        if bucket is None and token in BUCKET_WORDS and not bang and not negate:
            bucket = BUCKET_WORDS[token]
            continue
        if token in skip:
            continue
        tag = norm_tag(token)
        if not tag or _idlike(tag):
            continue
        target = exclude if (bang or negate) else tags
        if tag not in target:
            target.append(tag)
        negate = False
    if bucket is None and not tags and not exclude:
        return None
    return {"bucket": bucket, "tags": tags, "exclude": exclude, "raw": text[:120]}


def parse_setup(raw, chapter_key):
    """Read the optional ``## Project setup`` block from the guide.

    Lines (any order, all optional)::

        - Case: <name>
        - Victim: <name>; <name>
        - Suspect: <name>; <name>
        - Avoid tags: residential, graphic
        - Avoid in CHAPTER 3: residential
    """
    match = re.search(
        r"^##\s+Project setup[^\n]*\n(.*?)(?=^##\s|\Z)", raw, re.M | re.S | re.I
    )
    setup = {
        "present": bool(match),
        "case": "",
        "victims": [],
        "suspects": [],
        "avoid_tags": [],
        "avoid_by_chapter": {},
    }
    if not match:
        return setup
    for line in match.group(1).splitlines():
        m = re.match(
            r"^\s*[-*]\s*\**\s*([A-Za-z][A-Za-z0-9 ]*?)\s*\**\s*:\s*\**\s*(.+?)\s*$", line
        )
        if not m:
            continue
        label, value = m.group(1).strip().lower(), m.group(2).strip().strip("*_ ")
        if label == "case":
            setup["case"] = value[:200]
        elif label in ("victim", "victims"):
            setup["victims"] = _names(value)
        elif label in ("suspect", "suspects", "defendant", "defendants"):
            setup["suspects"] = _names(value)
        elif label in ("avoid tags", "avoid tag", "avoid"):
            setup["avoid_tags"] = _tag_list(value)
        elif label.startswith("avoid in "):
            key = chapter_key(label[len("avoid in ") :].upper())
            setup["avoid_by_chapter"][key] = _tag_list(value)
    return setup


def _names(value):
    return [n.strip() for n in re.split(r"[;|]", value) if n.strip()][:12]


def _tag_list(value):
    tags = []
    for part in re.split(r"[,;/+]", value):
        tag = norm_tag(part)
        if tag and tag not in tags:
            tags.append(tag)
    return tags


def parse_base_files(raw):
    """Filenames of base images the guide asks the user to supply."""
    names = re.findall(
        r"BASE-[VSC][^\s|`\"'<>()\[\]]*?\.(?:jpe?g|png|webp|mp4|mov|webm|mkv)",
        raw,
        re.I,
    )
    return list(dict.fromkeys(names))


def _seconds(text):
    parts = [float(x) for x in text.split(":")]
    total = 0.0
    for part in parts:
        total = total * 60 + part
    return total


def parse_base_windows(raw):
    """Crop windows the guide gives for base clips, e.g. ``0:40–0:52`` on a table row.

    Returns {lowercase filename: (start, end)} for lines that name a BASE- video and a
    time range. The window only applies if the uploaded file is long enough to contain it
    (a clip you already trimmed is used whole).
    """
    windows = {}
    pattern = re.compile(
        r"(\d{1,2}:\d{2}(?::\d{2})?(?:\.\d+)?)\s*(?:–|—|-|to)\s*"
        r"(\d{1,2}:\d{2}(?::\d{2})?(?:\.\d+)?)"
    )
    for line in raw.splitlines():
        name = re.search(
            r"BASE-[VSC][^\s|`\"'<>()\[\]]*?\.(?:mp4|mov|webm|mkv)", line, re.I
        )
        if not name:
            continue
        rest = line[name.end() :]
        m = pattern.search(rest)
        if not m:
            continue
        a, b = _seconds(m.group(1)), _seconds(m.group(2))
        if b - a >= 1.0:
            windows.setdefault(name.group(0).lower(), (a, b))
    return windows


def name_parts(names):
    """Distinct matchable name words for narration checks (len >= 3)."""
    parts = []
    for name in names or []:
        for word in re.findall(r"[A-Za-z][A-Za-z'’-]{2,}", name):
            low = word.lower()
            if low not in parts and low not in ("jr", "sr", "the", "and"):
                parts.append(low)
    return parts


def mentions(text, parts):
    low = str(text or "").lower()
    return any(re.search(r"\b" + re.escape(p) + r"\b", low) for p in parts)


# --------------------------------------------------------------------------
# The pool
# --------------------------------------------------------------------------


def pool(project):
    """Usable base assets, each with bucket/tags/kind/duration."""
    skip = {project.get("narration_id"), project.get("music_id")}
    windows = ((project.get("episode") or {}).get("guide") or {}).get("base_windows") or {}
    items = []
    for asset in project.get("assets", []):
        if asset.get("kind") not in ("image", "video"):
            continue
        if asset.get("available_on_server") is False or asset.get("id") in skip:
            continue
        meta = parse_name(asset.get("name", ""))
        if not meta:
            continue
        duration = float(asset.get("video_duration") or asset.get("duration") or 0)
        if asset["kind"] == "video" and duration <= 0:
            continue
        window = None
        if asset["kind"] == "video":
            given = windows.get(str(asset.get("name", "")).lower())
            # Applies only when the uploaded file contains the whole window.
            if given and given[1] <= duration + 0.5:
                window = (given[0], min(given[1], duration))
        items.append(
            {
                "id": asset["id"],
                "name": asset.get("name", ""),
                "kind": asset["kind"],
                "duration": duration,
                "window": window,
                "bucket": meta["bucket"],
                "tags": meta["tags"],
            }
        )
    return items


def pool_warnings(items):
    """Findings about the pool itself (independent of any plan)."""
    findings = []
    long_clips = [
        i["name"]
        for i in items
        if i["kind"] == "video" and not i.get("window") and i["duration"] > 45
    ]
    if long_clips:
        shown = ", ".join(long_clips[:5]) + (" ..." if len(long_clips) > 5 else "")
        findings.append(
            {
                "code": "base_long_uncropped",
                "detail": (
                    f"{len(long_clips)} base clip(s) are over 45 seconds with no crop window, so any "
                    f"part of them may be used: {shown}. Trim them, or give a window in the guide's "
                    "Base clips table (for example 0:40–0:52)."
                ),
            }
        )
    return findings


def pool_counts(items):
    counts = {"V": 0, "S": 0, "C": 0}
    tags = {"V": {}, "S": {}, "C": {}}
    for item in items:
        counts[item["bucket"]] += 1
        for tag in item["tags"]:
            tags[item["bucket"]][tag] = tags[item["bucket"]].get(tag, 0) + 1
    return counts, tags


def enabled(project, items=None):
    e = project.get("episode") or {}
    if e.get("base_fill") is False:
        return False
    return bool(items if items is not None else pool(project))


# --------------------------------------------------------------------------
# Splitting a stretch into relevant shots
# --------------------------------------------------------------------------


def plan_segments(start, end, cuts, fps, target=DEFAULT_TARGET, max_hold=DEFAULT_MAX_HOLD):
    """Split frames [start, end) into shots of about ``target`` seconds.

    Cuts snap to narration phrase starts (``cuts`` in frames) when one is near,
    otherwise the stretch is split evenly. A stretch no longer than ``max_hold``
    is a single shot.
    """
    total = end - start
    if total <= 0:
        return []
    max_frames = int(round(max_hold * fps))
    if total <= max_frames:
        return [(start, end)]
    count = max(math.ceil(total / max_frames), int(round(total / (target * fps))))
    ideal = total / count
    tolerance = ideal * 0.35
    min_len = max(1, int(round(min(ideal * 0.6, 2.5 * fps))))
    points = [start]
    inner = sorted({c for c in cuts if start < c < end})
    for k in range(1, count):
        want = start + ideal * k
        window = [
            c
            for c in inner
            if abs(c - want) <= tolerance
            and c - points[-1] >= min_len
            and end - c >= min_len
        ]
        point = min(window, key=lambda c: abs(c - want)) if window else int(round(want))
        point = max(point, points[-1] + 1)
        points.append(min(point, end - 1))
    points.append(end)
    result = []
    for a, b in zip(points, points[1:]):
        if b <= a:
            continue
        # Snapping to a phrase start must never push a shot past the hold limit.
        pieces = max(1, math.ceil((b - a) / max_frames))
        edges = [a + round((b - a) * k / pieces) for k in range(pieces + 1)]
        result.extend((x, y) for x, y in zip(edges, edges[1:]) if y > x)
    return result


# --------------------------------------------------------------------------
# The picker
# --------------------------------------------------------------------------


class Planner:
    """Deterministic (seeded) relevance-first picker with variety rules."""

    def __init__(
        self,
        items,
        setup,
        seed=1,
        max_uses=DEFAULT_MAX_USES,
        spacing=DEFAULT_SPACING,
        chapter_key=None,
        label=True,
    ):
        self.items = items
        self.setup = setup or {}
        self.rng = random.Random(int(seed))
        self.max_uses = max_uses
        self.spacing = spacing
        self.label = label
        self.uses = {i["id"]: 0 for i in items}
        self.last_end = {}
        self.last_asset = None
        self.last_motion = None
        self.asset_motion = {}
        self.neutral_next = "C"
        self.victim_parts = name_parts(self.setup.get("victims"))
        self.suspect_parts = name_parts(self.setup.get("suspects"))
        self.log = []
        self.unfilled = []

    # -- bucket decision --------------------------------------------------
    def decide(self, text, hint):
        notes = []
        about_suspect = mentions(text, self.suspect_parts)
        about_victim = mentions(text, self.victim_parts)
        grief = bool(GRIEF_WORDS.search(text or ""))
        want = (hint or {}).get("bucket")
        if want == "S" and grief and not about_suspect:
            want = "V"
            notes.append("safety: suspect image not placed under a victim/family line")
        if want is None:
            if about_suspect and not grief and not about_victim:
                want = "S"
            elif about_suspect and (grief or about_victim):
                want = "V"
                notes.append("line names both; victim image chosen")
            elif about_victim or grief:
                want = "V"
            else:
                want = self.neutral_next
                self.neutral_next = "V" if want == "C" else "C"
        order = {"V": ["V", "C"], "C": ["C", "V"], "S": ["S", "C"]}[want]
        return want, order, notes

    # -- candidates -------------------------------------------------------
    def _avoided(self, item, chapter):
        avoid = set(self.setup.get("avoid_tags") or [])
        avoid |= set((self.setup.get("avoid_by_chapter") or {}).get(chapter, []))
        return bool(avoid & set(item["tags"]))

    def _eligible(self, item, duration, chapter, excluded=()):
        if self._avoided(item, chapter):
            return False
        if excluded and set(excluded) & set(item["tags"]):
            return False
        if item["kind"] == "video":
            window = item.get("window")
            available = (window[1] - window[0]) if window else item["duration"]
            if available + 1e-6 < duration:
                return False
        return True

    def _choose(
        self, candidates, t_start, strict_uses, strict_spacing, allow_consecutive=False
    ):
        pool_ = []
        for item in candidates:
            if strict_uses and self.uses[item["id"]] >= self.max_uses:
                continue
            if strict_spacing and (
                item["id"] in self.last_end
                and t_start - self.last_end[item["id"]] < self.spacing
            ):
                continue
            if (
                not strict_spacing
                and not allow_consecutive
                and item["id"] == self.last_asset
            ):
                continue
            pool_.append(item)
        if not pool_:
            return None
        least = min(self.uses[i["id"]] for i in pool_)
        group = [i for i in pool_ if self.uses[i["id"]] == least]
        oldest = min(self.last_end.get(i["id"], -1e9) for i in group)
        group = [i for i in group if self.last_end.get(i["id"], -1e9) == oldest] or group
        return self.rng.choice(sorted(group, key=lambda i: i["id"]))

    def choose(
        self, text, hint, chapter, t_start, duration, reason="gap", cue_id=None
    ):
        """Pick a base asset for one shot. Returns a dict or None (unfilled)."""
        want, order, notes = self.decide(text, hint)
        want_tags = (hint or {}).get("tags") or []
        excluded = (hint or {}).get("exclude") or []
        tiers = []
        for bucket in order:
            in_bucket = [
                i
                for i in self.items
                if i["bucket"] == bucket
                and self._eligible(i, duration, chapter, excluded)
            ]
            if len(want_tags) > 1:
                every = [i for i in in_bucket if set(want_tags) <= set(i["tags"])]
                tiers.append((bucket, "tag-match", every))
            if want_tags:
                tagged = [i for i in in_bucket if set(i["tags"]) & set(want_tags)]
                tiers.append((bucket, "tag-match", tagged))
            tiers.append((bucket, "bucket", in_bucket))
        picked, tier_name, relaxed = None, "", []
        passes = (
            (True, True, False, ""),
            (True, False, False, "repeat sooner than the spacing rule"),
            (False, False, False, "image used more than the per-image limit"),
            (False, False, True, "same image twice in a row and past its limit (pool too small)"),
        )
        # Relevance first: a scarce tagged image may come back sooner than the
        # spacing rule before an image of the wrong topic is used; it never
        # exceeds the per-image limit.
        for bucket, tier, candidates in tiers:
            if not candidates:
                continue
            for strict_uses, strict_spacing, consecutive, note in (
                passes[:2] if tier == "tag-match" else passes
            ):
                picked = self._choose(
                    candidates, t_start, strict_uses, strict_spacing, consecutive
                )
                if picked:
                    tier_name = (
                        tier if bucket == order[0] else f"fallback-{BUCKETS[bucket]}"
                    )
                    if want_tags and tier == "bucket" and bucket == order[0]:
                        notes.append("no image with the requested tag; any in bucket used")
                    if note:
                        relaxed.append(note)
                    break
            if picked:
                break
        entry = {
            "start": round(t_start, 3),
            "duration": round(duration, 3),
            "want": want,
            "hint": (hint or {}).get("raw", ""),
            "chapter": chapter,
            "reason": reason,
            "cue": cue_id,
        }
        if not picked:
            entry["unfilled"] = True
            self.unfilled.append(entry)
            self.log.append(entry)
            return None
        self.uses[picked["id"]] += 1
        self.last_end[picked["id"]] = t_start + duration
        self.last_asset = picked["id"]
        motion = self._motion(picked)
        trim = 0.0
        crop_end = None
        if picked["kind"] == "video":
            window = picked.get("window")
            base = window[0] if window else 0.0
            span = (window[1] - window[0]) if window else picked["duration"]
            room = max(0.0, span - duration)
            offset = round(self.rng.uniform(0, room), 1) if room > 0.1 else 0.0
            trim = base + min(offset, room)
            crop_end = trim + duration
            motion = "none"
        entry.update(
            bucket=picked["bucket"],
            asset_id=picked["id"],
            asset_name=picked["name"],
            tags=picked["tags"],
            tier=tier_name,
            motion=motion,
            relaxed=relaxed,
            notes=notes,
        )
        self.log.append(entry)
        label = ""
        if self.label:
            label = LABEL_CLIP if picked["kind"] == "video" else LABEL_IMAGE
        return {
            "asset_id": picked["id"],
            "kind": picked["kind"],
            "trim": trim,
            "source_crop_end": crop_end,
            "motion": motion,
            "label": label,
            "meta": {
                "bucket": picked["bucket"],
                "tags": picked["tags"],
                "asset_name": picked["name"],
                "tier": tier_name,
                "hint": (hint or {}).get("raw", ""),
                "notes": notes + relaxed,
            },
        }

    def _motion(self, item):
        tags = set(item["tags"])
        if "portrait" in tags:
            prefer = ["slow-zoom", "slow-zoom-out"]
        elif "memorial" in tags:
            prefer = ["slow-zoom-out", "slow-zoom"]
        elif tags & {"location", "day", "night", "police"} or item["bucket"] == "C":
            prefer = ["pan-left", "pan-right", "slow-zoom"]
        else:
            prefer = list(MOTIONS)
        history = self.asset_motion.setdefault(item["id"], [])
        for motion in prefer + [m for m in MOTIONS if m not in prefer]:
            if motion != self.last_motion and motion not in history:
                break
        else:
            motion = next(m for m in prefer if m != self.last_motion)
        history.append(motion)
        self.last_motion = motion
        return motion

    # -- summary ----------------------------------------------------------
    def summary(self, seed):
        placed = [e for e in self.log if not e.get("unfilled")]
        by_bucket = {"V": 0, "S": 0, "C": 0}
        by_tag = {}
        for e in placed:
            by_bucket[e["bucket"]] += 1
        for e in self.log:
            for tag in (parse_hint(e.get("hint")) or {}).get("tags", []):
                by_tag.setdefault(e["want"], {}).setdefault(tag, 0)
                by_tag[e["want"]][tag] += 1
        counts, tag_counts = pool_counts(self.items)
        return {
            "enabled": True,
            "seed": int(seed),
            "fills": len(placed),
            "seconds": round(sum(e["duration"] for e in placed), 2),
            "unfilled": len(self.unfilled),
            "unfilled_seconds": round(sum(e["duration"] for e in self.unfilled), 2),
            "by_bucket": by_bucket,
            "requested_by_tag": by_tag,
            "pool": counts,
            "pool_tags": tag_counts,
            "max_uses": self.max_uses,
            "spacing": self.spacing,
            "repeat_sooner": sum(
                any("spacing" in r for r in e.get("relaxed", [])) for e in placed
            ),
            "over_limit": sum(
                any("limit" in r for r in e.get("relaxed", [])) for e in placed
            ),
            "back_to_back": sum(
                any("twice in a row" in r for r in e.get("relaxed", [])) for e in placed
            ),
            "overrides": sum(
                any(n.startswith("safety") for n in e.get("notes", [])) for e in placed
            ),
            "tag_fallbacks": sum(
                any("requested tag" in n for n in e.get("notes", [])) for e in placed
            ),
            "max_uses_seen": max(self.uses.values(), default=0),
            "missing_clips": sorted(
                {e["cue"] for e in placed if e.get("reason") == "missing-clip" and e.get("cue")}
            ),
            "reasons": {
                r: sum(1 for e in placed if e.get("reason") == r)
                for r in ("gap", "fill-card", "missing-clip", "clip-tail")
            },
            "log": self.log[:600],
        }


# --------------------------------------------------------------------------
# Readiness
# --------------------------------------------------------------------------


def readiness(summary, setup=None, guide_base_files=None, uploaded_names=None):
    """Plain-language findings about the pool for the current plan."""
    findings = []
    if not summary:
        return findings
    need_each = summary.get("max_uses", DEFAULT_MAX_USES)
    pool_counts_ = summary.get("pool", {})
    for bucket, fills in summary.get("by_bucket", {}).items():
        if not fills:
            continue
        need = math.ceil(fills / need_each)
        have = pool_counts_.get(bucket, 0)
        if have < need:
            findings.append(
                {
                    "code": "base_pool_small",
                    "detail": (
                        f"{BUCKETS[bucket].capitalize()} base images: {have} uploaded, "
                        f"about {need} needed ({fills} fills, each image used at most "
                        f"{need_each} times). Add {need - have} more named BASE-{bucket}-..."
                    ),
                }
            )
    for bucket, tags in summary.get("requested_by_tag", {}).items():
        for tag, wanted in tags.items():
            need = math.ceil(wanted / need_each)
            have = summary.get("pool_tags", {}).get(bucket, {}).get(tag, 0)
            if have < min(need, 2):
                findings.append(
                    {
                        "code": "base_tag_small",
                        "detail": (
                            f"Guide asks for {BUCKETS.get(bucket, bucket)} '{tag}' images "
                            f"{wanted} time(s) but only {have} uploaded. "
                            f"Add BASE-{bucket}--{tag}--01.jpg style files."
                        ),
                    }
                )
    if summary.get("missing_clips"):
        shown = ", ".join(summary["missing_clips"][:10]) + (
            " ..." if len(summary["missing_clips"]) > 10 else ""
        )
        findings.append(
            {
                "code": "base_missing_clips",
                "detail": (
                    f"{len(summary['missing_clips'])} guide placement(s) have no usable "
                    f"clip yet, so base images stand in for them: {shown}. Upload or "
                    "approve those clips to replace the stand-ins."
                ),
            }
        )
    if summary.get("unfilled"):
        findings.append(
            {
                "code": "base_unfilled",
                "detail": (
                    f"{summary['unfilled_seconds']:.1f} seconds could not be filled "
                    "(no usable base image for that bucket). Marked gap cards remain."
                ),
            }
        )
    if summary.get("repeat_sooner"):
        findings.append(
            {
                "code": "base_repeats",
                "detail": (
                    f"{summary['repeat_sooner']} fill(s) repeat an image sooner than "
                    f"{int(summary['spacing'])} seconds because the pool is small."
                ),
            }
        )
    if summary.get("back_to_back"):
        findings.append(
            {
                "code": "base_back_to_back",
                "detail": f"{summary['back_to_back']} fill(s) show the same image twice in a row because the pool is too small; add more base images.",
            }
        )
    if summary.get("over_limit"):
        findings.append(
            {
                "code": "base_overused",
                "detail": f"{summary['over_limit']} fill(s) reuse an image beyond its limit; add more base images.",
            }
        )
    if summary.get("tag_fallbacks"):
        findings.append(
            {
                "code": "base_tag_fallback",
                "detail": f"{summary['tag_fallbacks']} fill(s) used any image in the bucket because none had the requested tag.",
            }
        )
    if guide_base_files is not None and uploaded_names is not None:
        have = {n.lower() for n in uploaded_names}
        missing = [n for n in guide_base_files if n.lower() not in have]
        if missing:
            shown = ", ".join(missing[:8]) + (" ..." if len(missing) > 8 else "")
            findings.append(
                {
                    "code": "base_files_missing",
                    "detail": f"The guide lists {len(missing)} base file(s) not uploaded yet: {shown}",
                }
            )
    if setup is not None and summary.get("fills") and not setup.get("present"):
        findings.append(
            {
                "code": "base_setup_missing",
                "detail": "The guide has no Project setup block, so names are not known; bucket choice relies on the guide's Fill hints only.",
            }
        )
    return findings
