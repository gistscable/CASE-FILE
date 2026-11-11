# Audio breaks (Mode O): original sound inside the documentary

For key moments (a family statement, a judge, a sentencing) the narration **pauses**, the clip plays with
its **own sound and picture** for 2 to 30 seconds, then the narration **resumes at the same word**.
Everything after a break moves later by the break's length. The narration recording is never edited, and
every spoken word still appears once, in order.

Everywhere else source audio stays muted, exactly as before.

## In the guide

Add one field to a normal footage card (the card needs a Source ID):

```
### 12. Narration beat

**At:** “The judge then turned to the family”
**Show:** The mother's statement, muted, while the narration introduces it.
**Preview:** [Court feed, ~0:08–0:14](https://example.org/hearing) (`S07`).
**Label:** County court | 2024.
**Care:** Composed statement only.
**Audio break:** 0:20–0:32
**Source ID:** S07
```

* `At` is the first phrase spoken **after** the break. The break plays just before that phrase.
* `Audio break` is a window **inside the card's source file** (`0:20–0:32`, `1:02:10–1:02:25`, or `20s–32s`).
  It must be 2 to 30 seconds. About one break every 3 to 4 minutes, and about 8 per video, works best;
  more is only a note in the plan, not an error.
* The card's normal `Preview` window is still the **muted** picture that covers the narration afterwards.
  It does not need to be the same part of the file.
* If the script needs a lead-in line ("In court, she said:") the locked script lacks, propose it and
  wait for the producer's approval; the editor never rewrites the script.

## Clearance (explicit, per source file)

Playing someone's recorded voice is a separate decision from showing their picture. The break plays only
when, on that source in the app, you have:

1. linked the file and recorded its reuse basis, and ticked **I recorded this file's reuse basis**, then
2. ticked **I may play this file's original audio in the video** (shown only for sources that have an audio
   break; the file must have an audio track).

Changing the file or its rights notes clears the tick. **Producer sign-off never ticks it for you.** Without
the tick the break is left out, the video plays normally, and the Issues list says
"Audio break left out" (it blocks the final export until you clear it or remove the break from the guide;
drafts still render).

## What the render does

* Picture: the clip's window, with its source/date label.
* Sound: the clip's own audio, loudness-matched, with a short fade at each edge, while the music bed ducks
  under it as it does under the narration.
* The video is longer than the narration by the total of the breaks; captions have no text during a break.
* `plan.md` and the export notes list every break (video time, narration time, window, length) and every
  break that was left out, and why.

## Rules the editor enforces

* A break only plays from the **primary** file the card was written for, not a guide alternative.
* A hand-edited break (changed window or file) is flagged and the plan must be rebuilt.
* The narration check now follows the narration itself: breaks pause it and never consume it.
* No looping: the break window plays once and is never extended.

Tests: `tests/test_audiobreak.py` (27), including a render that measures the real audio (narration before the
break, the clip's own tone during it, narration resuming at the same word).
