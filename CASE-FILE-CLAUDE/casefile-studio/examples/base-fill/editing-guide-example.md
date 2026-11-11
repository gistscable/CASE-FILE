# Example production guide (fictional demo of the base-image format)

**Standing boundaries:** Fictional example. Keep narration unchanged; mute source audio; label archive images honestly.

## Project setup

- Case: Harbor Vale (fictional example)
- Victim: Alex Rivers
- Suspect: Sam Drake
- Avoid tags: graphic
- Avoid in CHAPTER 1: residential

## Script-by-script placement

### HOOK

### 1. Narration beat

**At:** “Alex Rivers was a fictional student”
**Fill:** V / portrait
**Show:** No footage of this moment exists. The editor covers it with victim portraits.
**Care:** Archive images only; never imply they show the narrated moment.

### CHAPTER 1

### 2. Narration beat

**At:** “On a quiet evening a camera”
**Show:** Street camera view near the tracks, muted.
**Preview:** [Local news report, ~0:10–0:14](https://example.org/news-report) (`S01`).
**Label:** Harbor Vale News | June 2024.
**Care:** Wide view only.
**Fill:** C / location
**Source ID:** S01
**Crop fill:** The 4 s window plays once; a location base image covers the rest of the scene.
**Your timing:** `00:00:08,000 --> 00:00:20,000`

### 3. Narration beat

**At:** “His mother Dana stood”
**Fill:** V / family
**Show:** No clip of the mother is available; family and portrait base images stand in.

### 4. Narration beat

**At:** “The family held a vigil”
**Fill:** V / memorial
**Show:** No vigil footage available; memorial base images stand in.

### 5. Narration beat

**At:** “Months later Sam Drake”
**Fill:** S / court
**Show:** No courtroom footage available; court base images of the suspect stand in.

## Source library

### S01 — Harbor Vale News: street report
- Uploader: Harbor Vale News · Upload: 2024-06-02
- YouTube: https://example.org/news-report
- Save as: `S01.mp4` · Window: 0:10–0:14

## Base clips

Real images and clips of the victim, the suspect and the location. The editor uses them
for any stretch of narration with no matching clip, with relevant tags and varied zoom.

| Save as | What it shows | Where to get it | Tag |
|---|---|---|---|
| `BASE-V--portrait--01.jpg` | victim portrait (official photo) | police release | portrait |
| `BASE-V--portrait--02.jpg` | second portrait | police release | portrait |
| `BASE-V--family--01.jpg` | family appeal still | news report, 0:30 | family |
| `BASE-V--memorial--01.jpg` | vigil still | news report, 1:12 | memorial |
| `BASE-S--court--01.jpg` | suspect at a hearing | court-feed still | court |
| `BASE-C--location--01.jpg` | street near the tracks | news report, 0:05 | location |
| `BASE-C--location--02.mp4` | street, 12 s clip | news report, 0:40–0:52 | location |

## File checklist

| Save as | Type | Where to get it | Window |
|---|---|---|---|
| `S01.mp4` | footage | https://example.org/news-report | 0:10–0:14 |
| every `BASE-` file above | base images | see the table above | n/a |
