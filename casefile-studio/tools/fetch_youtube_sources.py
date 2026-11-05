#!/usr/bin/env python3
"""Fetch and rename the guide's YouTube source videos.

The Last Timeline guide names 21 original YouTube uploads (C01–C21). This tool
downloads each one with ``yt-dlp`` (or renames files you already downloaded) to
the canonical file name recorded in the manifest:

    {source_id}__{upload_date}__{uploader_slug}__{title_slug}__{video_id}.mp4

Example:
    C04__2024-05-09__tampapd__tampa-police-seek-persons-of-interest-in-jevario-buie-death__a0NS9AsqdeA.mp4

Why a tool and not committed files: the app itself never downloads YouTube
media (see EPISODE-WORKFLOW.md), the uploads are third-party news/police
material with no reuse licence established here, and the full set is several
GB. Downloads therefore land in ``sources/downloads/``, which is gitignored.
Keep the originals off git and put only the reviewed excerpts in
``data/media/<project-id>/`` when you actually edit.

Usage:
    python3 tools/fetch_youtube_sources.py list
    python3 tools/fetch_youtube_sources.py fetch                  # all 21
    python3 tools/fetch_youtube_sources.py fetch --ids C04,C05    # a subset
    python3 tools/fetch_youtube_sources.py rename --dir ~/Downloads/yt
    python3 tools/fetch_youtube_sources.py verify

Exit codes: 0 = everything asked for succeeded, 1 = at least one failure,
2 = usage/manifest/tooling problem (missing yt-dlp, bad manifest, unknown id).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
import unicodedata
from pathlib import Path

TOOL = Path(__file__).resolve()
STUDIO = TOOL.parent.parent
DEFAULT_MANIFEST = STUDIO / "examples" / "the-last-timeline" / "sources" / "manifest.json"
DEFAULT_OUT = STUDIO / "examples" / "the-last-timeline" / "sources" / "downloads"
TITLE_SLUG_MAX = 60
UPLOADER_SLUG_MAX = 40
VIDEO_ID_RE = re.compile(r"(?<![A-Za-z0-9_-])([A-Za-z0-9_-]{11})(?![A-Za-z0-9_-])")


# --------------------------------------------------------------------------
# naming
# --------------------------------------------------------------------------
def slug(value: str, max_len: int = TITLE_SLUG_MAX) -> str:
    """ASCII, lowercase, hyphen-separated, cut on a word boundary."""
    value = unicodedata.normalize("NFKD", str(value or ""))
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    if len(value) <= max_len:
        return value
    cut = value[:max_len]
    if "-" in cut:
        cut = cut[: cut.rfind("-")]
    return cut.strip("-")


def build_file_name(source: dict, ext: str = ".mp4") -> str:
    """Canonical file name for one manifest entry."""
    if not ext.startswith("."):
        ext = "." + ext
    parts = [
        source["id"],
        source["upload_date"],
        slug(source["uploader"], UPLOADER_SLUG_MAX),
        slug(source["title"], TITLE_SLUG_MAX),
        source["video_id"],
    ]
    return "__".join(p for p in parts if p) + ext


def match_video_id(name: str, video_ids: set[str]) -> str | None:
    """Return the manifest video id embedded in a file name, if any."""
    for token in VIDEO_ID_RE.findall(name):
        if token in video_ids:
            return token
    return None


def die(message: str, code: int = 2) -> None:
    """Print a usage/tooling problem to stderr and exit with that code."""
    print(message, file=sys.stderr)
    raise SystemExit(code)


def load_manifest(path: Path | str) -> dict:
    path = Path(path).expanduser()
    if not path.exists():
        die(f"manifest not found: {path}")
    manifest = json.loads(path.read_text())
    if not isinstance(manifest.get("sources"), list) or not manifest["sources"]:
        die(f"manifest has no sources: {path}")
    return manifest


def select_sources(manifest: dict, ids: str | None) -> list[dict]:
    sources = manifest["sources"]
    if not ids:
        return sources
    wanted = [part.strip().upper() for part in ids.replace(" ", ",").split(",") if part.strip()]
    by_id = {s["id"]: s for s in sources}
    blocked = {b["registry_id"]: b for b in manifest.get("blocked", [])}
    out, unknown = [], []
    for source_id in wanted:
        if source_id in by_id:
            out.append(by_id[source_id])
        elif source_id in blocked:
            die(
                f"{source_id} is a BLOCKED guide beat: the guide assigns it no source "
                f"range and no media exists to download ({blocked[source_id]['reason']})."
            )
        else:
            unknown.append(source_id)
    if unknown:
        die(f"unknown Source ID(s): {', '.join(unknown)} (expected C01–C21)")
    return out


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def human_size(num: float | int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if num < 1024 or unit == "TB":
            return f"{num:.1f} {unit}" if unit != "B" else f"{int(num)} B"
        num /= 1024
    return f"{num:.1f} TB"


def duration_text(seconds: float) -> str:
    seconds = int(round(seconds))
    return f"{seconds // 60}:{seconds % 60:02d}"


def find_yt_dlp(explicit: str | None) -> str | None:
    candidate = explicit or os.environ.get("YT_DLP")
    if candidate:
        resolved = shutil.which(candidate) or (candidate if Path(candidate).exists() else None)
        return resolved
    return shutil.which("yt-dlp")


def existing_file(out_dir: Path, source: dict) -> Path | None:
    path = out_dir / source["file_name"]
    if path.exists() and path.stat().st_size > 0:
        return path
    stem = path.with_suffix("")
    for sibling in sorted(out_dir.glob(stem.name + ".*")) if out_dir.exists() else []:
        if sibling.is_file() and sibling.stat().st_size > 0:
            return sibling
    return None


def ffprobe_duration(path: Path) -> float | None:
    probe = shutil.which("ffprobe")
    if not probe:
        return None
    try:
        result = subprocess.run(
            [probe, "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
            capture_output=True, text=True, timeout=120,
        )
        value = (result.stdout or "").strip()
        return float(value) if value else None
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------
def cmd_list(args) -> int:
    manifest = load_manifest(args.manifest)
    out_dir = Path(args.out).expanduser()
    sources = select_sources(manifest, args.ids)
    widths = max((len(s["file_name"]) for s in sources), default=40)
    print(f"manifest: {args.manifest}")
    print(f"downloads: {out_dir}\n")
    present = 0
    for source in sources:
        found = existing_file(out_dir, source)
        if found:
            present += 1
            status = f"have ({human_size(found.stat().st_size)})"
        else:
            status = "missing"
        print(f'{source["id"]}  {duration_text(source["duration_seconds"]):>6}  {source["upload_date"]}  '
              f'{status:<20}  {source["file_name"]}')
    guide = manifest.get("guide", {})
    print(f"\n{len(sources)} sources listed, {present} already downloaded. "
          f'{guide.get("blocked_placements", len(manifest.get("blocked", [])))} guide beats are BLOCKED '
          f'(registry ids G003–G104) and have no media at all.')
    print(f'Runtime of the full set: {duration_text(sum(s["duration_seconds"] for s in sources))}.')
    return 0


def cmd_fetch(args) -> int:
    manifest = load_manifest(args.manifest)
    out_dir = Path(args.out).expanduser()
    sources = select_sources(manifest, args.ids)
    yt_dlp = find_yt_dlp(args.yt_dlp)
    if not yt_dlp:
        print("yt-dlp not found. Install it (pipx install yt-dlp, brew install yt-dlp, "
              "or pip install --user yt-dlp) and re-run, or pass --yt-dlp /path/to/yt-dlp.",
              file=sys.stderr)
        return 2

    incoming = out_dir / ".incoming"
    incoming.mkdir(parents=True, exist_ok=True)
    height = f"[height<={args.max_height}]" if args.max_height else ""
    fmt = args.format or (
        f"bv*[ext=mp4]{height}+ba[ext=m4a]/b[ext=mp4]{height}/bv*{height}+ba/b"
    )

    log = {
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "manifest": str(args.manifest),
        "out_dir": str(out_dir),
        "format": fmt,
        "results": [],
    }
    failures: list[str] = []
    for index, source in enumerate(sources, start=1):
        label = f'[{index}/{len(sources)}] {source["id"]} {source["title"][:60]}'
        found = None if args.force else existing_file(out_dir, source)
        if found:
            print(f"{label}\n    already present: {found.name}")
            log["results"].append({"id": source["id"], "status": "skipped",
                                   "path": str(found), "bytes": found.stat().st_size})
            continue

        target = out_dir / source["file_name"]
        command = [
            yt_dlp,
            "--no-playlist",
            "--no-progress",
            "--newline",
            "--socket-timeout", str(args.socket_timeout),
            "--retries", "3",
            "--merge-output-format", "mp4",
            "-f", fmt,
            "-o", str(incoming / "%(id)s.%(ext)s"),
        ]
        if args.cookies_from_browser:
            command += ["--cookies-from-browser", args.cookies_from_browser]
        if args.cookies:
            command += ["--cookies", args.cookies]
        command.append(source["url"])

        print(f"{label}\n    {source['url']}")
        started = time.time()
        try:
            result = subprocess.run(command, capture_output=True, text=True)
        except OSError as exc:  # yt-dlp vanished between check and run
            print(f"    could not run yt-dlp: {exc}", file=sys.stderr)
            failures.append(source["id"])
            log["results"].append({"id": source["id"], "status": "failed", "error": str(exc)})
            continue

        if result.returncode != 0:
            tail = (result.stderr or result.stdout or "").strip().splitlines()[-4:]
            print("    download failed:\n      " + "\n      ".join(tail), file=sys.stderr)
            failures.append(source["id"])
            log["results"].append({"id": source["id"], "status": "failed",
                                   "error": "\n".join(tail)})
            continue

        produced = [
            path for path in incoming.iterdir()
            if path.is_file() and source["video_id"] in path.name
        ]
        if not produced:
            print("    yt-dlp reported success but no matching file was produced", file=sys.stderr)
            failures.append(source["id"])
            log["results"].append({"id": source["id"], "status": "failed",
                                   "error": "no output file"})
            continue

        produced.sort(key=lambda p: p.stat().st_size, reverse=True)
        renamed = produced[0]
        os.replace(renamed, target)
        for leftover in produced[1:]:
            leftover.unlink(missing_ok=True)
        size = target.stat().st_size
        elapsed = time.time() - started
        print(f"    saved {target.name} ({human_size(size)}, {elapsed:.0f}s)")
        log["results"].append({
            "id": source["id"], "status": "downloaded", "path": str(target),
            "bytes": size, "seconds": round(elapsed, 1),
        })

    log["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    log_path = Path(args.log).expanduser() if args.log else out_dir / "download-log.json"
    log_path.write_text(json.dumps(log, indent=2) + "\n")

    downloaded = sum(1 for r in log["results"] if r["status"] == "downloaded")
    skipped = sum(1 for r in log["results"] if r["status"] == "skipped")
    print(f"\n{downloaded} downloaded, {skipped} already present, {len(failures)} failed.")
    print(f"log: {log_path}")
    print("These files are third-party material with no reuse licence established; "
          "keep downloads/ out of git and only import cleared excerpts into a project.")
    return 1 if failures else 0


def cmd_rename(args) -> int:
    manifest = load_manifest(args.manifest)
    source_dir = Path(args.dir).expanduser()
    if not source_dir.is_dir():
        print(f"not a directory: {source_dir}", file=sys.stderr)
        return 2
    default_out = Path(DEFAULT_OUT).expanduser()
    requested = Path(args.out).expanduser()
    out_dir = requested if requested != default_out else source_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    by_video_id = {s["video_id"]: s for s in manifest["sources"]}

    renamed = skipped = unmatched = 0
    for path in sorted(p for p in source_dir.rglob("*") if p.is_file()):
        if path.name == "download-log.json" or path.suffix.lower() in {
            ".json", ".txt", ".md", ".srt", ".vtt", ".part", ".ytdl", ".temp",
        }:
            continue  # sidecars and half-finished downloads are not media yet
        video_id = match_video_id(path.name, set(by_video_id))
        if not video_id:
            unmatched += 1
            continue
        source = by_video_id[video_id]
        target = out_dir / build_file_name(source, path.suffix.lower())
        if path.resolve() == target.resolve():
            skipped += 1
            continue
        if target.exists() and target.stat().st_size >= path.stat().st_size:
            skipped += 1
            print(f'keep   {target.name} (already the larger copy)')
            continue
        os.replace(path, target)
        renamed += 1
        print(f'rename {path.name}\n    -> {target.name}')
    print(f"\n{renamed} renamed, {skipped} already correct, {unmatched} file(s) with no matching source id.")
    if unmatched and not renamed:
        print("Files without a YouTube id in the name cannot be matched safely; "
              "rename them by hand using sources.csv.")
    return 0


def cmd_verify(args) -> int:
    manifest = load_manifest(args.manifest)
    out_dir = Path(args.out).expanduser()
    sources = select_sources(manifest, args.ids)
    problems = 0
    for source in sources:
        found = existing_file(out_dir, source)
        if not found:
            print(f'{source["id"]}  MISSING   {source["file_name"]}')
            problems += 1
            continue
        expected = source["duration_seconds"]
        actual = ffprobe_duration(found)
        if actual is None:
            print(f'{source["id"]}  ok (no ffprobe)  {human_size(found.stat().st_size)}  {found.name}')
            continue
        tolerance = max(2.0, expected * args.tolerance)
        if abs(actual - expected) > tolerance:
            print(f'{source["id"]}  DURATION  expected {duration_text(expected)}, '
                  f'got {duration_text(actual)}  {found.name}')
            problems += 1
        else:
            print(f'{source["id"]}  ok  {duration_text(actual)}  {human_size(found.stat().st_size)}  {found.name}')
    print(f"\n{len(sources) - problems}/{len(sources)} sources verified.")
    return 1 if problems else 0


def main(argv: list[str] | None = None) -> int:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--manifest", default=str(DEFAULT_MANIFEST),
                        help="path to sources/manifest.json")
    common.add_argument("--out", default=str(DEFAULT_OUT),
                        help="download directory (gitignored by default)")
    common.add_argument("--ids", help="comma-separated Source IDs, e.g. C01,C04")

    parser = argparse.ArgumentParser(
        description="Download and rename the guide's YouTube sources to canonical names.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="command")

    listing = sub.add_parser("list", parents=[common],
                             help="show each source, its file name and whether it is downloaded")
    listing.set_defaults(func=cmd_list)

    fetch = sub.add_parser("fetch", parents=[common],
                           help="download with yt-dlp and rename to the canonical name")
    fetch.add_argument("--yt-dlp", help="path to the yt-dlp binary")
    fetch.add_argument("--format", help="yt-dlp -f selector (default: best mp4 up to --max-height)")
    fetch.add_argument("--max-height", type=int, help="cap resolution, e.g. 720")
    fetch.add_argument("--force", action="store_true", help="re-download even if the file is present")
    fetch.add_argument("--cookies", help="cookies.txt for age/region-gated uploads")
    fetch.add_argument("--cookies-from-browser", help="e.g. chrome, firefox")
    fetch.add_argument("--socket-timeout", type=int, default=30)
    fetch.add_argument("--log", help="write the run log here (default: <out>/download-log.json)")
    fetch.set_defaults(func=cmd_fetch)

    rename = sub.add_parser("rename", parents=[common],
                            help="rename files you already downloaded, matching on YouTube id")
    rename.add_argument("--dir", required=True, help="directory to scan")
    rename.set_defaults(func=cmd_rename)

    verify = sub.add_parser("verify", parents=[common],
                            help="check presence and (with ffprobe) duration")
    verify.add_argument("--tolerance", type=float, default=0.02,
                        help="allowed duration difference as a fraction (default 0.02)")
    verify.set_defaults(func=cmd_verify)

    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return 2
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
