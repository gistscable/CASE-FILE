#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
# Prefer the local virtualenv created by setup-local.sh, so its Python and the
# ffmpeg/ffprobe symlinks are found even when the venv has not been activated.
if [ -d .venv/bin ]; then
  PATH="$(cd .venv/bin && pwd):$PATH"
  export PATH
fi
if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
  echo "FFmpeg and ffprobe are required. See README.md for setup." >&2
  exit 1
fi
exec python -m uvicorn app:app --host 0.0.0.0 --port "${PORT:-8000}"
