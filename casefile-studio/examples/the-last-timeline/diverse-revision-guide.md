# The Last Timeline — Casefile Studio guide, DIVERSE REVISION FOR APPROVAL

**105 narration-derived placements · 20 original YouTube picture sources · 73 distinct selected source windows · 32 BLOCKED beats · 8 optional audio candidates**

This is a **proposed replacement draft**, not an applied change to the previous guide. New hook subdivisions and every source/crop below are presented for your review. Original guides, narration, captions and JSON remain untouched. The placement count follows the supplied narration’s beat boundaries, not an example’s scene count. Most paragraphs remain one placement; the long hook is divided at existing timed words/sentences so its 42-second first paragraph is not one repeated CCTV crop.

## Opening Instruction

Existing opening **placement 1** uses **C01**, **https://www.youtube.com/watch?v=z0GGKSasvIg**, selected source crop **approximately `00:00:40,000–00:00:44,000`** (rail-level case-report B-roll). Place it from **`00:00:00,000` through `00:00:01,800`**, including the **67 ms lead-in** before the first caption at **`00:00:00,067`** in the same scene. Do not add a blank lead-in or move the narration. This is later case-location reporting, not a recording of the killing. The source crop has storyboard-sample support, but its continuous motion, exact edges, rights and imported availability still need checking. If unavailable, mark this scene BLOCKED rather than substituting another source.

## How to use

1. Load the supplied corrected SRT text (`captions_corrected.srt.md`; make a byte-identical `.srt` copy if required) and corrected JSON for word anchors, plus the unchanged narration. Confirm Casefile’s actual timing-input precedence. It has not been tested here.
2. Baseline is **00:31:37,100**: JSON duration/audio target duration **1,897,100,000 µs**, start 0, speed 1, matching the last continuous SRT end. This is the actual supplied 4,402-word narration including the long hook, not the earlier outline runtime.
3. JSON project/segment time ranges are **microseconds**; `words.start_time/end_time` are **milliseconds relative to segment start**. Inside-cue absolute ms = segment.target.start / 1000 + word offset. At a cue start use its exact SRT start. Round an internal word anchor only once to ms. Never force raw JSON caption ends to match continuous SRT ends.
4. All `Your timing` intervals are exact **project/narration** times and are contiguous from zero to baseline end, including reserved BLOCKED intervals. All `Preview` ranges are **approximate source-video** times. A blocked interval is **not** covered picture; the plan is not export-ready until those gaps are resolved.
5. CapCut JSON reports **30.0 fps**; Casefile output FPS is **unknown**, not inherited from the template. At Casefile’s actual F, snap a shared picture boundary once to `round(ms × F / 1000)`, using the same frame as preceding out/next in. Keep narration and caption inputs unchanged. Arbitrary ms boundaries may move up to a frame in output. Do not round the two sides independently.
6. The draft has **zero video segments**, 738 text segments and one audio segment. Import actual lawfully obtained media; YouTube links are locators, not imported files. No claim is made that the draft currently has pictures. Normal montage source audio is muted; narration/captions continue once.
7. The card order is **At / Show / Preview / Label / Care / Source ID / Your timing**, followed by unchanged narration text and repeated source/timing identifiers for copy-paste. Hook narration is partitioned verbatim into shorter chunks; its words/order are not rewritten. No private, graphic or generic stock substitutions are prescribed.
8. Repetition audit: no identical Source ID + selected range appears for more than **1 consecutive placement(s)**; the largest exact-pair allocation is **1.46%** of total baseline, below 15%. This is not an excuse for disguised reuse: the same photo/CCTV appearing in multiple reports is identified as the same underlying image, not a novel camera angle.

## Same-crop loop rule — picture only

After review approves a selected crop, if it is shorter than its scene, restart **that exact crop from its beginning** inside that same scene and trim the last repetition at the original scene end. Do not select another source, add a scene, exceed the crop, freeze a frame, alter speed or run the loop into the next scene. Narration/captions run once, unshifted. If crop bounds or media are unavailable, **BLOCKED**, not substitute. The app must support fixed-boundary looping; an instruction alone does not prove it works.

**Short-shot fatigue flag:** placements **23, 24, 40, 52, 59, 92 and 96** would require more than seven passes of their brief selected crop if used unchanged. These are real sampled windows, not invented longer trims. They meet the requested exact-pair limits but still need editorial review; approve a better beat-matching crop/source before changing them. Do not silently stretch a crop to reduce repetition.

Effects are **OFF by default**. At a loop join, optionally choose a subtle **200 ms cross-dissolve**, adjustable within roughly 150–250 ms, blending only the crop’s end with its own beginning inside the existing scene. No outside handles, no shorter/longer scene, no shifted narration or captions. If the approved crop/final remainder is too short, or the app cannot compensate the blend inside the fixed interval, flag it and retain a normal cut. No effects have been applied or tested.

## Script-by-script placement

## HOOK

### 1. Narration beat

**At:** “Three minutes”  
**Show:** Low, rail-level view down the tracks in the case report.  
**Preview:** ['I feel cheated': Family of murdered 14-year-old Tampa boy speaks out, offers reward](https://www.youtube.com/watch?v=z0GGKSasvIg) — **approximate** source crop `00:00:40,000–00:00:44,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-24 | ARCHIVE / case context  
**Care:** Exact discovery point and filming date unconfirmed; later news B-roll. Reusing this original upload with this specific sampled window because: Establishes the case corridor without pretending to show the killing. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 1, zero-based existing word slot 0; SRT cue start. Visual lead-in at zero; spoken/caption onset remains 00:00:00,067.  
**Source ID:** C01  
**Your timing:** `00:00:00,000 --> 00:00:01,800`

**Narration — unchanged:**

Three minutes.

**Source ID:** C01  
**Your timing:** `00:00:00,000 --> 00:00:01,800`

### 2. Narration beat

**At:** “That is the whole distance between a boy”  
**Show:** Jevario’s car portrait, as carried in the April reward report.  
**Preview:** ['I feel cheated': Family of murdered 14-year-old Tampa boy speaks out, offers reward](https://www.youtube.com/watch?v=z0GGKSasvIg) — **approximate** source crop `00:01:44,000–00:01:52,000` (8 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-24 | ARCHIVE / case context  
**Care:** Crop/blur the other child visible behind him; this is a photograph already present in the source, not a newly frozen video frame. Reusing this original upload with this specific sampled window because: Puts the victim before the timeline; different from the rail-level opening. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 2, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C01  
**Your timing:** `00:00:01,800 --> 00:00:20,300`

**Narration — unchanged:**

That is the whole distance between a boy being alive and a household being changed permanently — not three hours, not a long night of waiting, three minutes on a bright Wednesday afternoon in April, in a Tampa neighborhood where sprinklers were ticking and nothing was supposed to happen.

**Source ID:** C01  
**Your timing:** `00:00:01,800 --> 00:00:20,300`

### 3. BLOCKED — Narration beat

**At:** “At three thirty-three, a lens no bigger”  
**Show:** BLOCKED — The specified two-person 3:33 camera view is not established by the three-person release.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 8, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G003 — unresolved source registry, not a media asset  
**Your timing:** `00:00:20,300 --> 00:00:31,067`

**Narration — unchanged:**

At three thirty-three, a lens no bigger than a thumb watched two teenagers turn onto a street that was about to run out of road. One walked a half-step ahead.

**Source ID:** G003  
**Your timing:** `00:00:20,300 --> 00:00:31,067`

### 4. BLOCKED — Narration beat

**At:** “The other followed with his hands in his”  
**Show:** BLOCKED — Hands, gait and following distance in the described two-person shot have no verified matching crop.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 12, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G004 — unresolved source registry, not a media asset  
**Your timing:** `00:00:31,067 --> 00:00:42,700`

**Narration — unchanged:**

The other followed with his hands in his pockets, shoulders loose, the particular walk of someone who trusts the person in front of him. Neither looked up at the camera. Neither had a reason to.

**Source ID:** G004  
**Your timing:** `00:00:31,067 --> 00:00:42,700`

### 5. Narration beat

**At:** “The frame holds them for less than a”  
**Show:** Vegetation and ground beside the railway in the report.  
**Preview:** ['I feel cheated': Family of murdered 14-year-old Tampa boy speaks out, offers reward](https://www.youtube.com/watch?v=z0GGKSasvIg) — **approximate** source crop `00:01:28,000–00:01:32,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-24 | ARCHIVE / case context  
**Care:** Do not identify an exact discovery point. Reusing this original upload with this specific sampled window because: Location context for the camera gap, not an asserted empty CCTV frame. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 18, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C01  
**Your timing:** `00:00:42,700 --> 00:00:55,860`

**Narration — unchanged:**

The frame holds them for less than a second, and then the pavement is empty again and the afternoon resumes being ordinary. Somewhere behind those fences, someone is folding laundry. Someone is scrolling.

**Source ID:** C01  
**Your timing:** `00:00:42,700 --> 00:00:55,860`

### 6. BLOCKED — Narration beat

**At:** “Someone is deciding what to cook. A dog”  
**Show:** BLOCKED — No case footage verifies the hook’s laundry, cooking, barking dog or neighbors’ knowledge.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 23, zero-based existing word slot 6; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** G006 — unresolved source registry, not a media asset  
**Your timing:** `00:00:55,860 --> 00:01:07,367`

**Narration — unchanged:**

Someone is deciding what to cook. A dog barks two houses down and stops. Nobody on that block knows a clock has just started running, or that it will stop at three thirty-six.

**Source ID:** G006  
**Your timing:** `00:00:55,860 --> 00:01:07,367`

### 7. BLOCKED — Narration beat

**At:** “Three minutes later, the same lens catches movement”  
**Show:** BLOCKED — No original YouTube crop of the described lone 3:36 departure was established.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 28, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G007 — unresolved source registry, not a media asset  
**Your timing:** `00:01:07,367 --> 00:01:15,067`

**Narration — unchanged:**

Three minutes later, the same lens catches movement. One figure, returning the way he came. Alone.

**Source ID:** G007  
**Your timing:** `00:01:07,367 --> 00:01:15,067`

### 8. BLOCKED — Narration beat

**At:** “Not hurrying, not staring at his hands, not”  
**Show:** BLOCKED — The post-shooting gait/hand movements described here cannot be illustrated by the unrelated escape-running video.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 30, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G008 — unresolved source registry, not a media asset  
**Your timing:** `00:01:15,067 --> 00:01:29,100`

**Narration — unchanged:**

Not hurrying, not staring at his hands, not breaking stride — just walking past the same fences under the same white sky with the same loose shoulders. The other boy does not come back into frame.

**Source ID:** G008  
**Your timing:** `00:01:15,067 --> 00:01:29,100`

### 9. Narration beat

**At:** “He never will, on any camera, on any”  
**Show:** Jevario’s standing outdoor portrait.  
**Preview:** [15-year-old arrested for murder of Tampa teen found near railroad tracks](https://www.youtube.com/watch?v=ehT8yrPb9E0) — **approximate** source crop `00:00:16,000–00:00:19,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2024-12-05 | ARCHIVE / case context  
**Care:** Portrait from official news coverage; not a final-day image. Reusing this original upload with this specific sampled window because: Returns to the victim while narration addresses his absence. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 34, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C19  
**Your timing:** `00:01:29,100 --> 00:01:42,267`

**Narration — unchanged:**

He never will, on any camera, on any street, anywhere again. Somewhere inside those one hundred and eighty seconds lies every answer this case will spend years trying to drag out.

**Source ID:** C19  
**Your timing:** `00:01:29,100 --> 00:01:42,267`

### 10. Narration beat

**At:** “I'm not giving you those seconds yet. I'm”  
**Show:** Tampa Police building sign/exterior.  
**Preview:** [New video released of Tampa teen killed in April](https://www.youtube.com/watch?v=rT4s5tphM4g) — **approximate** source crop `00:00:40,000–00:00:43,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-05-09 | ARCHIVE / case context  
**Care:** Later case-report B-roll, not a crime-scene response. Reusing this original upload with this specific sampled window because: Signals the documented investigation without inventing phone or rail discoveries. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 38, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C06  
**Your timing:** `00:01:42,267 --> 00:01:55,000`

**Narration — unchanged:**

I'm not giving you those seconds yet. I'm not telling you what was found beside the rails, what was written in the messages nobody thought would matter, or why nearly a year passed before anyone was charged.

**Source ID:** C06  
**Your timing:** `00:01:42,267 --> 00:01:55,000`

### 11. Narration beat

**At:** “What I'll give you is the shape of”  
**Show:** Jevario’s standing portrait in the April appeal.  
**Preview:** [Local Tampa officials seek tips in shooting death of 14-year-old](https://www.youtube.com/watch?v=eUIhBElp_uc) — **approximate** source crop `00:00:33,000–00:00:37,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-22 | ARCHIVE / case context  
**Care:** Same original portrait may recur in other reports; this is a new editorial use, not a new camera angle. Reusing this original upload with this specific sampled window because: Victim identification, rather than a speculative image of the other teenager. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 43, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C02  
**Your timing:** `00:01:55,000 --> 00:02:02,600`

**Narration — unchanged:**

What I'll give you is the shape of it: both of them were children. One was fourteen. The other was fifteen.

**Source ID:** C02  
**Your timing:** `00:01:55,000 --> 00:02:02,600`

### 12. Narration beat

**At:** “And while the sun was still up that”  
**Show:** Justice for Jevario website page visible in the news report.  
**Preview:** [Family of Jevario Buie launches website in hopes of finding his killer](https://www.youtube.com/watch?v=pAtmiAZUuGU) — **approximate** source crop `00:01:48,000–00:01:56,000` (8 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** Tampa Bay 28 | upload 2024-04-29 | ARCHIVE / case context  
**Care:** No private account contents; keep date label. Reusing this original upload with this specific sampled window because: Family’s public-facing effort, not a recreation of the mother’s afternoon. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 46, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C15  
**Your timing:** `00:02:02,600 --> 00:02:13,067`

**Narration — unchanged:**

And while the sun was still up that day, a mother who didn't yet know her afternoon had ended was about to begin measuring time in a way she would never be able to stop.

**Source ID:** C15  
**Your timing:** `00:02:02,600 --> 00:02:13,067`

### 13. Narration beat

**At:** “And that still isn't the part that stays”  
**Show:** Wide courtroom view in the case’s later news report.  
**Preview:** [Sentencing is planned for Jahmir Moore on Friday](https://www.youtube.com/watch?v=MrRx2a1NT8s) — **approximate** source crop `00:00:22,000–00:00:24,000` (2 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2026-10-16 | ARCHIVE / case context  
**Care:** Not the instant of verdict; do not identify people from this small sample. Reusing this original upload with this specific sampled window because: A brief preview of the later legal stage mentioned by the hook. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 50, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C21  
**Your timing:** `00:02:13,067 --> 00:02:16,267`

**Narration — unchanged:**

And that still isn't the part that stays with people.

**Source ID:** C21  
**Your timing:** `00:02:13,067 --> 00:02:16,267`

### 14. Narration beat

**At:** “Further down this timeline there is a secure”  
**Show:** Fenced detention-area exterior/vegetation in the recapture report.  
**Preview:** [Teen accused of murder facing more charges after escaping detention center, Tampa police say](https://www.youtube.com/watch?v=OHILsLEzZ40) — **approximate** source crop `00:02:16,000–00:02:20,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-09 | ARCHIVE / case context  
**Care:** Do not expose residential details or assert how the fence was crossed. Reusing this original upload with this specific sampled window because: Previews custody context, not an escape route. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 51, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C09  
**Your timing:** `00:02:16,267 --> 00:02:30,500`

**Narration — unchanged:**

Further down this timeline there is a secure facility that wasn't, a search unfolding while a stadium emptied, a grandfather speaking into a courtroom microphone, and a number of years that satisfied absolutely no one.

**Source ID:** C09  
**Your timing:** `00:02:16,267 --> 00:02:30,500`

### 15. Narration beat

**At:** “I'm leaving all of it exactly where it”  
**Show:** Moore standing in a red uniform and yellow vest at the hearing.  
**Preview:** [Teen accused of murder denied bond after escaping from custody](https://www.youtube.com/watch?v=MRoEPt81UtQ) — **approximate** source crop `00:00:00,000–00:00:03,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2024-12-18 | ARCHIVE / case context  
**Care:** December 2024 hearing context, not the September trial. Reusing this original upload with this specific sampled window because: Previews the documented custody-to-court chain. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 56, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C18  
**Your timing:** `00:02:30,500 --> 00:02:43,233`

**Narration — unchanged:**

I'm leaving all of it exactly where it belongs — later — because if I handed you the ending now, you'd walk straight past the thing that should unsettle you most: how completely normal the beginning looked.

**Source ID:** C18  
**Your timing:** `00:02:30,500 --> 00:02:43,233`

### 16. Narration beat

**At:** “A straight warning before we go further. This”  
**Show:** Low track view in the April family-appeal report.  
**Preview:** [With no arrests made, family pleads for information after 14-year-old shot and killed in Tampa](https://www.youtube.com/watch?v=YiVcQQGFf_E) — **approximate** source crop `00:00:36,000–00:00:39,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-26 | ARCHIVE / case context  
**Care:** No graphic imagery; avoid adjoining interview speculation. Reusing this original upload with this specific sampled window because: Restrained case-location picture under the content warning. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 61, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C14  
**Your timing:** `00:02:43,233 --> 00:02:54,767`

**Narration — unchanged:**

A straight warning before we go further. This account contains the killing of a child, a crime scene, digital evidence, and grief that never resolves into anything clean.

**Source ID:** C14  
**Your timing:** `00:02:43,233 --> 00:02:54,767`

### 17. Narration beat

**At:** “There are parents in this story who never”  
**Show:** Wide sentencing courtroom with people at counsel tables and near the bench.  
**Preview:** [Florida teen gets 55 years in 15-year-old's murder](https://www.youtube.com/watch?v=zyKDsEekos4) — **approximate** source crop `00:02:24,000–00:02:32,000` (8 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2026-10-17 | ARCHIVE / case context  
**Care:** Do not show a child speaking or claim to know the adult’s exact words without listening. Reusing this original upload with this specific sampled window because: Context for a judgment that does not undo a loss. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 65, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C17  
**Your timing:** `00:02:54,767 --> 00:03:06,633`

**Narration — unchanged:**

There are parents in this story who never receive an answer, and a verdict that closes a file without closing a wound. If that is heavier than you can carry today, stop here with no guilt attached.

**Source ID:** C17  
**Your timing:** `00:02:54,767 --> 00:03:06,633`

### 18. Narration beat

**At:** “The story will wait for you”  
**Show:** Jevario’s standing portrait in the station report.  
**Preview:** [Family of Jevario Buie launches website in hopes of finding his killer](https://www.youtube.com/watch?v=pAtmiAZUuGU) — **approximate** source crop `00:00:20,000–00:00:23,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** Tampa Bay 28 | upload 2024-04-29 | ARCHIVE / case context  
**Care:** Use source’s existing photo display; do not freeze or stretch it. Reusing this original upload with this specific sampled window because: Short, respectful pause before channel introduction. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 71, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C15  
**Your timing:** `00:03:06,633 --> 00:03:08,600`

**Narration — unchanged:**

The story will wait for you.

**Source ID:** C15  
**Your timing:** `00:03:06,633 --> 00:03:08,600`

### 19. Narration beat

**At:** “If you're new here, you've found The Last”  
**Show:** Side view of the railway corridor.  
**Preview:** ['I feel cheated': Family of murdered 14-year-old Tampa boy speaks out, offers reward](https://www.youtube.com/watch?v=z0GGKSasvIg) — **approximate** source crop `00:00:32,000–00:00:35,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-24 | ARCHIVE / case context  
**Care:** No exact scene-location assertion. Reusing this original upload with this specific sampled window because: Case-specific opening context for channel introduction. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 72, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C01  
**Your timing:** `00:03:08,600 --> 00:03:11,867`

**Narration — unchanged:**

If you're new here, you've found The Last Timeline.

**Source ID:** C01  
**Your timing:** `00:03:08,600 --> 00:03:11,867`

### 20. Narration beat

**At:** “Subscribe now so the rest of this case”  
**Show:** Public memorial website, including a memorial image.  
**Preview:** [Family of Jevario Buie launches website in hopes of finding his killer](https://www.youtube.com/watch?v=pAtmiAZUuGU) — **approximate** source crop `00:01:56,000–00:02:00,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** Tampa Bay 28 | upload 2024-04-29 | ARCHIVE / case context  
**Care:** Use only the public page shown by the station, not invented browsing. Reusing this original upload with this specific sampled window because: Connects audience engagement with the public case record. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 73, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C15  
**Your timing:** `00:03:11,867 --> 00:03:23,787`

**Narration — unchanged:**

Subscribe now so the rest of this case actually reaches you instead of vanishing into the feed, and drop a comment telling me where you're watching from — the city, the country, the hour on your clock.

**Source ID:** C15  
**Your timing:** `00:03:11,867 --> 00:03:23,787`

### 21. Narration beat

**At:** “I read them; I like knowing how far”  
**Show:** Jevario’s portrait after the briefing report.  
**Preview:** [New video released of Tampa teen killed in April](https://www.youtube.com/watch?v=rT4s5tphM4g) — **approximate** source crop `00:02:08,000–00:02:12,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-05-09 | ARCHIVE / case context  
**Care:** Skip if a moving-picture review reveals a transition or sensitive adjacent image. Reusing this original upload with this specific sampled window because: Returns attention to the victim before the event chronology. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 79, zero-based existing word slot 10; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** C06  
**Your timing:** `00:03:23,787 --> 00:03:28,647`

**Narration — unchanged:**

I read them; I like knowing how far a story travels. Take a breath.

**Source ID:** C06  
**Your timing:** `00:03:23,787 --> 00:03:28,647`

### 22. Narration beat

**At:** “We're going back to the beginning: a spring”  
**Show:** Station map zoom toward the reported Tampa location.  
**Preview:** [Local Tampa officials seek tips in shooting death of 14-year-old](https://www.youtube.com/watch?v=eUIhBElp_uc) — **approximate** source crop `00:00:20,000–00:00:24,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-22 | ARCHIVE / case context  
**Care:** Station graphic, not an independently surveyed scene map. Reusing this original upload with this specific sampled window because: Establishes geographical context for return to April. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 81, zero-based existing word slot 6; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** C02  
**Your timing:** `00:03:28,647 --> 00:03:39,200`

**Narration — unchanged:**

We're going back to the beginning: a spring afternoon, two boys who called each other friends, and the three minutes that split one family's life into a before and an after.

**Source ID:** C02  
**Your timing:** `00:03:28,647 --> 00:03:39,200`

## CHAPTER 1 — The call and the cameras

### 23. Narration beat

**At:** “On April 17, 2024, just after 3:30”  
**Show:** Busch/Rome street-sign shot.  
**Preview:** [Local Tampa officials seek tips in shooting death of 14-year-old](https://www.youtube.com/watch?v=eUIhBElp_uc) — **approximate** source crop `00:00:25,000–00:00:28,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-22 | ARCHIVE / case context  
**Care:** Street sign is contextual; not necessarily the precise discovery spot. Reusing this original upload with this specific sampled window because: Matches the named intersection/corridor. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 86, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C02  
**Your timing:** `00:03:39,200 --> 00:04:04,740`

**Narration — unchanged:**

On April 17, 2024, just after 3:30 p.m., Tampa police responded to reports of gunfire near the 1400 block of West Busch Boulevard. Reporting by the Tampa Bay Times described neighbors hearing shots and seeing someone running west along railroad tracks parallel to the boulevard. Those observations supplied a direction, not an identity.

**Source ID:** C02  
**Your timing:** `00:03:39,200 --> 00:04:04,740`

### 24. Narration beat

**At:** “Officers found fourteen year old Jevario Buie near”  
**Show:** Trackside vegetation and rail view.  
**Preview:** ['I feel cheated': Family of murdered 14-year-old Tampa boy speaks out, offers reward](https://www.youtube.com/watch?v=z0GGKSasvIg) — **approximate** source crop `00:00:56,000–00:00:59,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-24 | ARCHIVE / case context  
**Care:** No body or discovery reenactment; filming date uncertain. Reusing this original upload with this specific sampled window because: Non-graphic location context for discovery. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 94, zero-based existing word slot 6; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** C01  
**Your timing:** `00:04:04,740 --> 00:04:26,100`

**Narration — unchanged:**

Officers found fourteen year old Jevario Buie near the tracks between Busch Boulevard and Rome Avenue. According to the police account, he died at the scene. The location was in Tampa’s Lowry Park neighborhood. What happened there would require investigators to reconstruct the movements that preceded the reports of gunfire.

**Source ID:** C01  
**Your timing:** `00:04:04,740 --> 00:04:26,100`

### 25. Narration beat

**At:** “Jevario was an eighth grader at Memorial Middle”  
**Show:** Jevario’s car portrait.  
**Preview:** [Family of Jevario Buie launches website in hopes of finding his killer](https://www.youtube.com/watch?v=pAtmiAZUuGU) — **approximate** source crop `00:00:24,000–00:00:27,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** Tampa Bay 28 | upload 2024-04-29 | ARCHIVE / case context  
**Care:** Blur other child; no selected source verifies a school or football scene. Reusing this original upload with this specific sampled window because: Victim character detail rather than generic football footage. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 102, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C15  
**Your timing:** `00:04:26,100 --> 00:04:46,667`

**Narration — unchanged:**

Jevario was an eighth grader at Memorial Middle School who played football, as contemporary reporting from 10 Tampa Bay documented. His family told ABC Action News he was excited about playing high school football and hoped to attend Tampa Tech. That was an ambition, not confirmation of an arranged school placement.

**Source ID:** C15  
**Your timing:** `00:04:26,100 --> 00:04:46,667`

### 26. Narration beat

**At:** “Surveillance recordings from nearby homes preserved portions of”  
**Show:** Three teenagers progress into the residential-camera image.  
**Preview:** [Tampa Police Seek Persons of Interest in Jevario Buie death](https://www.youtube.com/watch?v=a0NS9AsqdeA) — **approximate** source crop `00:00:01,000–00:00:07,000` (6 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** TampaPD | upload 2024-05-09 | ARCHIVE / case context  
**Care:** Not the killing and not a continuous 46-minute walk. Reusing this original upload with this specific sampled window because: Actual released surveillance supports the company documented by investigators. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 110, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C04  
**Your timing:** `00:04:46,667 --> 00:05:11,500`

**Narration — unchanged:**

Surveillance recordings from nearby homes preserved portions of that afternoon. In its December 5, 2024 release, Tampa police described footage showing Jevario, Jahmir Moore, and another person walking together between 2:41 and 3:27 p.m. That interval established their presence together without explaining everything that happened afterward.

**Source ID:** C04  
**Your timing:** `00:04:46,667 --> 00:05:11,500`

### 27. BLOCKED — Narration beat

**At:** “At 3:33 p.m., police said, footage”  
**Show:** BLOCKED — The distinct two-person and lone-departure camera views and exact North Rome sequence are not verified here.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 118, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G027 — unresolved source registry, not a media asset  
**Your timing:** `00:05:11,500 --> 00:05:35,667`

**Narration — unchanged:**

At 3:33 p.m., police said, footage showed Moore and Jevario walking north on North Rome Avenue toward a dead end near the scene. At 3:36 p.m., Moore appeared walking west and south, away from the area. Jevario was not seen accompanying him. The recordings documented movement; they did not, by themselves, establish intent.

**Source ID:** G027  
**Your timing:** `00:05:11,500 --> 00:05:35,667`

### 28. Narration beat

**At:** “Those recorded minutes would become a public appeal”  
**Show:** Chief Bercaw at the podium before the shared surveillance.  
**Preview:** [CRIMESTOPPERS REWARD INCREASED IN HOMICIDE INVESTIGATION OF 14-YEAR-OLD JEVARIO BUIE](https://www.youtube.com/watch?v=WV986cbBAqg) — **approximate** source crop `00:02:25,000–00:02:31,000` (6 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** TampaPD | upload 2024-05-09 | ARCHIVE / case context  
**Care:** Muted montage; do not imply this is December identification. Reusing this original upload with this specific sampled window because: May public appeal context for the released images. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 127, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C05  
**Your timing:** `00:05:35,667 --> 00:05:53,000`

**Narration — unchanged:**

Those recorded minutes would become a public appeal for help identifying the other two teenagers. In May, police released video showing Jevario with two young men and asked the community for information. At that stage, the two companions had not been publicly identified.

**Source ID:** C05  
**Your timing:** `00:05:35,667 --> 00:05:53,000`

### 29. Narration beat

**At:** “Moore’s name belonged to a later announcement. For”  
**Show:** Chief Bercaw at the December announcement.  
**Preview:** [Teen to be charged as adult for murder of 14-year-old Jevario Buie](https://www.youtube.com/watch?v=B5qzKsfKcAA) — **approximate** source crop `00:01:22,000–00:01:27,000` (5 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-05 | ARCHIVE / case context  
**Care:** Source window differs from earlier portraits and maps; it is later briefing footage. Reusing this original upload with this specific sampled window because: Later named-suspect announcement, explicitly date-separated from May. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 135, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C03  
**Your timing:** `00:05:53,000 --> 00:06:03,200`

**Narration — unchanged:**

Moore’s name belonged to a later announcement. For anyone watching that appeal, the unanswered question remained: who were the two people walking with Jevario?

**Source ID:** C03  
**Your timing:** `00:05:53,000 --> 00:06:03,200`

## CHAPTER 2 — The public appeal

### 30. Narration beat

**At:** “On April 22, 2024, Tampa police appealed for”  
**Show:** April news presenter beside Jevario’s photos.  
**Preview:** [Local Tampa officials seek tips in shooting death of 14-year-old](https://www.youtube.com/watch?v=eUIhBElp_uc) — **approximate** source crop `00:00:03,000–00:00:11,000` (8 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-22 | ARCHIVE / case context  
**Care:** Original station branding retained; no creator re-upload. Reusing this original upload with this specific sampled window because: The initial public appeal itself. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 139, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C02  
**Your timing:** `00:06:03,200 --> 00:06:25,633`

**Narration — unchanged:**

On April 22, 2024, Tampa police appealed for the community’s help identifying whoever was responsible for Jevario’s death. Investigators needed information, not assumptions repeated until they sounded certain. The family’s efforts unfolded alongside that request, keeping his name before people who might know something.

**Source ID:** C02  
**Your timing:** `00:06:03,200 --> 00:06:25,633`

### 31. Narration beat

**At:** “His mother, Jasmine Baldwin, had been helping him”  
**Show:** Public memorial/fundraising webpage in the case report.  
**Preview:** [Family of Jevario Buie launches website in hopes of finding his killer](https://www.youtube.com/watch?v=pAtmiAZUuGU) — **approximate** source crop `00:02:00,000–00:02:04,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** Tampa Bay 28 | upload 2024-04-29 | ARCHIVE / case context  
**Care:** Job-application picture remains unavailable; do not fabricate it. Reusing this original upload with this specific sampled window because: Matches the family fundraiser, not the unfilmed job application. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 146, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C15  
**Your timing:** `00:06:25,633 --> 00:06:50,167`

**Narration — unchanged:**

His mother, Jasmine Baldwin, had been helping him begin his first job application about two hours before he died. His grandfather, Michael Baldwin Sr., joined the appeals for answers. His grandmother, JoQuetta Winters, organized a family fundraiser supporting funeral arrangements and related family travel. These were demands arriving before an arrest.

**Source ID:** C15  
**Your timing:** `00:06:25,633 --> 00:06:50,167`

### 32. Narration beat

**At:** “On April 27, Jevario’s loved ones attended a”  
**Show:** Memorial booth/display, photographs and attendees at the crime-victims vigil.  
**Preview:** [Family of a Jevario Buie bids for justice in hopes to find answers in his death](https://www.youtube.com/watch?v=cXp03ZJ5SFg) — **approximate** source crop `00:01:12,000–00:01:16,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** WFLA News Channel 8 | upload 2024-04-28 | ARCHIVE / case context  
**Care:** Wide view only; blur private people/children and avoid intimate distress. Reusing this original upload with this specific sampled window because: Actual vigil coverage rather than funeral or generic crowd. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 155, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C12  
**Your timing:** `00:06:50,167 --> 00:07:08,633`

**Narration — unchanged:**

On April 27, Jevario’s loved ones attended a healing vigil for crime survivors in Tampa. The gathering provided another opportunity to ask for information. It did not resolve the investigation, and public appeals continued as the family prepared for his funeral the following weekend.

**Source ID:** C12  
**Your timing:** `00:06:50,167 --> 00:07:08,633`

### 33. BLOCKED — Narration beat

**At:** “On May 4, the funeral took place at”  
**Show:** BLOCKED — No clean YouTube crop of the May 4 service/burial was verified; a May 3 interview is not the funeral.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 162, zero-based existing word slot 6; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** G033 — unresolved source registry, not a media asset  
**Your timing:** `00:07:08,633 --> 00:07:29,127`

**Narration — unchanged:**

On May 4, the funeral took place at Bible-Based Fellowship Church of Temple Terrace, followed by burial at Orange Hill Cemetery. Family members wore green, his favorite color. The services marked a farewell, but they supplied no answer to the question investigators were still pursuing: who was responsible?

**Source ID:** G033  
**Your timing:** `00:07:08,633 --> 00:07:29,127`

### 34. Narration beat

**At:** “By May 9, the reward had increased to”  
**Show:** Thaddeus Bullard at the police briefing podium.  
**Preview:** [New video released of Tampa teen killed in April](https://www.youtube.com/watch?v=rT4s5tphM4g) — **approximate** source crop `00:01:03,000–00:01:10,000` (7 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-05-09 | ARCHIVE / case context  
**Care:** Date May 9; it is not the family vigil or December announcement. Reusing this original upload with this specific sampled window because: Matches his reward-support role. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 170, zero-based existing word slot 6; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** C06  
**Your timing:** `00:07:29,127 --> 00:07:53,167`

**Narration — unchanged:**

By May 9, the reward had increased to $20,000. ATF, the Florida Attorney General’s Office, Crime Stoppers of Tampa Bay, and community partners supported it. Those donors included Thaddeus Bullard, known professionally as Titus O’Neil. Hillsborough County State Attorney Suzy Lopez joined officials urging people with information to come forward.

**Source ID:** C06  
**Your timing:** `00:07:29,127 --> 00:07:53,167`

### 35. Narration beat

**At:** “Police also released a clip showing Jevario walking”  
**Show:** Patrick Messmer speaking at the May briefing.  
**Preview:** [New video released of Tampa teen killed in April](https://www.youtube.com/watch?v=rT4s5tphM4g) — **approximate** source crop `00:01:28,000–00:01:34,000` (6 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-05-09 | ARCHIVE / case context  
**Care:** Confirm lower-third spelling against narration; do not treat an allegation as a verdict. Reusing this original upload with this specific sampled window because: His investigation statement corresponds to the group-size distinction. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 180, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C06  
**Your timing:** `00:07:53,167 --> 00:08:11,567`

**Narration — unchanged:**

Police also released a clip showing Jevario walking with two people shortly before the shooting. Their investigation, officials said, had not uncovered evidence of a large group participating. That distinction mattered: public speculation was not the same thing as an investigative finding.

**Source ID:** C06  
**Your timing:** `00:07:53,167 --> 00:08:11,567`

### 36. Narration beat

**At:** “There was now a reward, yet no arrest”  
**Show:** Reporter outside the police building in the April appeal package.  
**Preview:** [With no arrests made, family pleads for information after 14-year-old shot and killed in Tampa](https://www.youtube.com/watch?v=YiVcQQGFf_E) — **approximate** source crop `00:01:48,000–00:01:56,000` (8 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-26 | ARCHIVE / case context  
**Care:** Different from the interview/community/portrait windows in this upload. Reusing this original upload with this specific sampled window because: Contemporaneous reporting while the appeal remained unresolved. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 189, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C14  
**Your timing:** `00:08:11,567 --> 00:08:23,567`

**Narration — unchanged:**

There was now a reward, yet no arrest had been announced. That did not establish that nobody had spoken. It left a harder question: what information would move the case forward?

**Source ID:** C14  
**Your timing:** `00:08:11,567 --> 00:08:23,567`

## CHAPTER 3 — The camera canvass

### 37. Narration beat

**At:** “The camera canvass turned the neighborhood into a”  
**Show:** Bercaw at the lectern during his canvass explanation.  
**Preview:** [CRIMESTOPPERS REWARD INCREASED IN HOMICIDE INVESTIGATION OF 14-YEAR-OLD JEVARIO BUIE](https://www.youtube.com/watch?v=WV986cbBAqg) — **approximate** source crop `00:02:11,000–00:02:25,000` (14 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** TampaPD | upload 2024-05-09 | ARCHIVE / case context  
**Care:** Speech timing is automatic-caption-derived; montage audio remains muted. Reusing this original upload with this specific sampled window because: Official account of gathering evidence; not literal footage of door knocks. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 193, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C05  
**Your timing:** `00:08:23,567 --> 00:08:42,967`

**Narration — unchanged:**

The camera canvass turned the neighborhood into a source of evidence. Tampa police later reported obtaining surveillance from nearby residences. Those recordings supplied separate observations of the afternoon, allowing detectives to reconstruct portions of a sequence that no single public account could explain.

**Source ID:** C05  
**Your timing:** `00:08:23,567 --> 00:08:42,967`

### 38. Narration beat

**At:** “This method had a limitation. A recording could”  
**Show:** The group crosses the camera’s near field and tree area.  
**Preview:** [Tampa Police Seek Persons of Interest in Jevario Buie death](https://www.youtube.com/watch?v=a0NS9AsqdeA) — **approximate** source crop `00:00:08,000–00:00:13,000` (5 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** TampaPD | upload 2024-05-09 | ARCHIVE / case context  
**Care:** A different action phase from the entry crop; no inference about intent. Reusing this original upload with this specific sampled window because: Demonstrates the limitations of one surveillance view. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 202, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C04  
**Your timing:** `00:08:42,967 --> 00:09:03,033`

**Narration — unchanged:**

This method had a limitation. A recording could place someone within view, but an image was not an identification. Detectives needed to establish who appeared in the footage, not simply describe where those figures went. Recognizing a face and proving a person’s identity were different investigative tasks.

**Source ID:** C04  
**Your timing:** `00:08:42,967 --> 00:09:03,033`

### 39. Narration beat

**At:** “The police department’s later release organized the recordings”  
**Show:** Released surveillance reproduced inside the report.  
**Preview:** [New video released of Tampa teen killed in April](https://www.youtube.com/watch?v=rT4s5tphM4g) — **approximate** source crop `00:01:40,000–00:01:48,000` (8 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-05-09 | ARCHIVE / case context  
**Care:** Do not claim the report’s source clock is the incident clock or this is three distinct cameras. Reusing this original upload with this specific sampled window because: Supports the use of recorded observations in the timeline. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 210, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C06  
**Your timing:** `00:09:03,033 --> 00:09:27,700`

**Narration — unchanged:**

The police department’s later release organized the recordings around three time references. The first covered 2:41 through 3:27 p.m.; the next was 3:33 p.m.; the last was 3:36 p.m. Read together, those references distinguished the earlier company from the later separation without requiring an uninterrupted recording of every minute.

**Source ID:** C06  
**Your timing:** `00:09:03,033 --> 00:09:27,700`

### 40. Narration beat

**At:** “For investigators, direction also mattered. The department described”  
**Show:** North Rome/West Busch street signs.  
**Preview:** [Teen to be charged as adult for murder of 14-year-old Jevario Buie](https://www.youtube.com/watch?v=B5qzKsfKcAA) — **approximate** source crop `00:01:04,000–00:01:07,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-05 | ARCHIVE / case context  
**Care:** The exact directional walk remains unshown. Reusing this original upload with this specific sampled window because: Spatial context for the named direction; not an unverified departure image. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 219, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C03  
**Your timing:** `00:09:27,700 --> 00:09:50,467`

**Narration — unchanged:**

For investigators, direction also mattered. The department described movement toward a dead end on North Rome Avenue, followed by movement west and south away from the scene. Its published account said Jevario was not visible with the departing teenager. That was a documented observation, not a camera recording of everything that occurred between those points.

**Source ID:** C03  
**Your timing:** `00:09:27,700 --> 00:09:50,467`

### 41. Narration beat

**At:** “The names used in that later account should”  
**Show:** Residential-camera surveillance shown during Bercaw’s request to identify the two people.  
**Preview:** [CRIMESTOPPERS REWARD INCREASED IN HOMICIDE INVESTIGATION OF 14-YEAR-OLD JEVARIO BUIE](https://www.youtube.com/watch?v=WV986cbBAqg) — **approximate** source crop `00:02:36,000–00:02:45,000` (9 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** TampaPD | upload 2024-05-09 | ARCHIVE / case context  
**Care:** Different passage of the briefing, not its introduction. Reusing this original upload with this specific sampled window because: The May identification request, not December naming. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 228, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C05  
**Your timing:** `00:09:50,467 --> 00:10:10,433`

**Narration — unchanged:**

The names used in that later account should not obscure what police were asking in May. At the May 9 conference, Chief Lee Bercaw sought help identifying the two people shown with Jevario. The public footage was an investigative request, not an announcement that every identity had already been established.

**Source ID:** C05  
**Your timing:** `00:09:50,467 --> 00:10:10,433`

### 42. Narration beat

**At:** “Major Patrick Messmer said people close to Jevario”  
**Show:** Messmer answering in the May briefing.  
**Preview:** [New video released of Tampa teen killed in April](https://www.youtube.com/watch?v=rT4s5tphM4g) — **approximate** source crop `00:00:44,000–00:00:50,000` (6 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-05-09 | ARCHIVE / case context  
**Care:** His statement is the investigators’ position, not proof every friend witnessed the crime. Reusing this original upload with this specific sampled window because: Matches the named official’s appeal for cooperation. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 236, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C06  
**Your timing:** `00:10:10,433 --> 00:10:28,100`

**Narration — unchanged:**

Major Patrick Messmer said people close to Jevario knew what had happened and needed to cooperate. That statement conveyed the investigators’ position. It did not establish that every friend had witnessed the crime, or that anyone appearing in the footage necessarily shared responsibility for it.

**Source ID:** C06  
**Your timing:** `00:10:10,433 --> 00:10:28,100`

### 43. Narration beat

**At:** “The canvass had supplied images, locations, and a”  
**Show:** Tampa police vehicles/exterior in the report.  
**Preview:** [New video released of Tampa teen killed in April](https://www.youtube.com/watch?v=rT4s5tphM4g) — **approximate** source crop `00:01:56,000–00:01:59,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-05-09 | ARCHIVE / case context  
**Care:** Not footage of a suspect arrest. Reusing this original upload with this specific sampled window because: Closes the camera-method section with case-specific institutional context. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 244, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C06  
**Your timing:** `00:10:28,100 --> 00:10:40,200`

**Narration — unchanged:**

The canvass had supplied images, locations, and a framework of minutes. What it still needed was a connection between a recorded figure and a name. What evidence would make that connection?

**Source ID:** C06  
**Your timing:** `00:10:28,100 --> 00:10:40,200`

## CHAPTER 4 — A phone left at the scene

### 44. BLOCKED — Narration beat

**At:** “The next lead was at the scene. Jevario’s”  
**Show:** BLOCKED — No verified YouTube image of the recovered phone and its screen was located.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 249, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G044 — unresolved source registry, not a media asset  
**Your timing:** `00:10:40,200 --> 00:10:58,167`

**Narration — unchanged:**

The next lead was at the scene. Jevario’s cellphone lay nearby, displaying unread Instagram messages. According to court records described by the Tampa Bay Times, detectives obtained his phone records and examined conversations that could explain whom he had intended to meet.

**Source ID:** G044  
**Your timing:** `00:10:40,200 --> 00:10:58,167`

### 45. BLOCKED — Narration beat

**At:** “One account drew their attention: jahhgeezyyy. Investigators identified”  
**Show:** BLOCKED — No original YouTube exhibit window verifying both Instagram handles is available.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 257, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G045 — unresolved source registry, not a media asset  
**Your timing:** `00:10:58,167 --> 00:11:21,067`

**Narration — unchanged:**

One account drew their attention: jahhgeezyyy. Investigators identified it as belonging to Jahmir Moore. Jevario used the handle _jdot2xx. The distinction mattered because an online username was only a starting point; connecting it to a person gave the exchanges an identifiable participant behind it.

**Source ID:** G045  
**Your timing:** `00:10:58,167 --> 00:11:21,067`

### 46. BLOCKED — Narration beat

**At:** “Moore had begun following Jevario two days before”  
**Show:** BLOCKED — No verified display of the specific follow dates and meeting messages was found.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 266, zero-based existing word slot 4; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** G046 — unresolved source registry, not a media asset  
**Your timing:** `00:11:21,067 --> 00:11:42,867`

**Narration — unchanged:**

Moore had begun following Jevario two days before the killing. On April 16, he asked whether Jevario would meet him. The following day, another message directed Jevario to meet him halfway. These exchanges documented arrangements made before the encounter, rather than explanations offered after investigators began asking questions.

**Source ID:** G046  
**Your timing:** `00:11:21,067 --> 00:11:42,867`

### 47. BLOCKED — Narration beat

**At:** “A third account, using the name Luh 3”  
**Show:** BLOCKED — No verified original Citgo photograph/message exhibit window was located.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 275, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G047 — unresolved source registry, not a media asset  
**Your timing:** `00:11:42,867 --> 00:12:05,900`

**Narration — unchanged:**

A third account, using the name Luh 3, also communicated with Moore about meeting. Shortly before 2:30 p.m. on April 17, Moore sent Jevario a photograph of a Citgo station at 1815 West Waters Avenue. The image supplied a specific place for detectives to examine, narrowing their search for relevant surveillance.

**Source ID:** G047  
**Your timing:** `00:11:42,867 --> 00:12:05,900`

### 48. Narration beat

**At:** “Police obtained recordings from that area and located”  
**Show:** The three-person group continues beyond the tree toward a vehicle area.  
**Preview:** [Tampa Police Seek Persons of Interest in Jevario Buie death](https://www.youtube.com/watch?v=a0NS9AsqdeA) — **approximate** source crop `00:00:13,000–00:00:17,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** TampaPD | upload 2024-05-09 | ARCHIVE / case context  
**Care:** Not the Citgo image, not the witness interview, and not a separate lone walk. Reusing this original upload with this specific sampled window because: A distinct later phase of the real release supports the camera/meeting connection. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 283, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C04  
**Your timing:** `00:12:05,900 --> 00:12:26,700`

**Narration — unchanged:**

Police obtained recordings from that area and located footage of the three meeting. The photograph and the messages therefore connected two kinds of evidence: plans exchanged online and movements recorded outside. Neither source needed to carry the entire reconstruction alone; each helped investigators interpret the other.

**Source ID:** C04  
**Your timing:** `00:12:05,900 --> 00:12:26,700`

### 49. BLOCKED — Narration beat

**At:** “About two months after Jevario’s death, detectives interviewed”  
**Show:** BLOCKED — The third teenager’s interview is not verified as a releasable YouTube recording; do not identify a young witness.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 291, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G049 — unresolved source registry, not a media asset  
**Your timing:** `00:12:26,700 --> 00:12:47,867`

**Narration — unchanged:**

About two months after Jevario’s death, detectives interviewed the third teenager. The reported records did not explain that delay. He said he had tried to persuade Jevario to return to his house, but Jevario continued walking with Moore. That was his account to investigators, not something the messages themselves established.

**Source ID:** G049  
**Your timing:** `00:12:26,700 --> 00:12:47,867`

### 50. Narration beat

**At:** “Keep following the evidence with us, and subscribe”  
**Show:** Jevario’s car portrait at the end of the appeal.  
**Preview:** [Local Tampa officials seek tips in shooting death of 14-year-old](https://www.youtube.com/watch?v=eUIhBElp_uc) — **approximate** source crop `00:00:38,000–00:00:41,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-04-22 | ARCHIVE / case context  
**Care:** Blur the child in the background; no app demo or recreated phone. Reusing this original upload with this specific sampled window because: Victim-focused section close/CTA. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 299, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C02  
**Your timing:** `00:12:47,867 --> 00:12:58,667`

**Narration — unchanged:**

Keep following the evidence with us, and subscribe for the next chapter. Police had a handle and a meeting place. What would give them access to Moore’s own phone?

**Source ID:** C02  
**Your timing:** `00:12:47,867 --> 00:12:58,667`

## CHAPTER 5 — The unrelated arrest

### 51. BLOCKED — Narration beat

**At:** “The opening came through a different case. In”  
**Show:** BLOCKED — No distinct YouTube footage of the September car-theft surrender is verified.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 303, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G051 — unresolved source registry, not a media asset  
**Your timing:** `00:12:58,667 --> 00:13:21,000`

**Narration — unchanged:**

The opening came through a different case. In September 2024, Jahmir Moore turned himself in on unrelated charges arising from a car theft investigation. According to the Tampa Bay Times account of court records, detectives could then obtain and analyze his cellphone records. The homicide investigation had gained another source of evidence.

**Source ID:** G051  
**Your timing:** `00:12:58,667 --> 00:13:21,000`

### 52. Narration beat

**At:** “That sequence needs a legal distinction. An arrest”  
**Show:** Judge shown looking at the bench papers in detention-hearing coverage.  
**Preview:** [Teen accused of murder denied bond after escaping from custody](https://www.youtube.com/watch?v=MRoEPt81UtQ) — **approximate** source crop `00:00:04,000–00:00:07,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2024-12-18 | ARCHIVE / case context  
**Care:** No actual warrant/consent/extraction document is verified; date label must say December hearing. Reusing this original upload with this specific sampled window because: Explicitly later case-court context for a legal distinction, not the phone-search authorization. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 312, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C18  
**Your timing:** `00:13:21,000 --> 00:13:42,600`

**Narration — unchanged:**

That sequence needs a legal distinction. An arrest does not, by itself, establish authorization to search every item of digital data. The published account does not specify the warrant, consent, or other authority used here. It establishes when access became possible, without documenting the legal process behind the examination.

**Source ID:** C18  
**Your timing:** `00:13:21,000 --> 00:13:42,600`

### 53. BLOCKED — Narration beat

**At:** “The same limit applies to chain of custody”  
**Show:** BLOCKED — No chain-of-custody log, extraction demonstration or relevant case-evidence handling footage was verified.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 321, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G053 — unresolved source registry, not a media asset  
**Your timing:** `00:13:42,600 --> 00:14:03,367`

**Narration — unchanged:**

The same limit applies to chain of custody. That reporting does not identify each person who handled the device, its storage history, or the extraction procedure. Those details cannot be supplied as narrative fact. What the records describe is the material investigators attributed to Moore’s phone and associated communications.

**Source ID:** G053  
**Your timing:** `00:13:42,600 --> 00:14:03,367`

### 54. Narration beat

**At:** “Among the discoveries were lyrics stored as notes”  
**Show:** Bercaw at the podium during the report’s digital-evidence explanation.  
**Preview:** [Teen to be charged as adult for murder of 14-year-old Jevario Buie](https://www.youtube.com/watch?v=B5qzKsfKcAA) — **approximate** source crop `00:01:46,000–00:01:55,000` (9 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-05 | ARCHIVE / case context  
**Care:** No lyric quotation, graphic detail or private phone recreation. Reusing this original upload with this specific sampled window because: A matching official explanation of notes/search history, not a fabricated lyric screen. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 330, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C03  
**Your timing:** `00:14:03,367 --> 00:14:25,567`

**Narration — unchanged:**

Among the discoveries were lyrics stored as notes. They referred to Vario, Jevario’s nickname, and mentioned the location of the killing. Police said the notes also contained information they had not released publicly. That distinction concerned information unavailable through official public disclosures, rather than merely a reference to a widely reported death.

**Source ID:** C03  
**Your timing:** `00:14:03,367 --> 00:14:25,567`

### 55. BLOCKED — Narration beat

**At:** “Investigators also noted a Google search asking how”  
**Show:** BLOCKED — The homicide-search and weapon-claim exhibits have no verified safe YouTube crop here.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 339, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G055 — unresolved source registry, not a media asset  
**Your timing:** `00:14:25,567 --> 00:14:44,800`

**Narration — unchanged:**

Investigators also noted a Google search asking how many years someone could receive for homicide. In another exchange, shortly before the unrelated arrest, Moore claimed to possess the capital murder weapon. That was a claim recorded in a message; the wording alone did not establish which firearm he possessed.

**Source ID:** G055  
**Your timing:** `00:14:25,567 --> 00:14:44,800`

### 56. BLOCKED — Narration beat

**At:** “The communications added another time reference. About twenty”  
**Show:** BLOCKED — No verified display of the account-switch message or the separate non-public-detail message was located.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 347, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G056 — unresolved source registry, not a media asset  
**Your timing:** `00:14:44,800 --> 00:15:09,367`

**Narration — unchanged:**

The communications added another time reference. About twenty minutes after the shooting, Moore told a friend he would use a different Instagram account. Separately, an Instagram exchange relayed another detail about the shooting that police said had not been made public. Investigators now had communications, social media messages, notes, and search history to assess together.

**Source ID:** G056  
**Your timing:** `00:14:44,800 --> 00:15:09,367`

### 57. Narration beat

**At:** “State Attorney Chinwe Fossett would later set out”  
**Show:** Wide courtroom view during the detention-hearing report.  
**Preview:** [Teen accused of murder denied bond after escaping from custody](https://www.youtube.com/watch?v=MRoEPt81UtQ) — **approximate** source crop `00:00:28,000–00:00:34,000` (6 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2024-12-18 | ARCHIVE / case context  
**Care:** No actual motion page is shown; keep the hearing date, and do not invent who the foreground lawyer is. Reusing this original upload with this specific sampled window because: The legal setting of a written detention request; not identification of Fossett’s voice or appearance. This does not claim a new camera angle when underlying footage is republished. Scripted “Assistant” has no timed word slot; anchor at the first existing captioned word, without inventing onset. Anchor basis: cue 357, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C18  
**Your timing:** `00:15:09,367 --> 00:15:26,600`

**Narration — unchanged:**

Assistant State Attorney Chinwe Fossett would later set out the investigation in a written detention request. Her account brought these findings into the court record. It was a prosecutor’s presentation of the evidence, not a substitute for testing that evidence through the judicial process.

**Source ID:** C18  
**Your timing:** `00:15:09,367 --> 00:15:26,600`

### 58. Narration beat

**At:** “September had opened access. The murder arrest would”  
**Show:** Hannah Dineen reporting outside on the arrest-announcement night.  
**Preview:** [Teen to be charged as adult for murder of 14-year-old Jevario Buie](https://www.youtube.com/watch?v=B5qzKsfKcAA) — **approximate** source crop `00:00:19,000–00:00:27,000` (8 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-05 | ARCHIVE / case context  
**Care:** Reporter footage, not a September arrest or investigative reconstruction. Reusing this original upload with this specific sampled window because: Actual December reporting bridges the September-to-December interval. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 365, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C03  
**Your timing:** `00:15:26,600 --> 00:15:35,467`

**Narration — unchanged:**

September had opened access. The murder arrest would not come until December. What remained to be established during that interval?

**Source ID:** C03  
**Your timing:** `00:15:26,600 --> 00:15:35,467`

## CHAPTER 6 — December 4

### 59. Narration beat

**At:** “On December 4, 2024, Tampa police arrested Jahmir”  
**Show:** Moore’s police portrait in the arrest report.  
**Preview:** [15-year-old arrested for murder of Tampa teen found near railroad tracks](https://www.youtube.com/watch?v=ehT8yrPb9E0) — **approximate** source crop `00:01:24,000–00:01:27,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2024-12-05 | ARCHIVE / case context  
**Care:** Not a recording of the arrest; no stolen-firearm close-up verified. Reusing this original upload with this specific sampled window because: Names the arrested defendant with contemporaneous case reporting. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 368, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C19  
**Your timing:** `00:15:35,467 --> 00:15:58,600`

**Narration — unchanged:**

On December 4, 2024, Tampa police arrested Jahmir Moore. The U.S. Marshals Task Force assisted. Moore was fifteen. The investigation had reached an arrest, not a verdict. Officials now identified him as the teenager accused of killing Jevario Buie. The unanswered questions would move into a prosecution.

**Source ID:** C19  
**Your timing:** `00:15:35,467 --> 00:15:58,600`

### 60. Narration beat

**At:** “The announced charges were first-degree murder; carrying”  
**Show:** Wide December press conference with Bercaw and a display.  
**Preview:** [15-year-old arrested for murder of Tampa teen found near railroad tracks](https://www.youtube.com/watch?v=ehT8yrPb9E0) — **approximate** source crop `00:00:44,000–00:00:52,000` (8 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2024-12-05 | ARCHIVE / case context  
**Care:** No claim that the screen proves the recovered gun was the murder weapon. Reusing this original upload with this specific sampled window because: Contemporaneous charges announcement context. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 375, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C19  
**Your timing:** `00:15:58,600 --> 00:16:19,667`

**Narration — unchanged:**

The announced charges were first-degree murder; carrying a concealed firearm; tampering with physical evidence; minor in possession of a firearm. Police also reported finding a gun on Moore during his arrest. Chief Lee Bercaw said it had been stolen from Miami. That statement did not identify it as the murder weapon.

**Source ID:** C19  
**Your timing:** `00:15:58,600 --> 00:16:19,667`

### 61. Narration beat

**At:** “At the December 5 press conference, Bercaw said”  
**Show:** Bercaw speaking at the December briefing.  
**Preview:** [Teen to be charged as adult for murder of 14-year-old Jevario Buie](https://www.youtube.com/watch?v=B5qzKsfKcAA) — **approximate** source crop `00:01:32,000–00:01:42,000` (10 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-05 | ARCHIVE / case context  
**Care:** Different from this upload’s camera, street-sign and digital-evidence windows; retain qualifications. Reusing this original upload with this specific sampled window because: Matches the feud/uncertain-involvement statement. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 383, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C03  
**Your timing:** `00:16:19,667 --> 00:16:39,367`

**Narration — unchanged:**

At the December 5 press conference, Bercaw said Jevario had been lured to the area. He also described a feud. He did not establish Jevario’s involvement in that dispute. The motive remained under investigation. Police had named a suspect without resolving every question about why the shooting happened.

**Source ID:** C03  
**Your timing:** `00:16:19,667 --> 00:16:39,367`

### 62. Narration beat

**At:** “Hillsborough County State Attorney Suzy Lopez announced that”  
**Show:** Prosecution-office representative at the announcement podium.  
**Preview:** [Teen to be charged as adult for murder of 14-year-old Jevario Buie](https://www.youtube.com/watch?v=B5qzKsfKcAA) — **approximate** source crop `00:01:58,000–00:02:05,000` (7 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-05 | ARCHIVE / case context  
**Care:** Do not label this visible man Suzy Lopez; his exact identity is not verified here. Use office label. Reusing this original upload with this specific sampled window because: The adult-prosecution announcement itself. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 391, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C03  
**Your timing:** `00:16:39,367 --> 00:17:00,033`

**Narration — unchanged:**

Hillsborough County State Attorney Suzy Lopez announced that Moore would be charged as an adult. The decision placed the case on the adult prosecution track. She later described the interval before his arrest as 231 days. That figure measured the wait for an arrest. It did not measure a completed court case.

**Source ID:** C03  
**Your timing:** `00:16:39,367 --> 00:17:00,033`

### 63. Narration beat

**At:** “The police department’s December release summarized communications records”  
**Show:** Chief Bercaw at the announcement podium.  
**Preview:** [15-year-old arrested for murder of Tampa teen found near railroad tracks](https://www.youtube.com/watch?v=ehT8yrPb9E0) — **approximate** source crop `00:01:16,000–00:01:22,000` (6 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2024-12-05 | ARCHIVE / case context  
**Care:** Different camera framing/source passage from the charge-announcement wide shot. Reusing this original upload with this specific sampled window because: Police explanation of investigative evidence, not a jury finding. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 400, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C19  
**Your timing:** `00:17:00,033 --> 00:17:21,500`

**Narration — unchanged:**

The police department’s December release summarized communications records, social media messages, notes, and search history. Investigators said the material implicated Moore. The release also referred to information not made public. Those were the authorities’ grounds for the accusation. They were not findings delivered by a jury.

**Source ID:** C19  
**Your timing:** `00:17:00,033 --> 00:17:21,500`

### 64. Narration beat

**At:** “Jevario’s mother, Jasmine Baldwin, and his grandfather, Michael”  
**Show:** Michael Baldwin Sr. speaking with officials/family behind him.  
**Preview:** [15-year-old arrested for murder of Tampa teen found near railroad tracks](https://www.youtube.com/watch?v=ehT8yrPb9E0) — **approximate** source crop `00:01:36,000–00:01:44,000` (8 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2024-12-05 | ARCHIVE / case context  
**Care:** Exclude distressed faces or intimate gestures; source muted. Reusing this original upload with this specific sampled window because: Matches the adult family member’s response to the arrest. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 408, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C19  
**Your timing:** `00:17:21,500 --> 00:17:38,267`

**Narration — unchanged:**

Jevario’s mother, Jasmine Baldwin, and his grandfather, Michael Baldwin Sr., addressed the arrest. Their family had a named defendant. Four days after the arrest, Moore escaped custody. How had the detention system failed to contain him?

**Source ID:** C19  
**Your timing:** `00:17:21,500 --> 00:17:38,267`

## CHAPTER 7 — Eleven hours

### 65. Narration beat

**At:** “On December 8, 2024, Jahmir Moore was missing”  
**Show:** Fenced juvenile-facility exterior in follow-up reporting.  
**Preview:** [Teen accused of murder facing more charges after escaping detention center, Tampa police say](https://www.youtube.com/watch?v=OHILsLEzZ40) — **approximate** source crop `00:02:18,000–00:02:22,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-09 | ARCHIVE / case context  
**Care:** No route diagrams or private-property identification. Reusing this original upload with this specific sampled window because: Specific detention context, not a recreation of an escape mechanism. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 414, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C09  
**Your timing:** `00:17:38,267 --> 00:17:57,233`

**Narration — unchanged:**

On December 8, 2024, Jahmir Moore was missing from the Hillsborough Regional Juvenile Detention Center. Police placed the outdoor recreation period at 10:33 a.m. A head count after the group returned inside established that he had not returned from the fenced area.

**Source ID:** C09  
**Your timing:** `00:17:38,267 --> 00:17:57,233`

### 66. Narration beat

**At:** “A nearby business recorded him running west around”  
**Show:** Business-camera view of the road with a running figure, carried in the escape report.  
**Preview:** [TPD: Search underway after teen accused of killing 14-year-old Jevario Buie escaped juvenile detenti](https://www.youtube.com/watch?v=pL4PoqPMafw) — **approximate** source crop `00:00:59,000–00:01:03,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-09 | ARCHIVE / case context  
**Care:** Sampled window is brief; confirm the figure appears across the selected trim and mask other identifying detail. Reusing this original upload with this specific sampled window because: December escape surveillance, not April homicide surveillance. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 421, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C07  
**Your timing:** `00:17:57,233 --> 00:18:13,167`

**Narration — unchanged:**

A nearby business recorded him running west around 10:45 a.m. The recording established movement outside the facility, not how he crossed its boundary. Police asked anyone who saw him to call 911 and avoid approaching him.

**Source ID:** C07  
**Your timing:** `00:17:57,233 --> 00:18:13,167`

### 67. Narration beat

**At:** “Tampa police coordinated a search with agencies, including”  
**Show:** Aircraft in the sky within the search package.  
**Preview:** [TPD: Search underway after teen accused of killing 14-year-old Jevario Buie escaped juvenile detenti](https://www.youtube.com/watch?v=pL4PoqPMafw) — **approximate** source crop `00:01:19,000–00:01:23,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-09 | ARCHIVE / case context  
**Care:** Do not substitute unrelated sports or label this exact flight independently confirmed. Reusing this original upload with this specific sampled window because: Visualizes search aviation as reported; the stadium game itself is not verified footage. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 427, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C07  
**Your timing:** `00:18:13,167 --> 00:18:34,827`

**Narration — unchanged:**

Tampa police coordinated a search with agencies, including the Hillsborough County Sheriff’s Office, Florida Highway Patrol, and U.S. Marshals. Search resources included dogs and aviation support. Meanwhile, the Buccaneers hosted the Raiders at Raymond James Stadium for a one p.m. kickoff, winning 28–13.

**Source ID:** C07  
**Your timing:** `00:18:13,167 --> 00:18:34,827`

### 68. Narration beat

**At:** “Just after 9:15 p.m., Tampa police”  
**Show:** Messmer at the later recapture briefing.  
**Preview:** [Teen accused of murder facing more charges after escaping detention center, Tampa police say](https://www.youtube.com/watch?v=OHILsLEzZ40) — **approximate** source crop `00:01:20,000–00:01:28,000` (8 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-09 | ARCHIVE / case context  
**Care:** No private home/street-address image. Reusing this original upload with this specific sampled window because: Explains apprehension through later official reporting, not a camera recording of the arrest. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 433, zero-based existing word slot 8; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** C09  
**Your timing:** `00:18:34,827 --> 00:18:54,100`

**Narration — unchanged:**

Just after 9:15 p.m., Tampa police and the U.S. Marshals Task Force arrested Moore without incident. The arrest occurred on the 100 block of West Keyes Avenue, about four miles from the detention center. Surveillance of people connected to Moore had led investigators to that address.

**Source ID:** C09  
**Your timing:** `00:18:34,827 --> 00:18:54,100`

### 69. Narration beat

**At:** “Deputy Chief Ruth Cate said Moore was with”  
**Show:** Messmer at the lectern with Cate standing beside him.  
**Preview:** [ESCAPED JUVENILE INMATE CAPTURED IN TAMPA](https://www.youtube.com/watch?v=dbGceLiuZ4Y) — **approximate** source crop `00:07:29,000–00:07:43,000` (14 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** TampaPD | upload 2024-12-09 | ARCHIVE / case context  
**Care:** Later briefing; no allegation that parents were charged. Reusing this original upload with this specific sampled window because: Matches the explanation about surveillance and a residence other than the parents’ home. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 440, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C08  
**Your timing:** `00:18:54,100 --> 00:19:13,660`

**Narration — unchanged:**

Deputy Chief Ruth Cate said Moore was with his parents when officers found him. Major Patrick Messmer said the residence was not his parents’ home. Cate said the parents had cooperated and had not been charged at that point. Their presence alone did not establish how Moore escaped or who helped him.

**Source ID:** C08  
**Your timing:** `00:18:54,100 --> 00:19:13,660`

### 70. Narration beat

**At:** “Moore received a felony charge of escape from”  
**Show:** Cate speaking at the follow-up briefing.  
**Preview:** [Teen accused of murder facing more charges after escaping detention center, Tampa police say](https://www.youtube.com/watch?v=OHILsLEzZ40) — **approximate** source crop `00:01:44,000–00:01:51,000` (7 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2024-12-09 | ARCHIVE / case context  
**Care:** Not a filmed transfer to Pinellas or the statute text. Reusing this original upload with this specific sampled window because: Custody/transfer-investigation context after recapture. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 448, zero-based existing word slot 8; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** C09  
**Your timing:** `00:19:13,660 --> 00:19:38,400`

**Narration — unchanged:**

Moore received a felony charge of escape from a juvenile detention facility. Officials transferred him to a juvenile facility in Pinellas County. Police spokesperson Joneé Lewis said possible assistance remained under investigation. Florida Statute 777.03 contains a limited family exemption, not blanket immunity for relatives assisting every offense.

**Source ID:** C09  
**Your timing:** `00:19:13,660 --> 00:19:38,400`

### 71. Narration beat

**At:** “Department of Juvenile Justice spokesperson Amanda Slama announced”  
**Show:** Cate responding at the recapture briefing.  
**Preview:** [ESCAPED JUVENILE INMATE CAPTURED IN TAMPA](https://www.youtube.com/watch?v=dbGceLiuZ4Y) — **approximate** source crop `00:02:20,000–00:02:35,000` (15 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** TampaPD | upload 2024-12-09 | ARCHIVE / case context  
**Care:** This establishes uncertainty at the time, not an internal report’s final outcome. Reusing this original upload with this specific sampled window because: Matches the statement that authorities did not yet know how secure custody failed. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 459, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C08  
**Your timing:** `00:19:38,400 --> 00:20:06,167`

**Narration — unchanged:**

Department of Juvenile Justice spokesperson Amanda Slama announced a full investigation into failures or oversights surrounding the escape. The reporting did not provide its findings or establish how Moore left the secure grounds. Recapture had ended eleven hours outside custody, but it had not answered the institutional question. What would the next hearing change about where, and under what restrictions, Moore remained detained?

**Source ID:** C08  
**Your timing:** `00:19:38,400 --> 00:20:06,167`

## CHAPTER 8 — No bond; the motive on the record

### 72. Narration beat

**At:** “On December 17, 2024, Jahmir Moore appeared before”  
**Show:** Moore, a judge, and the wide hearing courtroom appear in the station sequence.  
**Preview:** [Teen accused of murder denied bond after escaping from custody](https://www.youtube.com/watch?v=MRoEPt81UtQ) — **approximate** source crop `00:00:00,000–00:00:13,000` (13 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2024-12-18 | ARCHIVE / case context  
**Care:** Do not equate each pictured frame with the exact spoken ruling; upload is Dec 18, reporting the Dec 17 hearing. Reusing this original upload with this specific sampled window because: Actual no-bond case coverage; matches the hearing beat. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 470, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C18  
**Your timing:** `00:20:06,167 --> 00:20:28,233`

**Narration — unchanged:**

On December 17, 2024, Jahmir Moore appeared before Hillsborough Circuit Judge J. Logan Murphy for a pretrial detention hearing. Assistant State Attorney Chinwe Fossett had filed a written request for detention. The defense did not contest it. Murphy ordered Moore held without bail in the adult Hillsborough County Jail.

**Source ID:** C18  
**Your timing:** `00:20:06,167 --> 00:20:28,233`

### 73. Narration beat

**At:** “That ruling settled his custody status, not his”  
**Show:** Moore in custody clothing during the hearing report.  
**Preview:** [Teen accused of murder denied bond after escaping from custody](https://www.youtube.com/watch?v=MRoEPt81UtQ) — **approximate** source crop `00:00:34,000–00:00:41,000` (7 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2024-12-18 | ARCHIVE / case context  
**Care:** Not the September trial or a sentencing shot. Reusing this original upload with this specific sampled window because: Immediate detention status, distinct from guilt. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 478, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C18  
**Your timing:** `00:20:28,233 --> 00:20:46,867`

**Narration — unchanged:**

That ruling settled his custody status, not his guilt. The request also supplied a prosecution account of the investigation. Its significance extended beyond detention: the public could now examine an alleged motive behind a killing that officials had previously described without an explanation.

**Source ID:** C18  
**Your timing:** `00:20:28,233 --> 00:20:46,867`

### 74. BLOCKED — Narration beat

**At:** “The prosecution traced the dispute to a reported”  
**Show:** BLOCKED — No verified YouTube footage of the alleged March incident or Claymore scene was found.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 487, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G074 — unresolved source registry, not a media asset  
**Your timing:** `00:20:46,867 --> 00:21:07,600`

**Narration — unchanged:**

The prosecution traced the dispute to a reported shooting on March 24 at the Claymore Crossing Apartments in the Mango area. No one was hit. No police report documented that incident. The allegation therefore required careful attribution; its place in the prosecution’s theory did not make every claim about it established.

**Source ID:** G074  
**Your timing:** `00:20:46,867 --> 00:21:07,600`

### 75. BLOCKED — Narration beat

**At:** “Court records described an Instagram group conversation March”  
**Show:** BLOCKED — No verified source window showing the March group-chat exhibit was located.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 495, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G075 — unresolved source registry, not a media asset  
**Your timing:** `00:21:07,600 --> 00:21:28,033`

**Narration — unchanged:**

Court records described an Instagram group conversation March 25. Moore and others discussed someone they believed responsible for targeting their friend. Moore wrote that he would set em up and suggested robbery. The account reflected their suspicion about another teenager, not a judicial finding that the teenager had committed that shooting.

**Source ID:** G075  
**Your timing:** `00:21:07,600 --> 00:21:28,033`

### 76. Narration beat

**At:** “Later trial reporting supplied the meeting sequence. Moore”  
**Show:** Police surveillance reproduced in sentencing reporting.  
**Preview:** [Florida teen gets 55 years in 15-year-old's murder](https://www.youtube.com/watch?v=zyKDsEekos4) — **approximate** source crop `00:01:20,000–00:01:28,000` (8 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2026-10-17 | ARCHIVE / case context  
**Care:** Republished April surveillance is not a new camera angle; call/departure evidence remains unshown. Reusing this original upload with this specific sampled window because: Actual meeting/company context, not footage of Norton’s phone call. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 504, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C17  
**Your timing:** `00:21:28,033 --> 00:21:51,600`

**Narration — unchanged:**

Later trial reporting supplied the meeting sequence. Moore contacted Curtis Norton through Instagram about spending time together and shooting dice. Jevario joined the arrangements through Norton’s account, according to the prosecution. The three met on April 17. At about 3:32 p.m., Norton’s father called him home, and Norton left. Jevario stayed.

**Source ID:** C17  
**Your timing:** `00:21:28,033 --> 00:21:51,600`

### 77. BLOCKED — Narration beat

**At:** “The allegations would meet a competing explanation. Prosecutors”  
**Show:** BLOCKED — No original YouTube trial opening/explanation by Sinardi was verified.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 512, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G077 — unresolved source registry, not a media asset  
**Your timing:** `00:21:51,600 --> 00:22:11,233`

**Narration — unchanged:**

The allegations would meet a competing explanation. Prosecutors characterized the encounter as a revenge plot. Defense attorney Scott Sinardi would argue that Moore faced a setup and acted in self-defense. Those opposing accounts belonged to the trial ahead, not findings made at this detention hearing.

**Source ID:** G077  
**Your timing:** `00:21:51,600 --> 00:22:11,233`

### 78. Narration beat

**At:** “Keep following this case, and subscribe as we”  
**Show:** Counsel table and papers in the case’s later court report.  
**Preview:** [Sentencing is planned for Jahmir Moore on Friday](https://www.youtube.com/watch?v=MrRx2a1NT8s) — **approximate** source crop `00:00:07,000–00:00:10,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2026-10-16 | ARCHIVE / case context  
**Care:** Do not identify a particular lawyer from this sample. Reusing this original upload with this specific sampled window because: Transition into courtroom testing of evidence. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 519, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C21  
**Your timing:** `00:22:11,233 --> 00:22:26,967`

**Narration — unchanged:**

Keep following this case, and subscribe as we examine how the evidence was challenged, not merely announced. The next stage tests explanations against testimony and the burden of proof. Which account would the jury accept when the case reached trial?

**Source ID:** C21  
**Your timing:** `00:22:11,233 --> 00:22:26,967`

## CHAPTER 9 — Two stories in one courtroom

### 79. Narration beat

**At:** “Trial began in Hillsborough County on September 1”  
**Show:** Wide case courtroom view with bench and counsel tables.  
**Preview:** [17-year-old found guilty in 2024 murder of Tampa teen](https://www.youtube.com/watch?v=ViL-3fyD5iA) — **approximate** source crop `00:00:19,000–00:00:22,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2026-09-04 | ARCHIVE / case context  
**Care:** Not the opening minute of trial or a certified verdict-return shot. Reusing this original upload with this specific sampled window because: Trial-case setting from later verdict reporting. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 525, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C10  
**Your timing:** `00:22:26,967 --> 00:22:47,267`

**Narration — unchanged:**

Trial began in Hillsborough County on September 1, 2026. Jahmir Moore was seventeen and being tried as an adult. The dispute was no longer identity. Jurors would have to decide whether the shooting was a planned killing, as prosecutors alleged, or an act of self-defense, as Moore’s attorneys maintained.

**Source ID:** C10  
**Your timing:** `00:22:26,967 --> 00:22:47,267`

### 80. BLOCKED — Narration beat

**At:** “Assistant State Attorney Chinwe Fossett opened with an”  
**Show:** BLOCKED — No verified YouTube window of Fossett’s opening/slides was located.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 533, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G080 — unresolved source registry, not a media asset  
**Your timing:** `00:22:47,267 --> 00:23:08,167`

**Narration — unchanged:**

Assistant State Attorney Chinwe Fossett opened with an eighty minute presentation using more than one hundred exhibit slides. She argued that revenge directed at Curtis Norton had placed Jevario in danger. Her description of Jevario as collateral damage expressed the prosecution’s theory, not a finding by the court.

**Source ID:** G080  
**Your timing:** `00:22:47,267 --> 00:23:08,167`

### 81. BLOCKED — Narration beat

**At:** “Defense attorney Scott Sinardi offered a different interpretation”  
**Show:** BLOCKED — No verified YouTube window of Sinardi’s opening/medical-examiner argument was located.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 541, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G081 — unresolved source registry, not a media asset  
**Your timing:** `00:23:08,167 --> 00:23:28,767`

**Narration — unchanged:**

Defense attorney Scott Sinardi offered a different interpretation. He described a decision made within seconds during a struggle over a gun. He said Moore believed he was facing a setup. He also pointed jurors toward anticipated medical examiner testimony when challenging the prosecution’s characterization of the shooting.

**Source ID:** G081  
**Your timing:** `00:23:08,167 --> 00:23:28,767`

### 82. BLOCKED — Narration beat

**At:** “The state presented surveillance beginning near Moore’s home”  
**Show:** BLOCKED — No verified Belara Lakes/route exhibit crop was located; no unrelated apartment footage substituted.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 550, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G082 — unresolved source registry, not a media asset  
**Your timing:** `00:23:28,767 --> 00:23:49,987`

**Narration — unchanged:**

The state presented surveillance beginning near Moore’s home at the Belara Lakes Apartments off West Waters Avenue. The exhibits connected the group’s movements with the separation. Their courtroom purpose was evidentiary: prosecutors asked jurors to evaluate the recorded sequence alongside testimony, rather than accept the defense account in isolation.

**Source ID:** G082  
**Your timing:** `00:23:28,767 --> 00:23:49,987`

### 83. BLOCKED — Narration beat

**At:** “Norton testified that neither he nor Jevario carried”  
**Show:** BLOCKED — No verified Norton testimony crop was found; no young witness is identified by inference.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 559, zero-based existing word slot 4; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** G083 — unresolved source registry, not a media asset  
**Your timing:** `00:23:49,987 --> 00:24:12,100`

**Narration — unchanged:**

Norton testified that neither he nor Jevario carried a weapon that day. He denied involvement in the earlier shooting alleged by the defense. He also read private messages in which Moore denied responsibility for Jevario’s death. Fossett emphasized that those denials contained no explanation involving a setup or self-defense.

**Source ID:** G083  
**Your timing:** `00:23:49,987 --> 00:24:12,100`

### 84. BLOCKED — Narration beat

**At:** “The prosecution introduced social media posts, messages, and”  
**Show:** BLOCKED — No safe verified recording/exhibit crop is selected; the crime-scene photograph and gallery distress are intentionally not shown.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 567, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G084 — unresolved source registry, not a media asset  
**Your timing:** `00:24:12,100 --> 00:24:33,267`

**Narration — unchanged:**

The prosecution introduced social media posts, messages, and a recording Moore had composed. These exhibits became part of its argument about his conduct and knowledge after the shooting. A crime scene photograph was also displayed. A gallery member left the courtroom when it appeared; the image itself needs no description here.

**Source ID:** G084  
**Your timing:** `00:24:12,100 --> 00:24:33,267`

### 85. BLOCKED — Narration beat

**At:** “Moore took the stand and admitted firing the”  
**Show:** BLOCKED — No original YouTube window of Moore testifying was verified; a defendant seated silently is not testimony footage.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 575, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G085 — unresolved source registry, not a media asset  
**Your timing:** `00:24:33,267 --> 00:24:54,300`

**Narration — unchanged:**

Moore took the stand and admitted firing the shots. He testified that he feared for his life. He described seeing Jevario reach toward his waistband and claimed a struggle followed. He said fear explained his failure to call 911. He attributed his later online posts to wanting to appear cool.

**Source ID:** G085  
**Your timing:** `00:24:33,267 --> 00:24:54,300`

### 86. BLOCKED — Narration beat

**At:** “Fossett challenged that explanation with the surveillance and”  
**Show:** BLOCKED — No verified lone-walk/phone-browsing courtroom exhibit or rebuttal crop was found.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 582, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G086 — unresolved source registry, not a media asset  
**Your timing:** `00:24:54,300 --> 00:25:14,767`

**Narration — unchanged:**

Fossett challenged that explanation with the surveillance and the physical evidence. Footage showed Moore walking home slowly while looking at his phone. She argued that no defensive wounds were found on him. First responders had found no weapon on Jevario. The lead detective confirmed no report of the alleged earlier shooting.

**Source ID:** G086  
**Your timing:** `00:24:54,300 --> 00:25:14,767`

### 87. BLOCKED — Narration beat

**At:** “The prosecutor questioned the claimed concealed gun by”  
**Show:** BLOCKED — No verified safe shorts/exhibit or medical-evidence window was located.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 590, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G087 — unresolved source registry, not a media asset  
**Your timing:** `00:25:14,767 --> 00:25:34,533`

**Narration — unchanged:**

The prosecutor questioned the claimed concealed gun by pointing to Jevario’s shorts and their shallow pockets. Medical evidence had been presented during the trial, but its interpretation remained contested. Jurors had to assess the testimony against the exhibits, not treat either attorney’s argument as evidence itself.

**Source ID:** G087  
**Your timing:** `00:25:14,767 --> 00:25:34,533`

### 88. Narration beat

**At:** “After about four hours of deliberation, the jury”  
**Show:** Station news anchor reporting the verdict.  
**Preview:** [17-year-old found guilty in 2024 murder of Tampa teen](https://www.youtube.com/watch?v=ViL-3fyD5iA) — **approximate** source crop `00:00:00,000–00:00:04,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2026-09-04 | ARCHIVE / case context  
**Care:** No claim this is the moment jurors returned. Reusing this original upload with this specific sampled window because: An actual verdict update, not recreated jury audio. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 597, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C10  
**Your timing:** `00:25:34,533 --> 00:25:48,900`

**Narration — unchanged:**

After about four hours of deliberation, the jury found Moore guilty as charged, including first-degree murder and the accompanying firearm and evidence offenses. Sentencing was scheduled for October 16.

**Source ID:** C10  
**Your timing:** `00:25:34,533 --> 00:25:48,900`

### 89. Narration beat

**At:** “The family said the jury got it right”  
**Show:** Jevario’s car portrait in sentencing reporting.  
**Preview:** [Florida teen gets 55 years in 15-year-old's murder](https://www.youtube.com/watch?v=zyKDsEekos4) — **approximate** source crop `00:02:20,000–00:02:23,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2026-10-17 | ARCHIVE / case context  
**Care:** Not footage of the family’s verdict reaction; blur the child in the background and avoid later family distress. Reusing this original upload with this specific sampled window because: Victim-focused ending to trial outcome. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 602, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C17  
**Your timing:** `00:25:48,900 --> 00:26:01,600`

**Narration — unchanged:**

The family said the jury got it right, while acknowledging that nobody had won. The remaining decision belonged to the judge. Moore faced forty years to life. Which sentence would follow?

**Source ID:** C17  
**Your timing:** `00:25:48,900 --> 00:26:01,600`

## CHAPTER 10 — Fifty-five years

### 90. Narration beat

**At:** “On October 16, 2026, Hillsborough Circuit Judge Lyann”  
**Show:** Moore in custody clothing approaching/standing before the sentencing bench.  
**Preview:** [Florida teen gets 55 years in 15-year-old's murder](https://www.youtube.com/watch?v=zyKDsEekos4) — **approximate** source crop `00:00:08,000–00:00:14,000` (6 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2026-10-17 | ARCHIVE / case context  
**Care:** Not an April or December event. Reusing this original upload with this specific sampled window because: Actual sentencing-hearing context. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 607, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C17  
**Your timing:** `00:26:01,600 --> 00:26:22,320`

**Narration — unchanged:**

On October 16, 2026, Hillsborough Circuit Judge Lyann Goudie conducted a sentencing hearing lasting ninety minutes. Moore faced forty years to life. Jevario’s family requested life imprisonment. The judge had to weigh the crime alongside the significance of Moore’s age when he committed it.

**Source ID:** C17  
**Your timing:** `00:26:01,600 --> 00:26:22,320`

### 91. Narration beat

**At:** “Goudie said she could not pronounce life on”  
**Show:** Judge Goudie at the sentencing bench.  
**Preview:** [Florida teen gets 55 years in 15-year-old's murder](https://www.youtube.com/watch?v=zyKDsEekos4) — **approximate** source crop `00:01:04,000–00:01:08,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2026-10-17 | ARCHIVE / case context  
**Care:** Source muted; no audio claim until reviewed. Reusing this original upload with this specific sampled window because: Matches the judge’s assessment, without fabricating a lip-synced quotation. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 613, zero-based existing word slot 8; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** C17  
**Your timing:** `00:26:22,320 --> 00:26:42,667`

**Narration — unchanged:**

Goudie said she could not pronounce life on this seventeen year old. She did not consider him a monster. Youth and immaturity weighed in her decision. Research and case law required consideration of development, maturity, risk, and remorse. An adult convicted of this offense would face mandatory life without parole.

**Source ID:** C17  
**Your timing:** `00:26:22,320 --> 00:26:42,667`

### 92. Narration beat

**At:** “The sentence was fifty-five years, with judicial”  
**Show:** Judge Goudie at the bench in the sentencing update.  
**Preview:** [Jahmir Moore sentenced in murder of Tampa 14-year-old](https://www.youtube.com/watch?v=YIDP32FMSho) — **approximate** source crop `00:00:16,000–00:00:19,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2026-10-16 | ARCHIVE / case context  
**Care:** The source is a news package, not proof that this short shot contains the exact sentence pronouncement. Reusing this original upload with this specific sampled window because: Judicial sentencing context, not a future release hearing. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 622, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C11  
**Your timing:** `00:26:42,667 --> 00:27:04,767`

**Narration — unchanged:**

The sentence was fifty-five years, with judicial review and possible release after twenty-five. Concurrent penalties included five years for escape and 364 days for resisting arrest. Concurrent meant those terms ran alongside the principal sentence. Review offered a judicial decision, not a scheduled release date.

**Source ID:** C11  
**Your timing:** `00:26:42,667 --> 00:27:04,767`

### 93. BLOCKED — Narration beat

**At:** “The defense mitigation memorandum described separated parents and”  
**Show:** BLOCKED — No clean verified mitigation memorandum or supporting biographical exhibit is available on YouTube.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 630, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G093 — unresolved source registry, not a media asset  
**Your timing:** `00:27:04,767 --> 00:27:24,067`

**Narration — unchanged:**

The defense mitigation memorandum described separated parents and a cousin’s death in an accidental shooting. Moore had earned mostly Fs in ninth grade at Chamberlain High School. He had an ADHD diagnosis and had refused medication. He had earned money through lawn mowing and pressure washing work.

**Source ID:** G093  
**Your timing:** `00:27:04,767 --> 00:27:24,067`

### 94. Narration beat

**At:** “Jevario’s mother, Jasmine Baldwin, his sister, and grandparents”  
**Show:** Wide sentencing courtroom with an adult man at the lectern facing the judge.  
**Preview:** [Florida teen gets 55 years in 15-year-old's murder](https://www.youtube.com/watch?v=zyKDsEekos4) — **approximate** source crop `00:00:40,000–00:01:00,000` (20 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2026-10-17 | ARCHIVE / case context  
**Care:** Confirm identity by listening before labelling him by name; no child testimony, no prolonged close-up distress. Reusing this original upload with this specific sampled window because: Adult family sentencing-statement context. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 638, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C17  
**Your timing:** `00:27:24,067 --> 00:27:49,020`

**Narration — unchanged:**

Jevario’s mother, Jasmine Baldwin, his sister, and grandparents JoQuetta Winters and Michael Baldwin Sr. addressed the court. His grandfather urged accountability and personal change. Moore’s mother, Tabia Aska, described her son as a beautiful soul and rejected the label monster. Moore offered a barely audible apology. Goudie found it hollow.

**Source ID:** C17  
**Your timing:** `00:27:24,067 --> 00:27:49,020`

### 95. BLOCKED — Narration beat

**At:** “Florida Statute 921.1402 provides qualifying juvenile offenders”  
**Show:** BLOCKED — No verified YouTube source presenting the applicable statute/review factors accurately was located.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 647, zero-based existing word slot 8; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** G095 — unresolved source registry, not a media asset  
**Your timing:** `00:27:49,020 --> 00:28:15,633`

**Narration — unchanged:**

Florida Statute 921.1402 provides qualifying juvenile offenders a sentence review after twenty-five years. The court must consider maturity and rehabilitation. Continuing risk to society also matters. The victim’s next of kin may be heard. Sincere, sustained remorse and the offender’s development at the time of the crime are statutory considerations.

**Source ID:** G095  
**Your timing:** `00:27:49,020 --> 00:28:15,633`

### 96. Narration beat

**At:** “Goudie said future release would depend on Moore’s”  
**Show:** Judge Goudie speaking at the bench.  
**Preview:** [Jahmir Moore sentenced in murder of Tampa 14-year-old](https://www.youtube.com/watch?v=YIDP32FMSho) — **approximate** source crop `00:00:28,000–00:00:31,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2026-10-16 | ARCHIVE / case context  
**Care:** Different passage/framing from the earlier sentencing crop; no lip-sync attribution while muted. Reusing this original upload with this specific sampled window because: Closes the sentencing decision with the actual case judge, not an imagined future review. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 658, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C11  
**Your timing:** `00:28:15,633 --> 00:28:36,720`

**Narration — unchanged:**

Goudie said future release would depend on Moore’s prison conduct and acceptance of responsibility. The judgment imposed punishment while preserving an opportunity to demonstrate change. Eligibility alone would not establish rehabilitation or fitness to reenter society. What would that review require him to prove?

**Source ID:** C11  
**Your timing:** `00:28:15,633 --> 00:28:36,720`

## CHAPTER 11 — What the record shows

### 97. Narration beat

**At:** “The record has an outcome, but an outcome”  
**Show:** Wide courtroom after the adult lectern sequence.  
**Preview:** [Florida teen gets 55 years in 15-year-old's murder](https://www.youtube.com/watch?v=zyKDsEekos4) — **approximate** source crop `00:02:32,000–00:02:35,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2026-10-17 | ARCHIVE / case context  
**Care:** Do not count this as new evidence or a future hearing. Reusing this original upload with this specific sampled window because: Closing legal-stage context, not a new finding. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 666, zero-based existing word slot 6; JSON segment µs / 1000 + existing word offset ms.  
**Source ID:** C17  
**Your timing:** `00:28:36,720 --> 00:28:55,500`

**Narration — unchanged:**

The record has an outcome, but an outcome is not the same as an answer to every question. A conviction resolves criminal responsibility through a legal process. It does not turn every suspicion into fact, or make every unanswered institutional question disappear once punishment has been imposed.

**Source ID:** C17  
**Your timing:** `00:28:36,720 --> 00:28:55,500`

### 98. Narration beat

**At:** “This case leaves a documented chain: an emergency”  
**Show:** Case surveillance carried in the later news update.  
**Preview:** [Sentencing is planned for Jahmir Moore on Friday](https://www.youtube.com/watch?v=MrRx2a1NT8s) — **approximate** source crop `00:00:15,000–00:00:19,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** 10 Tampa Bay News | upload 2026-10-16 | ARCHIVE / case context  
**Care:** This is the same underlying April surveillance, not new cameras or operational footage of every listed stage. Reusing this original upload with this specific sampled window because: An existing evidence image for the documented chain. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 675, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C21  
**Your timing:** `00:28:55,500 --> 00:29:17,900`

**Narration — unchanged:**

This case leaves a documented chain: an emergency call, cameras, phone evidence, an arrest, an escape, a detention motion, a trial, and a sentence. Each stage produced a kind of record. Their value lies in what they establish together, without asking any single document to explain everything.

**Source ID:** C21  
**Your timing:** `00:28:55,500 --> 00:29:17,900`

### 99. Narration beat

**At:** “At arrest, officials said the motive remained unclear”  
**Show:** Chief Bercaw in a close view at the December briefing.  
**Preview:** [15-year-old arrested for murder of Tampa teen found near railroad tracks](https://www.youtube.com/watch?v=ehT8yrPb9E0) — **approximate** source crop `00:00:32,000–00:00:35,000` (3 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** FOX 13 Tampa Bay | upload 2024-12-05 | ARCHIVE / case context  
**Care:** Distinct close view rather than the display-wide shot used earlier; no assertion that this contains every quoted phrase. Reusing this original upload with this specific sampled window because: Returns to the contemporaneous official position, explicitly labelled as historical. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 684, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C19  
**Your timing:** `00:29:17,900 --> 00:29:36,867`

**Narration — unchanged:**

At arrest, officials said the motive remained unclear. The prosecution later presented a revenge theory, and the defense disputed it. The verdict settled the charge before the jury. It should not be described as a finding about every allegation surrounding the earlier dispute or everyone connected to it.

**Source ID:** C19  
**Your timing:** `00:29:17,900 --> 00:29:36,867`

### 100. Narration beat

**At:** “The escape leaves another boundary. Public reporting described”  
**Show:** Cate at the outdoor escape-search briefing, police car behind her.  
**Preview:** [Tampa police provide update on teen who escaped from detention center](https://www.youtube.com/watch?v=01cwmCRk9s4) — **approximate** source crop `00:02:05,000–00:02:20,000` (15 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** WFLA News Channel 8 | upload 2024-12-08 | ARCHIVE / case context  
**Care:** Dec 8 search briefing, not the next-day indoor recapture briefing. Reusing this original upload with this specific sampled window because: Contemporaneous institutional uncertainty rather than invented DJJ findings. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 691, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C20  
**Your timing:** `00:29:36,867 --> 00:29:58,967`

**Narration — unchanged:**

The escape leaves another boundary. Public reporting described an investigation into how secure custody failed. The sources reviewed for this account do not supply its findings. That absence supports a limited statement: the explanation remains missing from this account’s public record, not proof that no internal findings exist.

**Source ID:** C20  
**Your timing:** `00:29:36,867 --> 00:29:58,967`

### 101. BLOCKED — Narration beat

**At:** “The sentence also creates a distinction between eligibility”  
**Show:** BLOCKED — No verified statute/review explainer window matches the application-and-counsel procedure.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 700, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G101 — unresolved source registry, not a media asset  
**Your timing:** `00:29:58,967 --> 00:30:23,067`

**Narration — unchanged:**

The sentence also creates a distinction between eligibility and entitlement to freedom. Under Florida’s review statute, an eligible offender must apply to the sentencing court. Counsel is available, with appointed representation for someone unable to afford an attorney. A hearing then addresses whether modification is justified, rather than shortening imprisonment.

**Source ID:** G101  
**Your timing:** `00:29:58,967 --> 00:30:23,067`

### 102. BLOCKED — Narration beat

**At:** “If rehabilitation and fitness to reenter society are”  
**Show:** BLOCKED — No verified source window matches conditional modification/probation and relatives’ participation rules.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 711, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G102 — unresolved source registry, not a media asset  
**Your timing:** `00:30:23,067 --> 00:30:49,433`

**Narration — unchanged:**

If rehabilitation and fitness to reenter society are established, the statute requires modification and at least five years of probation. If they are not established, the court must explain its refusal in writing. The victim’s relatives may participate. Their absence cannot itself count against modification. Responsibility, conduct, and demonstrated change remain consequential.

**Source ID:** G102  
**Your timing:** `00:30:23,067 --> 00:30:49,433`

### 103. Narration beat

**At:** “For Jevario’s family, sentencing ended a legal stage”  
**Show:** Michael Baldwin Sr. in the earlier outdoor interview.  
**Preview:** [14-year-old Tampa Boy will be laid to rest Saturday, as family searches for answers](https://www.youtube.com/watch?v=D28FFVJXLNw) — **approximate** source crop `00:02:04,000–00:02:08,000` (4 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** WFLA News Channel 8 | upload 2024-05-03 | ARCHIVE / case context  
**Care:** Mute; no grief quotation, child distress or generic prison B-roll from elsewhere in this report. Reusing this original upload with this specific sampled window because: An earlier adult family perspective, date-labelled rather than presented as post-sentencing speech. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 721, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C16  
**Your timing:** `00:30:49,433 --> 00:31:07,900`

**Narration — unchanged:**

For Jevario’s family, sentencing ended a legal stage, not the loss they described. Their statements belong to that distinction. A judgment can determine punishment and preserve their opportunity to be heard again. It cannot restore the person whose absence brought them into court.

**Source ID:** C16  
**Your timing:** `00:30:49,433 --> 00:31:07,900`

### 104. BLOCKED — Narration beat

**At:** “As of November 4, 2026, the reporting reviewed”  
**Show:** BLOCKED — No November appellate docket/status video was verified; a sentencing report is not evidence that no appeal was filed.  
**Preview:** **BLOCKED — no verified source range; no substitute assigned.**  
**Label:** No source label until a genuine YouTube source is approved.  
**Care:** Please supply a clean original YouTube locator or approve a separately described context treatment. No automatic substitution, freeze, stock or synthetic screen. Anchor basis: cue 728, zero-based existing word slot 0; SRT cue start.  
**Source ID:** G104 — unresolved source registry, not a media asset  
**Your timing:** `00:31:07,900 --> 00:31:29,233`

**Narration — unchanged:**

As of November 4, 2026, the reporting reviewed here contains no reported appeal. That is not confirmation that none has been filed. Sentencing closes this trial stage while leaving lawful review available. Any account should identify new filings before claiming that the procedural position has changed.

**Source ID:** G104  
**Your timing:** `00:31:07,900 --> 00:31:29,233`

### 105. Narration beat

**At:** “Subscribe for the next documented case. Thank you”  
**Show:** Jevario’s memorial/name graphics shown in the family interview report.  
**Preview:** [14-year-old Tampa Boy will be laid to rest Saturday, as family searches for answers](https://www.youtube.com/watch?v=D28FFVJXLNw) — **approximate** source crop `00:02:48,000–00:02:55,000` (7 s); timestamped storyboard samples inspected, continuous edges/audio unreviewed.  
**Label:** WFLA News Channel 8 | upload 2024-05-03 | ARCHIVE / case context  
**Care:** These are existing memorial graphics in the source; do not add a freeze, private information or unrelated end card. Reusing this original upload with this specific sampled window because: Victim-focused sign-off rather than another anchor opening. This does not claim a new camera angle when underlying footage is republished. Anchor basis: cue 736, zero-based existing word slot 0; SRT cue start.  
**Source ID:** C16  
**Your timing:** `00:31:29,233 --> 00:31:37,100`

**Narration — unchanged:**

Subscribe for the next documented case. Thank you for watching. This was Jevario Buie’s case, told through the record.

**Source ID:** C16  
**Your timing:** `00:31:29,233 --> 00:31:37,100`

## Loop-Join Transition Table — OFF by default

These are joins **inside existing placements**, not extra scenes. Choose/apply/change/remove at will; normal cut is default. 200 ms is a suggestion, not an applied effect. Join positions depend on confirming the approximate crop length. If an approved trim changes, obtain approval and recalculate the internal joins without moving the outer scene edges.

| Placement | Existing source crop | Conditional repeat-start project times | Optional effect / safeguards |
|---|---|---|---|

| 2 | C01 ~`00:01:44,000–00:01:52,000` | `00:00:09,800`; `00:00:17,800` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 5 | C01 ~`00:01:28,000–00:01:32,000` | `00:00:46,700`; `00:00:50,700`; `00:00:54,700` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 9 | C19 ~`00:00:16,000–00:00:19,000` | `00:01:32,100`; `00:01:35,100`; `00:01:38,100`; `00:01:41,100` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 10 | C06 ~`00:00:40,000–00:00:43,000` | `00:01:45,267`; `00:01:48,267`; `00:01:51,267`; `00:01:54,267` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 11 | C02 ~`00:00:33,000–00:00:37,000` | `00:01:59,000` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 12 | C15 ~`00:01:48,000–00:01:56,000` | `00:02:10,600` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 13 | C21 ~`00:00:22,000–00:00:24,000` | `00:02:15,067` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 14 | C09 ~`00:02:16,000–00:02:20,000` | `00:02:20,267`; `00:02:24,267`; `00:02:28,267` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 15 | C18 ~`00:00:00,000–00:00:03,000` | `00:02:33,500`; `00:02:36,500`; `00:02:39,500`; `00:02:42,500` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 16 | C14 ~`00:00:36,000–00:00:39,000` | `00:02:46,233`; `00:02:49,233`; `00:02:52,233` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 17 | C17 ~`00:02:24,000–00:02:32,000` | `00:03:02,767` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 19 | C01 ~`00:00:32,000–00:00:35,000` | `00:03:11,600` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 20 | C15 ~`00:01:56,000–00:02:00,000` | `00:03:15,867`; `00:03:19,867` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 21 | C06 ~`00:02:08,000–00:02:12,000` | `00:03:27,787` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 22 | C02 ~`00:00:20,000–00:00:24,000` | `00:03:32,647`; `00:03:36,647` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 23 | C02 ~`00:00:25,000–00:00:28,000` | `00:03:42,200`; `00:03:45,200`; `00:03:48,200`; `00:03:51,200`; `00:03:54,200`; `00:03:57,200`; `00:04:00,200`; `00:04:03,200` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 24 | C01 ~`00:00:56,000–00:00:59,000` | `00:04:07,740`; `00:04:10,740`; `00:04:13,740`; `00:04:16,740`; `00:04:19,740`; `00:04:22,740`; `00:04:25,740` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 25 | C15 ~`00:00:24,000–00:00:27,000` | `00:04:29,100`; `00:04:32,100`; `00:04:35,100`; `00:04:38,100`; `00:04:41,100`; `00:04:44,100` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 26 | C04 ~`00:00:01,000–00:00:07,000` | `00:04:52,667`; `00:04:58,667`; `00:05:04,667`; `00:05:10,667` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 28 | C05 ~`00:02:25,000–00:02:31,000` | `00:05:41,667`; `00:05:47,667` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 29 | C03 ~`00:01:22,000–00:01:27,000` | `00:05:58,000`; `00:06:03,000` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 30 | C02 ~`00:00:03,000–00:00:11,000` | `00:06:11,200`; `00:06:19,200` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 31 | C15 ~`00:02:00,000–00:02:04,000` | `00:06:29,633`; `00:06:33,633`; `00:06:37,633`; `00:06:41,633`; `00:06:45,633`; `00:06:49,633` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 32 | C12 ~`00:01:12,000–00:01:16,000` | `00:06:54,167`; `00:06:58,167`; `00:07:02,167`; `00:07:06,167` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 34 | C06 ~`00:01:03,000–00:01:10,000` | `00:07:36,127`; `00:07:43,127`; `00:07:50,127` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 35 | C06 ~`00:01:28,000–00:01:34,000` | `00:07:59,167`; `00:08:05,167`; `00:08:11,167` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 36 | C14 ~`00:01:48,000–00:01:56,000` | `00:08:19,567` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 37 | C05 ~`00:02:11,000–00:02:25,000` | `00:08:37,567` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 38 | C04 ~`00:00:08,000–00:00:13,000` | `00:08:47,967`; `00:08:52,967`; `00:08:57,967`; `00:09:02,967` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 39 | C06 ~`00:01:40,000–00:01:48,000` | `00:09:11,033`; `00:09:19,033`; `00:09:27,033` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 40 | C03 ~`00:01:04,000–00:01:07,000` | `00:09:30,700`; `00:09:33,700`; `00:09:36,700`; `00:09:39,700`; `00:09:42,700`; `00:09:45,700`; `00:09:48,700` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 41 | C05 ~`00:02:36,000–00:02:45,000` | `00:09:59,467`; `00:10:08,467` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 42 | C06 ~`00:00:44,000–00:00:50,000` | `00:10:16,433`; `00:10:22,433` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 43 | C06 ~`00:01:56,000–00:01:59,000` | `00:10:31,100`; `00:10:34,100`; `00:10:37,100`; `00:10:40,100` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 48 | C04 ~`00:00:13,000–00:00:17,000` | `00:12:09,900`; `00:12:13,900`; `00:12:17,900`; `00:12:21,900`; `00:12:25,900` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 50 | C02 ~`00:00:38,000–00:00:41,000` | `00:12:50,867`; `00:12:53,867`; `00:12:56,867` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 52 | C18 ~`00:00:04,000–00:00:07,000` | `00:13:24,000`; `00:13:27,000`; `00:13:30,000`; `00:13:33,000`; `00:13:36,000`; `00:13:39,000`; `00:13:42,000` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 54 | C03 ~`00:01:46,000–00:01:55,000` | `00:14:12,367`; `00:14:21,367` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 57 | C18 ~`00:00:28,000–00:00:34,000` | `00:15:15,367`; `00:15:21,367` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 58 | C03 ~`00:00:19,000–00:00:27,000` | `00:15:34,600` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 59 | C19 ~`00:01:24,000–00:01:27,000` | `00:15:38,467`; `00:15:41,467`; `00:15:44,467`; `00:15:47,467`; `00:15:50,467`; `00:15:53,467`; `00:15:56,467` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 60 | C19 ~`00:00:44,000–00:00:52,000` | `00:16:06,600`; `00:16:14,600` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 61 | C03 ~`00:01:32,000–00:01:42,000` | `00:16:29,667` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 62 | C03 ~`00:01:58,000–00:02:05,000` | `00:16:46,367`; `00:16:53,367` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 63 | C19 ~`00:01:16,000–00:01:22,000` | `00:17:06,033`; `00:17:12,033`; `00:17:18,033` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 64 | C19 ~`00:01:36,000–00:01:44,000` | `00:17:29,500`; `00:17:37,500` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 65 | C09 ~`00:02:18,000–00:02:22,000` | `00:17:42,267`; `00:17:46,267`; `00:17:50,267`; `00:17:54,267` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 66 | C07 ~`00:00:59,000–00:01:03,000` | `00:18:01,233`; `00:18:05,233`; `00:18:09,233` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 67 | C07 ~`00:01:19,000–00:01:23,000` | `00:18:17,167`; `00:18:21,167`; `00:18:25,167`; `00:18:29,167`; `00:18:33,167` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 68 | C09 ~`00:01:20,000–00:01:28,000` | `00:18:42,827`; `00:18:50,827` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 69 | C08 ~`00:07:29,000–00:07:43,000` | `00:19:08,100` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 70 | C09 ~`00:01:44,000–00:01:51,000` | `00:19:20,660`; `00:19:27,660`; `00:19:34,660` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 71 | C08 ~`00:02:20,000–00:02:35,000` | `00:19:53,400` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 72 | C18 ~`00:00:00,000–00:00:13,000` | `00:20:19,167` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 73 | C18 ~`00:00:34,000–00:00:41,000` | `00:20:35,233`; `00:20:42,233` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 76 | C17 ~`00:01:20,000–00:01:28,000` | `00:21:36,033`; `00:21:44,033` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 78 | C21 ~`00:00:07,000–00:00:10,000` | `00:22:14,233`; `00:22:17,233`; `00:22:20,233`; `00:22:23,233`; `00:22:26,233` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 79 | C10 ~`00:00:19,000–00:00:22,000` | `00:22:29,967`; `00:22:32,967`; `00:22:35,967`; `00:22:38,967`; `00:22:41,967`; `00:22:44,967` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 88 | C10 ~`00:00:00,000–00:00:04,000` | `00:25:38,533`; `00:25:42,533`; `00:25:46,533` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 89 | C17 ~`00:02:20,000–00:02:23,000` | `00:25:51,900`; `00:25:54,900`; `00:25:57,900`; `00:26:00,900` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 90 | C17 ~`00:00:08,000–00:00:14,000` | `00:26:07,600`; `00:26:13,600`; `00:26:19,600` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 91 | C17 ~`00:01:04,000–00:01:08,000` | `00:26:26,320`; `00:26:30,320`; `00:26:34,320`; `00:26:38,320`; `00:26:42,320` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 92 | C11 ~`00:00:16,000–00:00:19,000` | `00:26:45,667`; `00:26:48,667`; `00:26:51,667`; `00:26:54,667`; `00:26:57,667`; `00:27:00,667`; `00:27:03,667` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 94 | C17 ~`00:00:40,000–00:01:00,000` | `00:27:44,067` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 96 | C11 ~`00:00:28,000–00:00:31,000` | `00:28:18,633`; `00:28:21,633`; `00:28:24,633`; `00:28:27,633`; `00:28:30,633`; `00:28:33,633`; `00:28:36,633` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 97 | C17 ~`00:02:32,000–00:02:35,000` | `00:28:39,720`; `00:28:42,720`; `00:28:45,720`; `00:28:48,720`; `00:28:51,720`; `00:28:54,720` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 98 | C21 ~`00:00:15,000–00:00:19,000` | `00:28:59,500`; `00:29:03,500`; `00:29:07,500`; `00:29:11,500`; `00:29:15,500` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 99 | C19 ~`00:00:32,000–00:00:35,000` | `00:29:20,900`; `00:29:23,900`; `00:29:26,900`; `00:29:29,900`; `00:29:32,900`; `00:29:35,900` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 100 | C20 ~`00:02:05,000–00:02:20,000` | `00:29:51,867` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 103 | C16 ~`00:02:04,000–00:02:08,000` | `00:30:53,433`; `00:30:57,433`; `00:31:01,433`; `00:31:05,433` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |

| 105 | C16 ~`00:02:48,000–00:02:55,000` | `00:31:36,233` | Optional 200 ms same-crop cross-dissolve, adjustable 150–250 ms; OFF. Keep all blending in-scene; no extra handles. Too-short remainder/unsupported engine → normal cut. |


BLOCKED placements have no loop recipe: no source duration exists to repeat. Confirm actual approved crop bounds before using the conditional join times above.

## Optional inter-scene transitions — OFF by default

| Boundary | Exact baseline point | Optional choice |
|---|---|---|

| 37 → 38 | `00:08:42,967` | Normal cut by default; optional 150–200 ms restrained dissolve only if existing crops can blend without outside handles or altered duration. |

| 58 → 59 | `00:15:35,467` | Normal cut by default; optional 150–200 ms restrained dissolve only if existing crops can blend without outside handles or altered duration. |

| 78 → 79 | `00:22:26,967` | Normal cut by default; optional 150–200 ms restrained dissolve only if existing crops can blend without outside handles or altered duration. |

| 89 → 90 | `00:26:01,600` | Normal cut by default; optional 150–200 ms restrained dissolve only if existing crops can blend without outside handles or altered duration. |

| 96 → 97 | `00:28:36,720` | Normal cut by default; optional 150–200 ms restrained dissolve only if existing crops can blend without outside handles or altered duration. |

## Research and review basis

The five supplied unique creator videos were reviewed as leads through their available metadata/descriptions/transcripts in the preceding research; the repeated e-zLHf7F-A4 URL is one upload, not two. They are not selected visual sources. Fresh YouTube searches found additional original station uploads. For this revision, metadata and timestamped storyboard images from **21 original uploads** were retrieved and visually inspected. Sampling is about 1 second for very short uploads, 4 seconds for most news packages and 5 seconds for long briefings. All precise-looking source range numbers remain **approximate editorial trims around sampled pictures**, not certified frame edges. No source audio or continuous video was watched/listened to. Scene timing is exact on your baseline; source crop timing is a different, approximate clock.

Research hints (not approved visuals):
- https://www.youtube.com/watch?v=e-zLHf7F-A4 — Trending Tragedies; edited documentary/reused reports; research only.
- https://www.youtube.com/watch?v=RnMPBUznyCU — True Crime Consequence; research only.
- https://www.youtube.com/watch?v=wKieNWr4ixM — The Crime Unit; research only.
- https://www.youtube.com/watch?v=vrL_IidTgrw — Crime Effect; research only.
- https://www.youtube.com/watch?v=yiQNf_cNcpI — Crime Base; research only.

Treat these as unsuitable clean visual masters, including any creator-watermarked portions. No claim is made that all their frames were inspected or that every frame carries a watermark. The selected originals below were verified independently; no sample-frame claims from the example guide were inherited.

## Source library — YouTube only

Dates are verified **upload dates from YouTube metadata**, not automatically event dates. C17 is uploaded Oct 17 but reports the Oct 16 hearing; C18 is uploaded Dec 18 but reports the Dec 17 hearing; C15 is uploaded Apr 29 and is earlier family-appeal coverage, not the funeral. C17’s title says the victim was 15; that title conflicts with the supplied narration’s correct age 14. Do not copy its age error into labels. C07’s upload is Dec 9 but its bulletin describes the Dec 8 search.

### C01 — 'I feel cheated': Family of murdered 14-year-old Tampa boy speaks out, offers reward

- Uploader: **10 Tampa Bay News** · Upload: **2024-04-24** · Metadata length: 128 seconds.
- YouTube: https://www.youtube.com/watch?v=z0GGKSasvIg
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 1, 2, 5, 19, 24.
- Selected approximate windows:

  - Scene 1: ~`00:00:40,000–00:00:44,000` — Low, rail-level view down the tracks in the case report.

  - Scene 2: ~`00:01:44,000–00:01:52,000` — Jevario’s car portrait, as carried in the April reward report.

  - Scene 5: ~`00:01:28,000–00:01:32,000` — Vegetation and ground beside the railway in the report.

  - Scene 19: ~`00:00:32,000–00:00:35,000` — Side view of the railway corridor.

  - Scene 24: ~`00:00:56,000–00:00:59,000` — Trackside vegetation and rail view.

### C02 — Local Tampa officials seek tips in shooting death of 14-year-old

- Uploader: **10 Tampa Bay News** · Upload: **2024-04-22** · Metadata length: 41 seconds.
- YouTube: https://www.youtube.com/watch?v=eUIhBElp_uc
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 11, 22, 23, 30, 50.
- Selected approximate windows:

  - Scene 11: ~`00:00:33,000–00:00:37,000` — Jevario’s standing portrait in the April appeal.

  - Scene 22: ~`00:00:20,000–00:00:24,000` — Station map zoom toward the reported Tampa location.

  - Scene 23: ~`00:00:25,000–00:00:28,000` — Busch/Rome street-sign shot.

  - Scene 30: ~`00:00:03,000–00:00:11,000` — April news presenter beside Jevario’s photos.

  - Scene 50: ~`00:00:38,000–00:00:41,000` — Jevario’s car portrait at the end of the appeal.

### C03 — Teen to be charged as adult for murder of 14-year-old Jevario Buie

- Uploader: **10 Tampa Bay News** · Upload: **2024-12-05** · Metadata length: 171 seconds.
- YouTube: https://www.youtube.com/watch?v=B5qzKsfKcAA
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 29, 40, 54, 58, 61, 62.
- Selected approximate windows:

  - Scene 29: ~`00:01:22,000–00:01:27,000` — Chief Bercaw at the December announcement.

  - Scene 40: ~`00:01:04,000–00:01:07,000` — North Rome/West Busch street signs.

  - Scene 54: ~`00:01:46,000–00:01:55,000` — Bercaw at the podium during the report’s digital-evidence explanation.

  - Scene 58: ~`00:00:19,000–00:00:27,000` — Hannah Dineen reporting outside on the arrest-announcement night.

  - Scene 61: ~`00:01:32,000–00:01:42,000` — Bercaw speaking at the December briefing.

  - Scene 62: ~`00:01:58,000–00:02:05,000` — Prosecution-office representative at the announcement podium.

### C04 — Tampa Police Seek Persons of Interest in Jevario Buie death

- Uploader: **TampaPD** · Upload: **2024-05-09** · Metadata length: 18 seconds.
- YouTube: https://www.youtube.com/watch?v=a0NS9AsqdeA
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 26, 38, 48.
- Selected approximate windows:

  - Scene 26: ~`00:00:01,000–00:00:07,000` — Three teenagers progress into the residential-camera image.

  - Scene 38: ~`00:00:08,000–00:00:13,000` — The group crosses the camera’s near field and tree area.

  - Scene 48: ~`00:00:13,000–00:00:17,000` — The three-person group continues beyond the tree toward a vehicle area.

### C05 — CRIMESTOPPERS REWARD INCREASED IN HOMICIDE INVESTIGATION OF 14-YEAR-OLD JEVARIO BUIE

- Uploader: **TampaPD** · Upload: **2024-05-09** · Metadata length: 863 seconds.
- YouTube: https://www.youtube.com/watch?v=WV986cbBAqg
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 28, 37, 41.
- Selected approximate windows:

  - Scene 28: ~`00:02:25,000–00:02:31,000` — Chief Bercaw at the podium before the shared surveillance.

  - Scene 37: ~`00:02:11,000–00:02:25,000` — Bercaw at the lectern during his canvass explanation.

  - Scene 41: ~`00:02:36,000–00:02:45,000` — Residential-camera surveillance shown during Bercaw’s request to identify the two people.

### C06 — New video released of Tampa teen killed in April

- Uploader: **10 Tampa Bay News** · Upload: **2024-05-09** · Metadata length: 133 seconds.
- YouTube: https://www.youtube.com/watch?v=rT4s5tphM4g
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 10, 21, 34, 35, 39, 42, 43.
- Selected approximate windows:

  - Scene 10: ~`00:00:40,000–00:00:43,000` — Tampa Police building sign/exterior.

  - Scene 21: ~`00:02:08,000–00:02:12,000` — Jevario’s portrait after the briefing report.

  - Scene 34: ~`00:01:03,000–00:01:10,000` — Thaddeus Bullard at the police briefing podium.

  - Scene 35: ~`00:01:28,000–00:01:34,000` — Patrick Messmer speaking at the May briefing.

  - Scene 39: ~`00:01:40,000–00:01:48,000` — Released surveillance reproduced inside the report.

  - Scene 42: ~`00:00:44,000–00:00:50,000` — Messmer answering in the May briefing.

  - Scene 43: ~`00:01:56,000–00:01:59,000` — Tampa police vehicles/exterior in the report.

### C07 — TPD: Search underway after teen accused of killing 14-year-old Jevario Buie escaped juvenile detenti

- Uploader: **10 Tampa Bay News** · Upload: **2024-12-09** · Metadata length: 159 seconds.
- YouTube: https://www.youtube.com/watch?v=pL4PoqPMafw
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 66, 67.
- Selected approximate windows:

  - Scene 66: ~`00:00:59,000–00:01:03,000` — Business-camera view of the road with a running figure, carried in the escape report.

  - Scene 67: ~`00:01:19,000–00:01:23,000` — Aircraft in the sky within the search package.

### C08 — ESCAPED JUVENILE INMATE CAPTURED IN TAMPA

- Uploader: **TampaPD** · Upload: **2024-12-09** · Metadata length: 618 seconds.
- YouTube: https://www.youtube.com/watch?v=dbGceLiuZ4Y
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 69, 71.
- Selected approximate windows:

  - Scene 69: ~`00:07:29,000–00:07:43,000` — Messmer at the lectern with Cate standing beside him.

  - Scene 71: ~`00:02:20,000–00:02:35,000` — Cate responding at the recapture briefing.

### C09 — Teen accused of murder facing more charges after escaping detention center, Tampa police say

- Uploader: **10 Tampa Bay News** · Upload: **2024-12-09** · Metadata length: 203 seconds.
- YouTube: https://www.youtube.com/watch?v=OHILsLEzZ40
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 14, 65, 68, 70.
- Selected approximate windows:

  - Scene 14: ~`00:02:16,000–00:02:20,000` — Fenced detention-area exterior/vegetation in the recapture report.

  - Scene 65: ~`00:02:18,000–00:02:22,000` — Fenced juvenile-facility exterior in follow-up reporting.

  - Scene 68: ~`00:01:20,000–00:01:28,000` — Messmer at the later recapture briefing.

  - Scene 70: ~`00:01:44,000–00:01:51,000` — Cate speaking at the follow-up briefing.

### C10 — 17-year-old found guilty in 2024 murder of Tampa teen

- Uploader: **10 Tampa Bay News** · Upload: **2026-09-04** · Metadata length: 25 seconds.
- YouTube: https://www.youtube.com/watch?v=ViL-3fyD5iA
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 79, 88.
- Selected approximate windows:

  - Scene 79: ~`00:00:19,000–00:00:22,000` — Wide case courtroom view with bench and counsel tables.

  - Scene 88: ~`00:00:00,000–00:00:04,000` — Station news anchor reporting the verdict.

### C11 — Jahmir Moore sentenced in murder of Tampa 14-year-old

- Uploader: **10 Tampa Bay News** · Upload: **2026-10-16** · Metadata length: 31 seconds.
- YouTube: https://www.youtube.com/watch?v=YIDP32FMSho
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 92, 96.
- Selected approximate windows:

  - Scene 92: ~`00:00:16,000–00:00:19,000` — Judge Goudie at the bench in the sentencing update.

  - Scene 96: ~`00:00:28,000–00:00:31,000` — Judge Goudie speaking at the bench.

### C12 — Family of a Jevario Buie bids for justice in hopes to find answers in his death

- Uploader: **WFLA News Channel 8** · Upload: **2024-04-28** · Metadata length: 120 seconds.
- YouTube: https://www.youtube.com/watch?v=cXp03ZJ5SFg
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 32.
- Selected approximate windows:

  - Scene 32: ~`00:01:12,000–00:01:16,000` — Memorial booth/display, photographs and attendees at the crime-victims vigil.

### C13 — Mother of 14-year-old murdered in Tampa demands justice for her son

- Uploader: **10 Tampa Bay News** · Upload: **2024-04-28** · Metadata length: 146 seconds.
- YouTube: https://www.youtube.com/watch?v=e9IADjNowCg
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): Not assigned to picture; researched/context or insert candidate only.
- Selected approximate windows:

### C14 — With no arrests made, family pleads for information after 14-year-old shot and killed in Tampa

- Uploader: **10 Tampa Bay News** · Upload: **2024-04-26** · Metadata length: 153 seconds.
- YouTube: https://www.youtube.com/watch?v=YiVcQQGFf_E
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 16, 36.
- Selected approximate windows:

  - Scene 16: ~`00:00:36,000–00:00:39,000` — Low track view in the April family-appeal report.

  - Scene 36: ~`00:01:48,000–00:01:56,000` — Reporter outside the police building in the April appeal package.

### C15 — Family of Jevario Buie launches website in hopes of finding his killer

- Uploader: **Tampa Bay 28** · Upload: **2024-04-29** · Metadata length: 154 seconds.
- YouTube: https://www.youtube.com/watch?v=pAtmiAZUuGU
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 12, 18, 20, 25, 31.
- Selected approximate windows:

  - Scene 12: ~`00:01:48,000–00:01:56,000` — Justice for Jevario website page visible in the news report.

  - Scene 18: ~`00:00:20,000–00:00:23,000` — Jevario’s standing portrait in the station report.

  - Scene 20: ~`00:01:56,000–00:02:00,000` — Public memorial website, including a memorial image.

  - Scene 25: ~`00:00:24,000–00:00:27,000` — Jevario’s car portrait.

  - Scene 31: ~`00:02:00,000–00:02:04,000` — Public memorial/fundraising webpage in the case report.

### C16 — 14-year-old Tampa Boy will be laid to rest Saturday, as family searches for answers

- Uploader: **WFLA News Channel 8** · Upload: **2024-05-03** · Metadata length: 252 seconds.
- YouTube: https://www.youtube.com/watch?v=D28FFVJXLNw
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 103, 105.
- Selected approximate windows:

  - Scene 103: ~`00:02:04,000–00:02:08,000` — Michael Baldwin Sr. in the earlier outdoor interview.

  - Scene 105: ~`00:02:48,000–00:02:55,000` — Jevario’s memorial/name graphics shown in the family interview report.

### C17 — Florida teen gets 55 years in 15-year-old's murder

- Uploader: **FOX 13 Tampa Bay** · Upload: **2026-10-17** · Metadata length: 174 seconds.
- YouTube: https://www.youtube.com/watch?v=zyKDsEekos4
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 17, 76, 89, 90, 91, 94, 97.
- Selected approximate windows:

  - Scene 17: ~`00:02:24,000–00:02:32,000` — Wide sentencing courtroom with people at counsel tables and near the bench.

  - Scene 76: ~`00:01:20,000–00:01:28,000` — Police surveillance reproduced in sentencing reporting.

  - Scene 89: ~`00:02:20,000–00:02:23,000` — Jevario’s car portrait in sentencing reporting.

  - Scene 90: ~`00:00:08,000–00:00:14,000` — Moore in custody clothing approaching/standing before the sentencing bench.

  - Scene 91: ~`00:01:04,000–00:01:08,000` — Judge Goudie at the sentencing bench.

  - Scene 94: ~`00:00:40,000–00:01:00,000` — Wide sentencing courtroom with an adult man at the lectern facing the judge.

  - Scene 97: ~`00:02:32,000–00:02:35,000` — Wide courtroom after the adult lectern sequence.

### C18 — Teen accused of murder denied bond after escaping from custody

- Uploader: **FOX 13 Tampa Bay** · Upload: **2024-12-18** · Metadata length: 136 seconds.
- YouTube: https://www.youtube.com/watch?v=MRoEPt81UtQ
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 15, 52, 57, 72, 73.
- Selected approximate windows:

  - Scene 15: ~`00:00:00,000–00:00:03,000` — Moore standing in a red uniform and yellow vest at the hearing.

  - Scene 52: ~`00:00:04,000–00:00:07,000` — Judge shown looking at the bench papers in detention-hearing coverage.

  - Scene 57: ~`00:00:28,000–00:00:34,000` — Wide courtroom view during the detention-hearing report.

  - Scene 72: ~`00:00:00,000–00:00:13,000` — Moore, a judge, and the wide hearing courtroom appear in the station sequence.

  - Scene 73: ~`00:00:34,000–00:00:41,000` — Moore in custody clothing during the hearing report.

### C19 — 15-year-old arrested for murder of Tampa teen found near railroad tracks

- Uploader: **FOX 13 Tampa Bay** · Upload: **2024-12-05** · Metadata length: 136 seconds.
- YouTube: https://www.youtube.com/watch?v=ehT8yrPb9E0
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 9, 59, 60, 63, 64, 99.
- Selected approximate windows:

  - Scene 9: ~`00:00:16,000–00:00:19,000` — Jevario’s standing outdoor portrait.

  - Scene 59: ~`00:01:24,000–00:01:27,000` — Moore’s police portrait in the arrest report.

  - Scene 60: ~`00:00:44,000–00:00:52,000` — Wide December press conference with Bercaw and a display.

  - Scene 63: ~`00:01:16,000–00:01:22,000` — Chief Bercaw at the announcement podium.

  - Scene 64: ~`00:01:36,000–00:01:44,000` — Michael Baldwin Sr. speaking with officials/family behind him.

  - Scene 99: ~`00:00:32,000–00:00:35,000` — Chief Bercaw in a close view at the December briefing.

### C20 — Tampa police provide update on teen who escaped from detention center

- Uploader: **WFLA News Channel 8** · Upload: **2024-12-08** · Metadata length: 359 seconds.
- YouTube: https://www.youtube.com/watch?v=01cwmCRk9s4
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 100.
- Selected approximate windows:

  - Scene 100: ~`00:02:05,000–00:02:20,000` — Cate at the outdoor escape-search briefing, police car behind her.

### C21 — Sentencing is planned for Jahmir Moore on Friday

- Uploader: **10 Tampa Bay News** · Upload: **2026-10-16** · Metadata length: 31 seconds.
- YouTube: https://www.youtube.com/watch?v=MrRx2a1NT8s
- Independently inspected: timestamped storyboard samples; metadata/description; automatic captions where available. Continuous picture/audio: not reviewed.
- Placement(s): 13, 78, 98.
- Selected approximate windows:

  - Scene 13: ~`00:00:22,000–00:00:24,000` — Wide courtroom view in the case’s later news report.

  - Scene 78: ~`00:00:07,000–00:00:10,000` — Counsel table and papers in the case’s later court report.

  - Scene 98: ~`00:00:15,000–00:00:19,000` — Case surveillance carried in the later news update.

### BLOCKED source registry — no invented media IDs

- **G003** (placement 3): BLOCKED — The specified two-person 3:33 camera view is not established by the three-person release. No YouTube source or selected crop assigned.

- **G004** (placement 4): BLOCKED — Hands, gait and following distance in the described two-person shot have no verified matching crop. No YouTube source or selected crop assigned.

- **G006** (placement 6): BLOCKED — No case footage verifies the hook’s laundry, cooking, barking dog or neighbors’ knowledge. No YouTube source or selected crop assigned.

- **G007** (placement 7): BLOCKED — No original YouTube crop of the described lone 3:36 departure was established. No YouTube source or selected crop assigned.

- **G008** (placement 8): BLOCKED — The post-shooting gait/hand movements described here cannot be illustrated by the unrelated escape-running video. No YouTube source or selected crop assigned.

- **G027** (placement 27): BLOCKED — The distinct two-person and lone-departure camera views and exact North Rome sequence are not verified here. No YouTube source or selected crop assigned.

- **G033** (placement 33): BLOCKED — No clean YouTube crop of the May 4 service/burial was verified; a May 3 interview is not the funeral. No YouTube source or selected crop assigned.

- **G044** (placement 44): BLOCKED — No verified YouTube image of the recovered phone and its screen was located. No YouTube source or selected crop assigned.

- **G045** (placement 45): BLOCKED — No original YouTube exhibit window verifying both Instagram handles is available. No YouTube source or selected crop assigned.

- **G046** (placement 46): BLOCKED — No verified display of the specific follow dates and meeting messages was found. No YouTube source or selected crop assigned.

- **G047** (placement 47): BLOCKED — No verified original Citgo photograph/message exhibit window was located. No YouTube source or selected crop assigned.

- **G049** (placement 49): BLOCKED — The third teenager’s interview is not verified as a releasable YouTube recording; do not identify a young witness. No YouTube source or selected crop assigned.

- **G051** (placement 51): BLOCKED — No distinct YouTube footage of the September car-theft surrender is verified. No YouTube source or selected crop assigned.

- **G053** (placement 53): BLOCKED — No chain-of-custody log, extraction demonstration or relevant case-evidence handling footage was verified. No YouTube source or selected crop assigned.

- **G055** (placement 55): BLOCKED — The homicide-search and weapon-claim exhibits have no verified safe YouTube crop here. No YouTube source or selected crop assigned.

- **G056** (placement 56): BLOCKED — No verified display of the account-switch message or the separate non-public-detail message was located. No YouTube source or selected crop assigned.

- **G074** (placement 74): BLOCKED — No verified YouTube footage of the alleged March incident or Claymore scene was found. No YouTube source or selected crop assigned.

- **G075** (placement 75): BLOCKED — No verified source window showing the March group-chat exhibit was located. No YouTube source or selected crop assigned.

- **G077** (placement 77): BLOCKED — No original YouTube trial opening/explanation by Sinardi was verified. No YouTube source or selected crop assigned.

- **G080** (placement 80): BLOCKED — No verified YouTube window of Fossett’s opening/slides was located. No YouTube source or selected crop assigned.

- **G081** (placement 81): BLOCKED — No verified YouTube window of Sinardi’s opening/medical-examiner argument was located. No YouTube source or selected crop assigned.

- **G082** (placement 82): BLOCKED — No verified Belara Lakes/route exhibit crop was located; no unrelated apartment footage substituted. No YouTube source or selected crop assigned.

- **G083** (placement 83): BLOCKED — No verified Norton testimony crop was found; no young witness is identified by inference. No YouTube source or selected crop assigned.

- **G084** (placement 84): BLOCKED — No safe verified recording/exhibit crop is selected; the crime-scene photograph and gallery distress are intentionally not shown. No YouTube source or selected crop assigned.

- **G085** (placement 85): BLOCKED — No original YouTube window of Moore testifying was verified; a defendant seated silently is not testimony footage. No YouTube source or selected crop assigned.

- **G086** (placement 86): BLOCKED — No verified lone-walk/phone-browsing courtroom exhibit or rebuttal crop was found. No YouTube source or selected crop assigned.

- **G087** (placement 87): BLOCKED — No verified safe shorts/exhibit or medical-evidence window was located. No YouTube source or selected crop assigned.

- **G093** (placement 93): BLOCKED — No clean verified mitigation memorandum or supporting biographical exhibit is available on YouTube. No YouTube source or selected crop assigned.

- **G095** (placement 95): BLOCKED — No verified YouTube source presenting the applicable statute/review factors accurately was located. No YouTube source or selected crop assigned.

- **G101** (placement 101): BLOCKED — No verified statute/review explainer window matches the application-and-counsel procedure. No YouTube source or selected crop assigned.

- **G102** (placement 102): BLOCKED — No verified source window matches conditional modification/probation and relatives’ participation rules. No YouTube source or selected crop assigned.

- **G104** (placement 104): BLOCKED — No November appellate docket/status video was verified; a sentencing report is not evidence that no appeal was filed. No YouTube source or selected crop assigned.

## Optional original-audio breaks

Eight **candidate** breaks, not automatic insertions. They are separate from picture-only crop selections. Approve and trim each by listening before use; source audio and picture play once. The CapCut companion explains synchronized pauses and the longer working clock.

### 1. Thaddeus Bullard at the May briefing

**Your project break:** `00:07:53:05 @ 30 fps` (nearest working frame); exact pre-insert baseline anchor **`00:07:53,167`**.  
**Pause after:** “Hillsborough County State Attorney Suzy Lopez joined officials urging people with information to come forward.”  
**Source ID:** C06  
**Source:** [New video released of Tampa teen killed in April](https://www.youtube.com/watch?v=rT4s5tphM4g) | 10 Tampa Bay News | upload 2024-05-09.  
**Trim source, approximately:** `01:03.0–01:11.0` on the **source-video clock**, approximately 8.0 seconds. Based on timed automatic captions plus sampled pictures; exact in/out pending listening/continuous review.  
**What is heard:** Thaddeus Bullard at the May briefing; use the source video’s original English audio, never a creator’s retelling.  
**What is seen:** Bullard speaks at the podium in sampled pictures. Exact cut points still require moving-picture review.  
**Find the cut:** search near “We need answers” through the completed thought near “amplifying this message”. These are automatic-transcript locators, not certified verbatim quotations.  
**Resume with:** “Police also released a clip showing Jevario walking with two people shortly before the shooting.”  
**Label:** Thaddeus Bullard | May 9, 2024  
**Care:** Do not continue into later bullying/group speculation. Skip if the source cannot supply a complete, respectful, intelligible excerpt.  
**Caption check:** resume cue 180 begins at `00:07:53,167`. This proposed break is at a continuous SRT cue boundary, so no saved cue needs a text split. In the working edit, trim any preceding caption/overlay tail at the pause; verify raw JSON gaps and actual speech rather than assuming silence.

### 2. Bercaw describes canvassing and evidence collection

**Your project break:** `00:08:42:29 @ 30 fps` (nearest working frame); exact pre-insert baseline anchor **`00:08:42,967`**.  
**Pause after:** “Those recordings supplied separate observations of the afternoon, allowing detectives to reconstruct portions of a sequence that no single public account could explain.”  
**Source ID:** C05  
**Source:** [CRIMESTOPPERS REWARD INCREASED IN HOMICIDE INVESTIGATION OF 14-YEAR-OLD JEVARIO BUIE](https://www.youtube.com/watch?v=WV986cbBAqg) | TampaPD | upload 2024-05-09.  
**Trim source, approximately:** `02:11.3–02:24.0` on the **source-video clock**, approximately 12.7 seconds. Based on timed automatic captions plus sampled pictures; exact in/out pending listening/continuous review.  
**What is heard:** Bercaw describes canvassing and evidence collection; use the source video’s original English audio, never a creator’s retelling.  
**What is seen:** Bercaw at lectern in sampled pictures. Exact cut points still require moving-picture review.  
**Find the cut:** search near “we canvased the areas” through the completed thought near “this investigation”. These are automatic-transcript locators, not certified verbatim quotations.  
**Resume with:** “This method had a limitation.”  
**Label:** Chief Lee Bercaw | May 9, 2024  
**Care:** Automatic captions overlap the sentence start/end; find the complete thought by ear. Skip if the source cannot supply a complete, respectful, intelligible excerpt.  
**Caption check:** resume cue 202 begins at `00:08:42,967`. This proposed break is at a continuous SRT cue boundary, so no saved cue needs a text split. In the working edit, trim any preceding caption/overlay tail at the pause; verify raw JSON gaps and actual speech rather than assuming silence.

### 3. Prosecution-office representative discusses adult prosecution

**Your project break:** `00:17:00:01 @ 30 fps` (nearest working frame); exact pre-insert baseline anchor **`00:17:00,033`**.  
**Pause after:** “It did not measure a completed court case.”  
**Source ID:** C03  
**Source:** [Teen to be charged as adult for murder of 14-year-old Jevario Buie](https://www.youtube.com/watch?v=B5qzKsfKcAA) | 10 Tampa Bay News | upload 2024-12-05.  
**Trim source, approximately:** `01:57.9–02:04.8` on the **source-video clock**, approximately 6.9 seconds. Based on timed automatic captions plus sampled pictures; exact in/out pending listening/continuous review.  
**What is heard:** Prosecution-office representative discusses adult prosecution; use the source video’s original English audio, never a creator’s retelling.  
**What is seen:** Man at the announcement podium in sampled pictures; not Suzy Lopez. Exact cut points still require moving-picture review.  
**Find the cut:** search near “There is no more adult decision” through the completed thought near “taking of a life”. These are automatic-transcript locators, not certified verbatim quotations.  
**Resume with:** “The police department’s December release summarized communications records, social media messages, notes, and search history.”  
**Label:** State Attorney’s Office | Dec 5, 2024  
**Care:** Do not name the representative until confirmed; not a judicial ruling. Skip if the source cannot supply a complete, respectful, intelligible excerpt.  
**Caption check:** resume cue 400 begins at `00:17:00,033`. This proposed break is at a continuous SRT cue boundary, so no saved cue needs a text split. In the working edit, trim any preceding caption/overlay tail at the pause; verify raw JSON gaps and actual speech rather than assuming silence.

### 4. Eric Glasser reads the archived escape alert

**Your project break:** `00:17:57:07 @ 30 fps` (nearest working frame); exact pre-insert baseline anchor **`00:17:57,233`**.  
**Pause after:** “A head count after the group returned inside established that he had not returned from the fenced area.”  
**Source ID:** C07  
**Source:** [TPD: Search underway after teen accused of killing 14-year-old Jevario Buie escaped juvenile detenti](https://www.youtube.com/watch?v=pL4PoqPMafw) | 10 Tampa Bay News | upload 2024-12-09.  
**Trim source, approximately:** `00:05.5–00:18.5` on the **source-video clock**, approximately 13.0 seconds. Based on timed automatic captions plus sampled pictures; exact in/out pending listening/continuous review.  
**What is heard:** Eric Glasser reads the archived escape alert; use the source video’s original English audio, never a creator’s retelling.  
**What is seen:** News anchor against breaking-news graphics in sampled pictures. Exact cut points still require moving-picture review.  
**Find the cut:** search near “Tampa Police telling us” through the completed thought near “now on the Run”. These are automatic-transcript locators, not certified verbatim quotations.  
**Resume with:** “A nearby business recorded him running west around 10:45 a.m.”  
**Label:** ARCHIVE | Dec 8, 2024 escape report  
**Care:** Upload is Dec 9; do not imply a current search. Confirm the clean start after introduction. Skip if the source cannot supply a complete, respectful, intelligible excerpt.  
**Caption check:** resume cue 421 begins at `00:17:57,233`. This proposed break is at a continuous SRT cue boundary, so no saved cue needs a text split. In the working edit, trim any preceding caption/overlay tail at the pause; verify raw JSON gaps and actual speech rather than assuming silence.

### 5. Messmer describes peaceful surrender

**Your project break:** `00:19:13:20 @ 30 fps` (nearest working frame); exact pre-insert baseline anchor **`00:19:13,660`**.  
**Pause after:** “Their presence alone did not establish how Moore escaped or who helped him.”  
**Source ID:** C08  
**Source:** [ESCAPED JUVENILE INMATE CAPTURED IN TAMPA](https://www.youtube.com/watch?v=dbGceLiuZ4Y) | TampaPD | upload 2024-12-09.  
**Trim source, approximately:** `07:57.0–08:05.0` on the **source-video clock**, approximately 8.0 seconds. Based on timed automatic captions plus sampled pictures; exact in/out pending listening/continuous review.  
**What is heard:** Messmer describes peaceful surrender; use the source video’s original English audio, never a creator’s retelling.  
**What is seen:** Messmer at the lectern with Cate behind/alongside in sampled pictures. Exact cut points still require moving-picture review.  
**Find the cut:** search near “we were able to get him” through the completed thought near “peacefully”. These are automatic-transcript locators, not certified verbatim quotations.  
**Resume with:** “Moore received a felony charge of escape from a juvenile detention facility.”  
**Label:** Major Patrick Messmer | Dec 9, 2024  
**Care:** Keep the complete qualification; no private address or parents’ culpability inference. Skip if the source cannot supply a complete, respectful, intelligible excerpt.  
**Caption check:** resume cue 448 begins at `00:19:13,660`. This proposed break is at a continuous SRT cue boundary, so no saved cue needs a text split. In the working edit, trim any preceding caption/overlay tail at the pause; verify raw JSON gaps and actual speech rather than assuming silence.

### 6. Courtroom audio of the detention ruling, as carried by the station

**Your project break:** `00:20:28:07 @ 30 fps` (nearest working frame); exact pre-insert baseline anchor **`00:20:28,233`**.  
**Pause after:** “Murphy ordered Moore held without bail in the adult Hillsborough County Jail.”  
**Source ID:** C18  
**Source:** [Teen accused of murder denied bond after escaping from custody](https://www.youtube.com/watch?v=MRoEPt81UtQ) | FOX 13 Tampa Bay | upload 2024-12-18.  
**Trim source, approximately:** `00:25.6–00:32.2` on the **source-video clock**, approximately 6.6 seconds. Based on timed automatic captions plus sampled pictures; exact in/out pending listening/continuous review.  
**What is heard:** Courtroom audio of the detention ruling, as carried by the station; use the source video’s original English audio, never a creator’s retelling.  
**What is seen:** Wide hearing courtroom around 28–32 seconds; the judge is not necessarily in the same frame. Exact cut points still require moving-picture review.  
**Find the cut:** search near “I'll Grant” through the completed thought near “premeditated”. These are automatic-transcript locators, not certified verbatim quotations.  
**Resume with:** “That ruling settled his custody status, not his guilt.”  
**Label:** Detention hearing | Dec 17, 2024  
**Care:** Confirm the voice, attribution and complete sentence; upload date Dec 18, not the hearing date. Skip if the source cannot supply a complete, respectful, intelligible excerpt.  
**Caption check:** resume cue 478 begins at `00:20:28,233`. This proposed break is at a continuous SRT cue boundary, so no saved cue needs a text split. In the working edit, trim any preceding caption/overlay tail at the pause; verify raw JSON gaps and actual speech rather than assuming silence.

### 7. News anchor reports the verdict

**Your project break:** `00:25:48:27 @ 30 fps` (nearest working frame); exact pre-insert baseline anchor **`00:25:48,900`**.  
**Pause after:** “Sentencing was scheduled for October 16.”  
**Source ID:** C10  
**Source:** [17-year-old found guilty in 2024 murder of Tampa teen](https://www.youtube.com/watch?v=ViL-3fyD5iA) | 10 Tampa Bay News | upload 2026-09-04.  
**Trim source, approximately:** `00:04.0–00:10.2` on the **source-video clock**, approximately 6.2 seconds. Based on timed automatic captions plus sampled pictures; exact in/out pending listening/continuous review.  
**What is heard:** News anchor reports the verdict; use the source video’s original English audio, never a creator’s retelling.  
**What is seen:** The package changes from anchor to case-court pictures and a portrait. Exact cut points still require moving-picture review.  
**Find the cut:** search near “A Tampa jury found” through the completed thought near “Jevario”. These are automatic-transcript locators, not certified verbatim quotations.  
**Resume with:** “The family said the jury got it right, while acknowledging that nobody had won.”  
**Label:** 10 Tampa Bay | Sept 4, 2026 verdict report  
**Care:** Not jury audio; crop/blur other child if portrait appears. End after full victim name, adjusting the estimated out by listening. Skip if the source cannot supply a complete, respectful, intelligible excerpt.  
**Caption check:** resume cue 602 begins at `00:25:48,900`. This proposed break is at a continuous SRT cue boundary, so no saved cue needs a text split. In the working edit, trim any preceding caption/overlay tail at the pause; verify raw JSON gaps and actual speech rather than assuming silence.

### 8. News anchor reports the sentence

**Your project break:** `00:27:04:23 @ 30 fps` (nearest working frame); exact pre-insert baseline anchor **`00:27:04,767`**.  
**Pause after:** “Review offered a judicial decision, not a scheduled release date.”  
**Source ID:** C11  
**Source:** [Jahmir Moore sentenced in murder of Tampa 14-year-old](https://www.youtube.com/watch?v=YIDP32FMSho) | 10 Tampa Bay News | upload 2026-10-16.  
**Trim source, approximately:** `00:00.3–00:04.2` on the **source-video clock**, approximately 3.9 seconds. Based on timed automatic captions plus sampled pictures; exact in/out pending listening/continuous review.  
**What is heard:** News anchor reports the sentence; use the source video’s original English audio, never a creator’s retelling.  
**What is seen:** Anchor remains on screen across this sampled opening. Exact cut points still require moving-picture review.  
**Find the cut:** search near “a judge has sentenced” through the completed thought near “55 years in prison”. These are automatic-transcript locators, not certified verbatim quotations.  
**Resume with:** “The defense mitigation memorandum described separated parents and a cousin’s death in an accidental shooting.”  
**Label:** 10 Tampa Bay | Oct 16, 2026 sentencing report  
**Care:** Transcript begins mid-phrase “hour”; if no complete clean opening can be trimmed, skip. Not the judge’s own audio. Skip if the source cannot supply a complete, respectful, intelligible excerpt.  
**Caption check:** resume cue 630 begins at `00:27:04,767`. This proposed break is at a continuous SRT cue boundary, so no saved cue needs a text split. In the working edit, trim any preceding caption/overlay tail at the pause; verify raw JSON gaps and actual speech rather than assuming silence.

## Missing Sources / Unverified Ranges / Timing Uncertainties

- BLOCKED placements have real reserved project intervals but **no assigned picture**. They are production holds, not black-scene instructions or claims of successful coverage. Please send original YouTube links for those beats, especially the two-person/lone-departure CCTV, recovered phone/private-message/Citgo exhibits, original trial testimony, mitigation documents and a reliable juvenile-review explainer. No invented crop or generic police opening fills these gaps.
- All source trims are **approximate**. Timestamped YouTube storyboard stills were inspected; they verify sampled pictures, not every frame, uninterrupted shot boundaries, facial expression, clean audio or precise edit points. English automatic captions were downloaded for speech locators; they can overlap, mistranscribe and extend beyond metadata duration. Source audio and continuous moving video were **not** reviewed. Fine-trim by listening and watching before approval.
- Third-party creator hint links remain research-only and excluded from visuals; do not use a watermarked/rebranded re-upload as clean original footage. Station logos/lower-thirds on original news uploads are normal provenance, not proof of reuse permission. No attempt was made to remove them. Watermark-free master availability and reuse rights remain unresolved.
- Standalone TampaPD escape locator `https://www.youtube.com/watch?v=5pMeJcySADY` returned unavailable. The running figure was instead independently located in the original station report C07, approximately 00:59–01:03. This is a **proposed new revision source**, not a silent change to an approved edit.
- No narration audio file was attached. The JSON references an inaccessible local Mac MP3 path. 00:31:37,100 is the matching SRT/project/audio metadata end, not a listening-confirmed last syllable. Casefile output FPS is unknown; supplied CapCut JSON FPS is 30.0.
- Preserved caption/script uncertainties: cue 72 contraction; handles across 260–261; missing “Assistant” in 357/473; endings in 469/517/524/681; “them/em” in 500; extra “add” in 635; “a rest/arrest” in 684. Anchor at the first existing “State Attorney” slot where “Assistant” has no timing. Inputs are not rewritten.
- This is a separately named **proposed revision for approval**, not an applied update. Existing guides and project inputs are untouched. Source/crop/scene choices here must be approved before replacing an existing approved plan. No app looping, transition, imported picture coverage, preview or export was tested.

## Validation result and approval gate

- **105** positive-duration reserved intervals, contiguous from **00:00:00,000 to 00:31:37,100**; first caption remains **00:00:00,067** in existing scene 1.
- **73** picture-assigned placements and **32 BLOCKED** placements. The latter prevent a claim of complete usable picture coverage. All source IDs resolve to the YouTube library or clearly marked unresolved-source registry.
- Every `At` is an exact narration excerpt; the narration text chunks reconstruct the entire supplied narration in order. No narration/caption timing input changed.
- **73** distinct original-upload/range pairs; maximum consecutive identical pair **1**; maximum exact-pair share **1.46%** of baseline, below 15%. This audit is additional to, not a replacement for, the underlying-footage duplication warnings.
- All media links are YouTube. Eight original-audio candidates use exact narration phrases and baseline resume-cue starts, with nearest 30 fps frame-style timecodes and approximate source trims.
- All supplied files remain SHA-256-identical. The previous guides were not overwritten. This revision is **for approval**, not an app-applied edit; no preview/export has been verified.
