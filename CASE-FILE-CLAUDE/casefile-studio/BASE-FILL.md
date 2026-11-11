# Base-image fill

A small pool of real pictures and clips of the **victim**, the **suspect** and the **crime scene** that the
editor uses, automatically, for any stretch of narration that has no matching clip. It replaces both
"VISUAL NEEDED" gap cards and looping a short clip.

## What it covers

1. **Gaps**: narration with no guide card, or a card whose clip is missing or not approved yet.
2. **Fill-only cards**: guide cards that say up front "no footage exists for this moment".
3. **Clip tails**: an approved clip shorter than its scene plays **once**, then a base image takes over
   (the old behaviour looped the clip).

Nothing changes for a project with no `BASE-` files.

## Naming the files

Start the filename with `BASE-` + a bucket letter, then optional tags, then anything unique:

| File | Bucket | Tags |
|---|---|---|
| `BASE-V--portrait--01.jpg` | victim | portrait |
| `BASE-V--memorial+family--02.mp4` | victim | memorial, family |
| `BASE-S--court--01.jpg` | suspect | court |
| `BASE-C--location--01.mp4` | crime scene / location | location |
| `BASE-V-3.jpg` | victim | none |

* `V` victim · `S` suspect · `C` crime scene / location.
* Segments are separated by `--`; join several tags with `+`. A final segment that is only a counter
  (`01`, `7`, `a3`, `07 (1)`) is just a unique id.
* **Any number of files per bucket and tag.** The editor stores every upload under its own internal id,
  so repeated numbering never causes a clash.
* Upload them with the rest of the footage (the normal media upload).

Standard tags: victim `portrait · family · memorial · daily-life`; suspect `portrait · court · custody`;
scene `location · day · night · police`. Other tags are allowed. Aliases are normalised
(`vigil`, `funeral`, `tribute` → `memorial`; `courtroom`, `hearing` → `court`; `mugshot`, `booking` → `custody`; `street`, `exterior` → `location`).

## Images and clips

Base files can be **photos or video clips**. A base clip plays once, muted, from a random start point,
for the length of the shot (never looped), and is only chosen if it is long enough. To keep it on the
right part of a long video, give a crop window in the guide's **Base clips** table, for example
`news report, 0:40–0:52`; the editor then starts only inside that window. A clip you already trimmed
before uploading is used whole (a window that the file is too short to contain is ignored). Base clips
over 45 seconds with no window are flagged, because any part of them could be used.

## What the guide carries

```
## Project setup
- Case: <name>
- Victim: <name>; <name>
- Suspect: <name>
- Avoid tags: graphic
- Avoid in CHAPTER 3: residential
```

Case, victim and suspect names come from the script/research (the Name Register). The editor reads this
block itself; nothing is typed in the app and nothing carries over between projects.

Any card may add a hint: `**Fill:** V / memorial` (bucket, then optional tags). A card with **no clip**
needs no Source ID: a `Fill:` hint (or `Source ID: BASE`) makes it a fill-only card.

A `## Base clips` table and a `## File checklist` list each file with **Save as**, what it shows, where
to get it and its tag. The editor compares that list with what you uploaded and tells you what is missing.
See `examples/base-fill/` for a complete example.

## How an image is chosen

1. **Bucket**: from the card's `Fill:` hint. With no hint: the suspect bucket is used only when the
   narration at that moment names the suspect; victim lines (victim name, family, funeral, vigil, ...) use
   the victim bucket; everything else alternates between scene and victim.
2. **Relevance first**: images with the requested tag are tried before any other image in the bucket.
3. **Variety**: least-used image first, chosen at random (seeded) among equals; the same image does not
   return within 90 s and is never used more than 4 times while others are available; a scarce tagged
   image may return sooner (never back-to-back) before an off-topic one is used.
4. **Never a gap if anything fits**: if the pool is too small, the repeat is reported, not hidden.
5. **Shots** are about 6 s (max 8 s), cut on narration phrase starts. A base video is only chosen if it
   is long enough, and it plays from a random point without looping.
6. **Motion** (stills): portraits slow zoom-in, memorial moments zoom-out, locations pan left/right;
   direction varies on every reuse and never repeats back-to-back.

### Hard safety rules

* A suspect image is never placed under a victim/family/grief line (a guide `S` hint is overridden
  there and the override is listed in the report).
* Tags in `Avoid tags` / `Avoid in CHAPTER n` are never used.
* A card that needs an explicit visual stop keeps its marked gap after the stop unless it also has a
  `Fill:` hint.
* Fills are labelled on screen "Archive image, not footage of the narrated event" (switch off with
  `base_label: false`; the plan report still marks them).

## In the app

The episode screen has a **Base images** panel (below the editing brief): how many Victim / Suspect /
Scene images are uploaded and with which tags, the names read from the guide, an on/off switch, the
archive-label switch, the longest base shot (5 to 12 s), a **Reshuffle** button, a summary of the current
plan's fills, and the readiness messages (what to add, which guide files are missing, which placements
are standing in for missing clips).

## Dates and chronology

Tags can be years, so a line about a 2024 hearing is never covered by 2026 footage:

* name the files `BASE-S--court+2024--01.jpg`, `BASE-S--court+2026--02.jpg`;
* hint `**Fill:** S / court+2024 / !2026` (also `not 2026` or `except 2026`). `!tag` excludes every image
  carrying that tag, even when nothing else fits (a scene or victim image is used instead).

When a hint lists several tags, images carrying all of them are tried first, then any one of them.

## Relation to the loop rule

Before this feature, a short clip looped inside its scene (the guide loop rule). With base images
uploaded, the clip plays once and a base image covers the rest. Switch **Cover gaps and clip tails with
base images** off (or upload no `BASE-` files) to get the old looping and marked gap cards exactly as
before. A guide whose own text states the old loop rule should be written without it when you use base
images, because the guide text is authoritative.

## Sign-off

The one explicit **producer sign-off** click also records the standard bulk-responsibility note on every
uploaded `BASE-` file, as it does for linked guide files. It verifies nothing; the note says so.

## Settings (episode options, API `PATCH /api/projects/{id}/episode/options`)

| Option | Effect |
|---|---|
| `{"reshuffle": true}` | new random order (same pool); rebuilds the plan |
| `{"base_seed": 7}` | choose the shuffle explicitly (same seed = identical plan) |
| `{"base_fill": false}` | switch base fill off (gaps return as marked cards) |
| `{"base_hold": 6}` | longest base shot, 3 to 12 s (default 8) |
| `{"base_label": false}` | hide the on-screen archive label |

Reports: `GET /api/projects/{id}/episode/base-report` (pool, findings) and the **Base-image fills**
table in `plan.md` (every fill: time, image, why, notes).

## Readiness messages

After each build the Issues list says, for example, "Victim base images: 3 uploaded, about 9 needed",
"memorial: only 1 image", "N fills repeat an image sooner than 90 seconds", "N guide placements have no
usable clip yet, so base images stand in", and "the guide lists base files not uploaded yet".

## Limits

* The scene limit stays 400. When fills would exceed it the editor lengthens base shots (up to 14 s).
* A guide may hold 300 footage cards plus 300 fill-only cards.
* Base files still need a recorded reuse basis like any other file (sign-off records the standard note); they are archive visuals, not evidence.
* Relevance is only as good as the tags and hints; untagged files are used for the whole bucket.
