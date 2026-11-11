# Change list: base-image fill (v0.4.17) and audio breaks / Mode O (v0.4.18), built on v0.4.16

New
- `audiobreak.py`, `AUDIO-BREAKS.md`, `tests/test_audiobreak.py` (27): Mode O audio breaks (see AUDIO-BREAKS.md).
- `basefill.py`: BASE- filename parsing (bucket, tags, year tags), base-clip crop windows, fill hints with exclusions (`!2026`), Project setup parsing, relevance-first seeded picker, shot splitting, readiness findings.
- `web/src/BaseImages.jsx`: the **Base images** panel on the episode screen (pool counts and tags, on/off, label, longest shot, Reshuffle, plan summary, findings).
- `BASE-FILL.md` (how to use), `examples/base-fill/` (example script and guide), `tests/test_basefill.py` (65 tests).

Changed
- `episode.py`: guide parser reads `**Fill:**`, fill-only cards (no Source ID needed), `## Project setup`, and the BASE- file list; `build()` fills gaps and clip tails from the pool instead of gap cards or loops, stays inside the 400-scene limit, records a fill summary; issues, plan report and input digest updated.
- `app.py`: version 0.4.17; scene sanitiser keeps the new motions and the fill marker; episode options `base_fill`, `base_seed`, `reshuffle`, `base_hold`, `base_label`; `GET /episode/base-report`; sign-off records the standard reuse note on BASE- files and ignores fill-only cards and base scenes.
- `renderer.py`: new motions `slow-zoom-out` and `pan-right`.
- `web/src/EpisodeSetup.jsx`, `web/src/episode.css`: mount the panel and style it. Rebuilt `web/assets/app.js` / `app.css`; `web/index.html` and `package.json` bumped to 0.4.17 so browsers load the new bundle.
- `README.md`: pointers. `EPISODE-WORKFLOW.md`: audio rule updated. Mode O also touches `episode.py` (parse, bind_source `audio_cleared`, build inserts, checks, plan report), `app.py` (sanitiser, sign-off windows), `renderer.py` (segmented voice track) and the source row/plan summary in `EpisodeSetup.jsx`; version 0.4.18.

Behaviour to know
- With no `BASE-` files, or with the switch off, behaviour is exactly as before (including looping short clips).
- With base images, a short clip plays once and a base image covers the rest. This replaces the loop for that case only.

Verification
- 346 tests pass (242 original + 12 deployment + 65 base-fill + 27 audio-break). The panel was server-rendered in Node for three states (no guide, empty pool, pool with a plan). Browser tests (`browser_*.py`) and the long render check were not run here.
