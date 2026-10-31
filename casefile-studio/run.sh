#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
  echo "FFmpeg and ffprobe are required. See README.md for setup." >&2
  exit 1
fi
# Use the local virtualenv when one exists, otherwise the system interpreter.
PYTHON=python
[ -x .venv/bin/python ] && PYTHON=.venv/bin/python
# serve.py binds one dual-stack socket so both IPv4 and IPv6 clients reach the app.
exec "$PYTHON" serve.py
