#!/bin/sh
# Container entrypoint.
#
# Two things happen here:
#
# 1. Data directory permissions. Render mounts a persistent disk owned by root,
#    while the app runs as the unprivileged `studio` user. When the disk is
#    mounted we hand the storage root to `studio` and then drop privileges.
#    Without a disk the container runs as `studio` from the start, unchanged.
#
# The default CMD binds to ${PORT:-10000}, which covers both Render routing and
# plain `docker run`.
set -eu

APP_USER=studio
DATA_DIR="${CASEFILE_DATA_DIR:-/app/data}"

as_root=no
[ "$(id -u)" = "0" ] && as_root=yes

if [ "$as_root" = "yes" ]; then
  mkdir -p "$DATA_DIR"
fi

# First boot on a fresh disk: copy the projects/exports shipped in the image
# into the empty storage root so the included workspace is present. Later
# deploys keep whatever is already on the disk.
if [ "$DATA_DIR" != "/app/data" ] && [ ! -e "$DATA_DIR/.volume-initialized" ]; then
  if [ -z "$(ls -A "$DATA_DIR" 2>/dev/null)" ] && [ -d /app/data ]; then
    echo "entrypoint: seeding $DATA_DIR from the image's /app/data"
    cp -a /app/data/. "$DATA_DIR"/
  fi
  touch "$DATA_DIR/.volume-initialized" 2>/dev/null || true
fi

if [ "$as_root" = "yes" ]; then
  if [ "$(stat -c %u "$DATA_DIR" 2>/dev/null || echo 0)" != "$(id -u "$APP_USER")" ]; then
    echo "entrypoint: handing $DATA_DIR to $APP_USER"
    chown -R "$APP_USER:$APP_USER" "$DATA_DIR"
  fi
fi

# Point the app at the storage root unless the image default already applies.
if [ "$DATA_DIR" != "/app/data" ] || [ "$as_root" = "yes" ]; then
  export CASEFILE_DATA_DIR="$DATA_DIR"
fi

if [ "$as_root" = "yes" ]; then
  exec gosu "$APP_USER" "$@"
fi
exec "$@"
