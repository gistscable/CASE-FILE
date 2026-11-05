# The Last Timeline — source download manifest

This folder is the fetch list for the guide's 21 original YouTube uploads
(`C01`–`C21`). It records the exact link, uploader, upload date, metadata
length and proposed file name for each source, so a download can be matched to
a guide row without guessing.

- `manifest.json` — machine-readable: source id, YouTube id, URL, title,
  uploader, upload date, metadata length, picture placements, selected
  approximate windows, canonical file name, plus the 32 BLOCKED beats.
- `sources.csv` — the same table for a spreadsheet.
- `windows.csv` — the guide's 73 selected approximate windows (placement,
  source, `source_start`, `source_end`, duration, intended picture), which is
  what you will actually trim in the editor.
- `downloads/` — where the tool puts the videos. **Gitignored. Never commit it.**

The guide itself is stored byte-identical at `../diverse-revision-guide.md`
(supplied file `Casefile_Studio_Diverse_Revision_FOR_APPROVAL.md`).

## File naming

```
{source_id}__{upload_date}__{uploader_slug}__{title_slug}__{video_id}.mp4
```

Example: `C04__2024-05-09__tampapd__tampa-police-seek-persons-of-interest-in-jevario-buie-death__a0NS9AsqdeA.mp4`

| Part | Meaning |
|---|---|
| `source_id` | the guide's Source ID, `C01`–`C21` |
| `upload_date` | YouTube upload date, **not** the event date |
| `uploader_slug` | station/agency, lowercase ASCII, hyphenated |
| `title_slug` | first 60 characters of the upload title, cut on a word boundary |
| `video_id` | the 11-character YouTube id, so a renamed file can always be re-verified |

## Running the download

The app deliberately does not download YouTube media (see
`../../EPISODE-WORKFLOW.md`). Use the tool with `yt-dlp` and `ffmpeg` on a
machine with normal internet access:

```bash
cd casefile-studio
python3 tools/fetch_youtube_sources.py list                  # what is missing
python3 tools/fetch_youtube_sources.py fetch                 # all 21
python3 tools/fetch_youtube_sources.py fetch --ids C04,C05   # a subset
python3 tools/fetch_youtube_sources.py fetch --max-height 720
python3 tools/fetch_youtube_sources.py rename --dir ~/Downloads/the-last-timeline
python3 tools/fetch_youtube_sources.py verify                # presence + duration
```

`fetch` downloads into `.incoming/` and renames each file to the canonical name
as soon as it finishes, writes `downloads/download-log.json`, skips files that
are already there (`--force` to redo), and exits non-zero if any source fails.
`rename` fixes files you already have: it matches the YouTube id inside the
existing name and renames only the ones it can prove.

Two sources are long briefings and dominate the download: `C05` (14:23) and
`C08` (10:18). The full set is 67½ minutes of video — budget a few GB, or fetch
only the chapters you are editing first.

## The 21 sources

| Source | Upload date | Uploader | Length | Guide placements | File name |
|---|---|---|---|---|---|
| C01 | 2024-04-24 | 10 Tampa Bay News | 2:08 | 1, 2, 5, 19, 24 | `C01__2024-04-24__10-tampa-bay-news__i-feel-cheated-family-of-murdered-14-year-old-tampa-boy__z0GGKSasvIg.mp4` |
| C02 | 2024-04-22 | 10 Tampa Bay News | 0:41 | 11, 22, 23, 30, 50 | `C02__2024-04-22__10-tampa-bay-news__local-tampa-officials-seek-tips-in-shooting-death-of-14__eUIhBElp_uc.mp4` |
| C03 | 2024-12-05 | 10 Tampa Bay News | 2:51 | 29, 40, 54, 58, 61, 62 | `C03__2024-12-05__10-tampa-bay-news__teen-to-be-charged-as-adult-for-murder-of-14-year-old__B5qzKsfKcAA.mp4` |
| C04 | 2024-05-09 | TampaPD | 0:18 | 26, 38, 48 | `C04__2024-05-09__tampapd__tampa-police-seek-persons-of-interest-in-jevario-buie-death__a0NS9AsqdeA.mp4` |
| C05 | 2024-05-09 | TampaPD | 14:23 | 28, 37, 41 | `C05__2024-05-09__tampapd__crimestoppers-reward-increased-in-homicide-investigation-of__WV986cbBAqg.mp4` |
| C06 | 2024-05-09 | 10 Tampa Bay News | 2:13 | 10, 21, 34, 35, 39, 42, 43 | `C06__2024-05-09__10-tampa-bay-news__new-video-released-of-tampa-teen-killed-in-april__rT4s5tphM4g.mp4` |
| C07 | 2024-12-09 | 10 Tampa Bay News | 2:39 | 66, 67 | `C07__2024-12-09__10-tampa-bay-news__tpd-search-underway-after-teen-accused-of-killing-14-year__pL4PoqPMafw.mp4` |
| C08 | 2024-12-09 | TampaPD | 10:18 | 69, 71 | `C08__2024-12-09__tampapd__escaped-juvenile-inmate-captured-in-tampa__dbGceLiuZ4Y.mp4` |
| C09 | 2024-12-09 | 10 Tampa Bay News | 3:23 | 14, 65, 68, 70 | `C09__2024-12-09__10-tampa-bay-news__teen-accused-of-murder-facing-more-charges-after-escaping__OHILsLEzZ40.mp4` |
| C10 | 2026-09-04 | 10 Tampa Bay News | 0:25 | 79, 88 | `C10__2026-09-04__10-tampa-bay-news__17-year-old-found-guilty-in-2024-murder-of-tampa-teen__ViL-3fyD5iA.mp4` |
| C11 | 2026-10-16 | 10 Tampa Bay News | 0:31 | 92, 96 | `C11__2026-10-16__10-tampa-bay-news__jahmir-moore-sentenced-in-murder-of-tampa-14-year-old__YIDP32FMSho.mp4` |
| C12 | 2024-04-28 | WFLA News Channel 8 | 2:00 | 32 | `C12__2024-04-28__wfla-news-channel-8__family-of-a-jevario-buie-bids-for-justice-in-hopes-to-find__cXp03ZJ5SFg.mp4` |
| C13 | 2024-04-28 | 10 Tampa Bay News | 2:26 | research only | `C13__2024-04-28__10-tampa-bay-news__mother-of-14-year-old-murdered-in-tampa-demands-justice-for__e9IADjNowCg.mp4` |
| C14 | 2024-04-26 | 10 Tampa Bay News | 2:33 | 16, 36 | `C14__2024-04-26__10-tampa-bay-news__with-no-arrests-made-family-pleads-for-information-after-14__YiVcQQGFf_E.mp4` |
| C15 | 2024-04-29 | Tampa Bay 28 | 2:34 | 12, 18, 20, 25, 31 | `C15__2024-04-29__tampa-bay-28__family-of-jevario-buie-launches-website-in-hopes-of-finding__pAtmiAZUuGU.mp4` |
| C16 | 2024-05-03 | WFLA News Channel 8 | 4:12 | 103, 105 | `C16__2024-05-03__wfla-news-channel-8__14-year-old-tampa-boy-will-be-laid-to-rest-saturday-as__D28FFVJXLNw.mp4` |
| C17 | 2026-10-17 | FOX 13 Tampa Bay | 2:54 | 17, 76, 89, 90, 91, 94, 97 | `C17__2026-10-17__fox-13-tampa-bay__florida-teen-gets-55-years-in-15-year-old-s-murder__zyKDsEekos4.mp4` |
| C18 | 2024-12-18 | FOX 13 Tampa Bay | 2:16 | 15, 52, 57, 72, 73 | `C18__2024-12-18__fox-13-tampa-bay__teen-accused-of-murder-denied-bond-after-escaping-from__MRoEPt81UtQ.mp4` |
| C19 | 2024-12-05 | FOX 13 Tampa Bay | 2:16 | 9, 59, 60, 63, 64, 99 | `C19__2024-12-05__fox-13-tampa-bay__15-year-old-arrested-for-murder-of-tampa-teen-found-near__ehT8yrPb9E0.mp4` |
| C20 | 2024-12-08 | WFLA News Channel 8 | 5:59 | 100 | `C20__2024-12-08__wfla-news-channel-8__tampa-police-provide-update-on-teen-who-escaped-from__01cwmCRk9s4.mp4` |
| C21 | 2026-10-16 | 10 Tampa Bay News | 0:31 | 13, 78, 98 | `C21__2026-10-16__10-tampa-bay-news__sentencing-is-planned-for-jahmir-moore-on-friday__MrRx2a1NT8s.mp4` |

`C13` is in the guide's library but assigned to **no picture** — it is a
research/context or insert candidate. Download it only if a later revision
uses it.

## What cannot be downloaded

32 of the guide's 105 beats are **BLOCKED**: the guide assigns them no source
range because no matching original upload was verified. They appear in
`manifest.json` as the `blocked` list (`G003`, `G004`, `G006` … `G104`) with
the reason for each. There is no link to fetch and no file name to give them —
do not substitute stock or an unrelated upload. The largest gaps are the
separate 3:33 two-person and 3:36 lone-departure CCTV, the recovered
phone/Instagram/Citgo exhibits, trial testimony, the mitigation memorandum,
and a statute/review explainer.

| Blocked segment | Placements | Count |
|---|---|---|
| Hook camera detail (laundry, dog, lone departure, post-shooting walk) | 3, 4, 6, 7, 8 | 5 |
| North Rome 3:33/3:36 sequence | 27 | 1 |
| May 4 funeral/burial | 33 | 1 |
| Phone, Instagram handles/messages, Citgo photo, witness interview | 44, 45, 46, 47, 49 | 5 |
| September car-theft surrender, chain of custody, search history, account switch | 51, 53, 55, 56 | 4 |
| March dispute, group chat, trial openings, Belara Lakes exhibits, testimony, exhibits, rebuttal, statute explains | 74, 75, 77, 80, 81, 82, 83, 84, 85, 86, 87, 93, 95, 101, 102, 104 | 16 |

## Before you use any of this

- **No reuse rights are established.** The links are locators, not licences.
  Station logos and lower-thirds on an original upload are provenance, not
  permission. Check each source's terms and get a lawful basis before
  publishing; FOX 13 material in particular is subject to a restrictive reuse
  policy.
- **Every source crop is approximate.** The guide's research inspected
  timestamped storyboard samples plus metadata and auto-captions. Continuous
  picture and source audio were not reviewed. Fine-trim in the app, in context.
- **Upload date ≠ event date.** `C07` (uploaded Dec 9) describes the Dec 8
  search; `C18` (uploaded Dec 18) reports the Dec 17 hearing; `C17` (uploaded
  Oct 17) reports the Oct 16 sentencing; `C15` (uploaded Apr 29) is earlier
  family-appeal coverage, not the funeral.
- **`C17`'s title says the victim was 15.** The narration's correct age is 14.
  Do not copy the title's error into a label.
- This is a **proposed revision for approval**, not an applied edit. Nothing
  here changes a project, an approved plan, or an existing export.
