# Agent handoff — Casefile Studio

State as of 2026-11-08 (v0.4.18). Read this before working in the repo.

## What this is

Casefile Studio: a documentary production tool. FastAPI backend
(`casefile-studio/app.py` + `episode.py`, `editorial.py`, `storage.py`),
React frontend (`casefile-studio/web/`, built bundle committed in
`web/assets/`). Version **0.4.18** (bump in `app.py`, `package.json`, and
both `?v=` refs in `web/index.html` together).

## Running it

```bash
cd casefile-studio
# ffmpeg must be on PATH. In a fresh sandbox, fetch it once:
#   pip download ffmpeg-binaries==1.1.0 --no-deps  (unpack into a dir on PATH)
.venv/bin/python -m uvicorn app:app --host 0.0.0.0 --port 8000
```

Hosted on Render: `render.yaml` at the repo root builds
`casefile-studio/Dockerfile` with a persistent disk at `/var/data`
(`CASEFILE_DATA_DIR`). See `casefile-studio/RENDER-DEPLOY.md`. Do not run more
than one uvicorn worker — jobs and AI sessions are in-process state.

Tests (346 passing at v0.4.18, including `tests/test_deployment.py`, which reads
`render.yaml` from the repo root; browser/long-render ones are slow-path):

```bash
PATH=<ffmpeg-dir>:$PATH .venv/bin/python -m pytest tests/ -q \
  --ignore=tests/browser_episode.py --ignore=tests/browser_production.py \
  --ignore=tests/browser_smoke.py --ignore=tests/long_render_check.py
```

Frontend rebuild after editing `web/src/`: `npm install && npm run build`
inside `casefile-studio/`, then restart the server. Browsers cache the
bundle — version bumps exist so a plain refresh picks it up.

## Hosting

The app deploys to Render as a Docker service: `casefile-studio/Dockerfile`
+ `casefile-studio/docker-entrypoint.sh` + `render.yaml` (repo root) +
`casefile-studio/RENDER-DEPLOY.md`. Deploy via Render's Blueprint flow
(New → Blueprint), not a hand-made Web Service. The storage root is
relocatable via `CASEFILE_DATA_DIR` (`storage.resolve_asset`); the
entrypoint seeds a fresh data volume from the image on first boot.
Optional HTTP basic auth via `BASIC_AUTH_USER` / `BASIC_AUTH_PASSWORD`
env vars (`tests/test_basicauth.py`) — off unless both are set; the app
has no login of its own, so keep it on for any public URL.

## Data conventions

The storage root is `CASEFILE_DATA_DIR` if set, otherwise `casefile-studio/data`
(`storage.DATA`). Render points it at the mounted disk. Asset paths are stored
relative to the code root when inside it, absolute when on the disk; resolve
them with `storage.resolve_asset` / `renderer.asset_path`, never
`ROOT / path`.

- `data/projects/*.json` — project state, **committed**.
- `data/exports/<id>/` — rendered outputs, **committed** (each ~90 MB MP4;
  keep individual files under GitHub's 100 MB limit).
- `data/media/<project-id>/` — uploaded source files, **not in git**
  (ignored). Originals live on the producer's Mac. A fresh clone cannot
  re-render without re-uploading media.
- `data/jobs/` — render job records, committed.
- `data/browser-sessions/`, `data/recovery-backups/` — ignored, transient.

## Current project state

| Project | id | State |
|---|---|---|
| **Bismilah** | `1a5bbba59d244274` | Producer-signed-off, reviewed plan, **final (no-banner) 480p export done**: `data/exports/1a938f1e9bf64f99/` |
| Tampa… | `4791316c6fae4722` | earlier project |
| Blackwater (demo) | `1b06752858c94e67` | demo |

Also in the repo root: `Bismilah-unreviewed-inspection.mp4` — the same
episode as an inspection draft **with** the burned-in disclosure banner
(pending the producer's confirmation to delete). Git tag `NyRA-Backup` +
GitHub Release of the same name = pre-sign-off backup point.

History note: the original Bismilah entry (`8e7a2f9d34074b1b`) was
deleted by a "clear session" action; `1a5bbba59d244274` (the former NyRA
Backup copy) is the live project and was repaired to point at its own
media copies. Do not resurrect the old id.

## Behavior rules that matter

- **Guide loop rule #8** (`episode.guide.raw` is authoritative over docs):
  gap scenes inherit the cue's selected crop and loop it to fill the
  scene — own beginning, final repetition trimmed, picture only, no
  substitutions/speed/freeze/spill. Never remove this. **Exception (v0.4.17):**
  when the project has `BASE-` files and base fill is on, the clip plays once and
  a relevant base image covers the rest instead of looping (producer request).
  With no `BASE-` files, or the switch off, the loop rule applies exactly as
  before (`tests/test_basefill.py::test_no_base_files_leaves_the_plan_unchanged`).
- **Producer sign-off**: `POST /api/projects/{id}/signoff {"confirmed":true}`
  marks sources reviewed, notes reuse responsibility, approves placements,
  rebuilds the reviewed plan, confirms digests, ticks attestations, covers
  a sub-0.25 s lead-in, and records the same standard reuse note on every
  uploaded `BASE-` file. It is the producer's explicit click — never flip
  these flags silently server-side. Tests: `tests/test_signoff.py`.
- **Inspection banner**: drafts (`draft:true`) and inspection-mode plans
  always burn it in. Only a reviewed plan + attestations + preflight-clean
  final render omits it. Never bypass the banner for unreviewed content.
- **"Clear session"** (`DELETE /api/projects/{id}/session`) deletes the
  project, its media, and its exports from the server. It is destructive;
  the producer has been burned by it once.

## Base-image fill (v0.4.17)

A pool of real `BASE-V/S/C--tag--n` images/clips (victim / suspect / scene)
covers narration that has no matching clip: gaps, fill-only guide cards, and the
tail of a clip shorter than its scene. Full description: `casefile-studio/BASE-FILL.md`
(example guide in `casefile-studio/examples/base-fill/`).

- Code: `basefill.py` (naming, hints, Project setup, seeded relevance picker,
  shot splitting, readiness); `episode.build()` calls it (`push_span`);
  `episode.parse_guide()` reads `**Fill:**`, fill-only cards (no Source ID needed),
  `## Project setup`, and the BASE- file list; `renderer.py` adds `slow-zoom-out`
  and `pan-right`; `app.py` adds options `base_fill/base_seed/reshuffle/base_hold/
  base_label` and `GET /episode/base-report`.
- Behavior: relevance first (hint tags, year tags, `!exclude`), then variety (least
  used, 90 s spacing, max 4 uses, never back-to-back); suspect images never under
  victim/family lines; scene limit 400 kept by lengthening base shots; scenes carry
  a `base_fill` marker and the label "Archive image, not footage of the narrated
  event". `issues()` skips base-fill scenes in guide-source checks.
- UI: `web/src/BaseImages.jsx` (mounted in `EpisodeSetup.jsx` above the plan result).
- Tests: `tests/test_basefill.py` (65).

## Audio breaks, Mode O (v0.4.18)

The narration can pause while a clip plays with its **own sound**, then resume at the same word. Source
audio is otherwise still always muted. Full description: `casefile-studio/AUDIO-BREAKS.md`.

- Guide: card field `**Audio break:** 0:20–0:32` (2–30 s window inside the card's source file); parsed in
  `episode.parse_guide` via `audiobreak.parse`.
- Clearance: binding flag `audio_cleared`, set only by the explicit per-source tick (`bind_source`); it needs
  `rights_confirmed` and an audio track, resets when the file or notes change, and **sign-off never sets it**.
- `episode.build()` pushes an insert scene (`insert_audio: True`, no narration, `audio_start` = narration
  position) before the cue's first scene via `push_insert`; uncleared/invalid breaks go to
  `plan["audio_breaks_skipped"]`. Insert scenes are excluded from the cue-crop (loop/tail) map, sign-off windows,
  and the generic scene-vs-cue checks; `issues()` validates them separately and its narration-continuity check
  skips them (the narration cursor ignores inserts). `plan["duration"]` stays the narration length;
  `plan["total_duration"]` adds `insert_seconds`.
- Renderer: for guide projects with inserts the voice track is rebuilt as narration slices + the clip's audio
  (loudnorm + fades) concatenated in scene order; without inserts the continuous-voice path is unchanged.
- UI: tick on the source row (`SourceRow`) and a summary line in the plan result. Tests: `tests/test_audiobreak.py` (27).

## Frontend anchors (web/src/main.jsx)

`api()` ~line 172; `acceptProject()` ~line 394; Review & export tab:
sign-off button + confirm modal in the Editorial review card; "Make final
video" button in the page header (opens ExportModal with the draft toggle
off; 480p/720p/1080p choice). ExportModal ~line 4842.
