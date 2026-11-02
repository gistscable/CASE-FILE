#!/usr/bin/env sh
# Password-free local setup for Casefile Studio (Linux x86_64, macOS Intel/ARM).
#
# No sudo / no apt / no Homebrew / no system-wide changes: everything goes into
# .venv/, which is already gitignored. It puts a static FFmpeg 7 and ffprobe on
# the venv's PATH so ./run.sh can find them.
#
# Prerequisites: Python 3.11+ (as `python3`) and Node/npm.
# Usage:  sh ./setup-local.sh   then   sh ./run.sh
set -eu
cd "$(dirname "$0")"

OS=$(uname -s)
ARCH=$(uname -m)
case "$OS:$ARCH" in
  Linux:x86_64|Linux:amd64) FFPROBE_PKG="@ffprobe-installer/linux-x64" ;;
  Darwin:x86_64)            FFPROBE_PKG="@ffprobe-installer/darwin-x64" ;;
  Darwin:arm64)             FFPROBE_PKG="@ffprobe-installer/darwin-arm64" ;;
  *)
    echo "No prebuilt binaries configured for $OS/$ARCH." >&2
    echo "On Windows, run this inside WSL; otherwise install ffmpeg + ffprobe" >&2
    echo "with your package manager and follow README.md instead." >&2
    exit 1
    ;;
esac

command -v python3 >/dev/null 2>&1 || { echo "Python 3.11+ is required as 'python3'." >&2; exit 1; }
python3 -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)' || {
  echo "Python 3.11+ is required (found $(python3 -V 2>&1))." >&2
  exit 1
}
command -v npm >/dev/null 2>&1 || { echo "npm is required (the repo already uses Node for the UI build)." >&2; exit 1; }

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
. .venv/bin/activate

pip install --disable-pip-version-check -q -r requirements.txt
# 0.6.0 ships FFmpeg 7.x, the major version this renderer was tested against.
# It has manylinux x86_64 and macOS x86_64 / arm64 wheels.
pip install --disable-pip-version-check -q "imageio-ffmpeg==0.6.0"
# The ffprobe-installer packages contain a prebuilt binary in the npm tarball;
# nothing is downloaded from outside the registry at install time.
npm install --no-audit --no-fund --prefix .venv/opt "$FFPROBE_PKG" >/dev/null

FFMPEG=$(python -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())")
FFPROBE=$(find .venv/opt/node_modules -type f -name ffprobe -print -quit)
if [ -z "$FFPROBE" ]; then
  echo "Could not locate the downloaded ffprobe binary." >&2
  exit 1
fi
# Symlinks in .venv/bin resolve relative to that directory, so use absolute paths.
case "$FFPROBE" in /*) ;; *) FFPROBE="$PWD/$FFPROBE" ;; esac
case "$FFMPEG" in /*) ;; *) FFMPEG="$PWD/$FFMPEG" ;; esac
chmod +x "$FFMPEG" "$FFPROBE"
if [ "$OS" = "Darwin" ]; then
  # Unsigned binaries unpacked by pip/npm can be blocked by Gatekeeper.
  xattr -d com.apple.quarantine "$FFMPEG" 2>/dev/null || true
  xattr -d com.apple.quarantine "$FFPROBE" 2>/dev/null || true
fi
ln -sf "$FFMPEG" .venv/bin/ffmpeg
ln -sf "$FFPROBE" .venv/bin/ffprobe
command -v ffmpeg >/dev/null || { echo "ffmpeg was not linked into .venv/bin." >&2; exit 1; }
command -v ffprobe >/dev/null || { echo "ffprobe was not linked into .venv/bin." >&2; exit 1; }

if [ ! -f /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf ]; then
  echo "Note: no system DejaVu Sans at the Linux path. renderer.py falls back to" >&2
  echo "      the bundled DM Sans font; set CASEFILE_FONT_DIR to a directory" >&2
  echo "      holding DejaVuSans.ttf / DejaVuSans-Bold.ttf to override it." >&2
fi

ffmpeg -version | head -1
ffprobe -version | head -1
echo "Setup complete. Start the app with:  sh ./run.sh"
echo "Then open http://localhost:8000"
