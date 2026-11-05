# ONE-TIME PROMPT — Casefile Studio + CapCut (Agent-Proof, No-Lazy Version)
*Use verbatim. Attach: Narration.md + corrected SRT + corrected JSON + 1x Casefile example guide + 1x CapCut example guide + optional YouTube links.*

I am attaching my narration, the **corrected SRT and JSON**, and two example editing guides: one for **Casefile Studio** and one for **CapCut**. Create two new Markdown guides for the new narration, using the attached guides as **format and workflow templates only**. Do not carry over their case names, footage, scene counts, insert counts, timing, FPS or other case-specific details. The 104-placement and 44-placement examples are **structure only** — do not copy their number of scenes.

**Sources (Anti-Lazy Rule):**
- Use only YouTube sources. Prefer real, case-related footage/reporting. Do not use non-YouTube, generic stock, reenactments, or unrelated material as case footage.
- **YouTube links I paste are RESEARCH HINTS ONLY** — they help you find clean originals, but many have watermarks and must NOT be used as visuals. Prefer the original uploader (police dept, court, news station) over creator re-uploads. Flag watermarked links as unsuitable.
- If I paste links, review them first, then research additional *distinct* YouTube locators as needed. If no suitable distinct YouTube material can be verified for a beat, **flag the gap** — do NOT invent a timestamp/shot and do NOT fill it by re-using a generic 10-sec placeholder.
- A YouTube link is a locator, not an imported file.

**Source Diversity (This Prevents the Lazy 8-Source → 90-Scene Problem):**
- You **MUST NOT** reuse the same `Source ID` + same `selected source range` (e.g. `00:00:00,000–00:00:10,000`) for more than **2 consecutive placements** or for more than **15% of total project duration**.
- Each narrative beat needs its own distinct source window that actually matches what is being said. If you must reuse a Source ID, you **MUST** choose a different in/out crop and justify it in `Care:` (why this different crop fits this beat).
- Do not use generic `provisional/unreviewed crop, 10 sec` for every card. Every `Preview:` must be a distinct, beat-specific window (e.g. `~0:42–0:46`, `0:29–0:33`, `1:20–1:28`) with what is actually visible described in `Show:`.
- Use however many distinct sources the story actually requires — do not artificially limit to 8. If the example had 26 sources, you may create 20+ if needed. Source library must list every Source ID used.

**Accuracy:**
- Distinguish actual event footage vs later news/court/briefing context. Include source title / uploader / link / verified date. Never invent quotes, speakers, visuals, or precise in/out points.
- Mark every `Preview` range as `approximate` until checked. State clearly if audio or continuous video was not reviewed.
- Treat sensitive people/events respectfully; no graphic material or identifiable private details unless I expressly request it.

**Timing:**
- Inspect file units yourself. Use corrected SRT `HH:MM:SS,mmm` cue starts for alignment and JSON `words.start_time/end_time` (ms relative to segment start) for anchors inside a cue: `absolute ms = segment.start/1000 + word_offset`. Convert µs ↔ ms correctly. Do NOT assume JSON caption ends = continuous SRT ends.
- Use exact `HH:MM:SS,mmm` project times and exact `At:` narration phrases. Do not move narration/captions. Flag conflicts / missing word timings / uncertain anchors instead of guessing.

**Casefile Studio Guide — Required Format:**
- Keep this exact card together per placement, in order: `At / Show / Preview / Label / Care / Source ID / Your timing`
- Add `**Narration — unchanged:**` verbatim paragraph after each card, then `**Source ID:**`, `**Your timing:** HH:MM:SS,mmm --> HH:MM:SS,mmm`.
- Continuous coverage from `00:00:00,000` through verified baseline end (`00:31:37,100` or as supplied), with `scene N end = scene N+1 start`. If first caption starts at `00:00:00,167`, include `00:00:00,000–00:00:00,167` inside **existing scene 1** and explicitly name its Source ID / YouTube link / selected range in *both* the Opening Instruction and Placement 1. Do not create a blank scene.
- Deliver: Opening Instruction + `How to use` + `Same-crop loop rule` + `Script-by-script placement` (with HOOK / CHAPTER 1… headings) + `Source library — YouTube only` + `Loop-join & Transition Table`.

**Crop Loop Rule (Picture-Only, No Substitution):**
- If selected source crop < scene duration, repeat **that exact crop from its own beginning** inside the same scene, trim final repeat at scene end. Never switch source, add scene, go beyond crop, freeze frame, change speed, or carry loop into next scene. Loop picture only — narration/captions continue once.
- If crop/boundaries unavailable, flag as `BLOCKED` — do not substitute.

**Transitions — Off By Default:**
- Add an easy-to-find **Loop-Join Transition Table** after placements. For each scene where a crop must loop, suggest *optional* 150–250 ms cross-dissolve inside the existing scene (no extra handles, no duration change). State `off by default — apply/change/remove at will`. Do the same for optional inter-scene cuts. Never auto-apply.

**CapCut Guide:**
- Follow CapCut template: numbered insert cards with pre-insert project time `HH:MM:SS:FF @ actual FPS`, `pause-after` / `resume-with` exact phrases, Source ID / YouTube link, approximate `MM:SS.s` source in/out + duration, what is heard/seen, Label, Care.
- Use source's original audio; narration/picture/captions/music pause together, then resume together. Do not force template's insert count.
- Distinguish project clock vs source clock. Explain lengthening of working edit and work backwards 10→1. Check caption splits at breaks.

**Validation Before Delivery:**
- Verify every `Your timing` is contiguous, every `At:` exists verbatim, every `Source ID` is in library and every link is YouTube, opening `00:00:00,000` covered, ending through baseline.
- Keep ms internally; note frame-snapping at output FPS may shift transition by 1 frame.
- Deliver two `.md` files + short `Missing Sources / Unverified Ranges / Timing Uncertainties` list. Never claim preview/export verified unless tested.

**When Updating an Approved Guide:**
Do not silently replace source, crop, timings, or add scenes. Propose replacement and wait for approval. Preserve loop rule.

---
**Optional YouTube Research Hints (paste here — watermarks are OK for research, not for visuals):**
PASTE LINKS HERE
