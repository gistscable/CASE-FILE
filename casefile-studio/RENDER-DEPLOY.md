# Hosting Casefile Studio on Render

The repo ships a [Render Blueprint](https://render.com/docs/blueprint-spec) at
`render.yaml` (repo root). It builds `casefile-studio/Dockerfile` and creates one
web service with a persistent disk.

## Deploy

1. Push this branch to GitHub.
2. In the Render Dashboard: **New → Blueprint**, pick the `gistscable/CASE-FILE`
   repo, and select the branch you want to deploy.
3. Render reads `render.yaml`, builds the image, and starts the service.
   First build takes a few minutes (apt + pip + a ~160 MB image).
4. Open the `onrender.com` URL. `GET /healthz` should return
   `{"ok": true, ...}`.

## What the blueprint does

| Setting | Value | Why |
| --- | --- | --- |
| `runtime` | `docker` | The renderer shells out to `ffmpeg`/`ffprobe` and draws captions with DejaVu fonts. The Dockerfile installs both; Render's native Python runtime does not. |
| `rootDir` | `casefile-studio` | Docker paths resolve relative to the root directory. This also keeps the 90 MB proof videos at the repo root out of the build context. |
| `healthCheckPath` | `/healthz` | Cheap, media-free liveness endpoint. |
| `plan` | `starter` | The smallest instance type that can attach a persistent disk. |
| `envVars.CASEFILE_DATA_DIR` | `/var/data` | Points the app's storage root at the disk. |
| `disk.mountPath` | `/var/data` | Must match `CASEFILE_DATA_DIR`. Size is 10 GB. |

### Storage layout

`CASEFILE_DATA_DIR` (default: `casefile-studio/data`) holds everything the app
writes: `projects/`, `media/` (uploads), `exports/` (rendered MP4s and
sidecars), and `jobs/`.

On Render the disk starts empty. On first boot `docker-entrypoint.sh` copies the
projects and exports baked into the image into `/var/data`, drops a
`.volume-initialized` marker, and never copies again. Later deploys keep
whatever is already on the disk, so producer uploads and renders survive
redeploys and restarts.

Asset paths are stored relative to the checkout when the file lives inside it,
and as absolute paths when it lives on the disk. Both forms are validated
against the code root and the data root, so a crafted path cannot reach outside
them.

### Disk permissions

Render mounts persistent disks owned by `root`, while the app runs as the
unprivileged `studio` user. The entrypoint therefore starts as root only long
enough to `chown` the storage root to `studio`, then drops privileges with
`gosu` before the server starts. With no disk attached it runs as `studio` from
the start.

### Port

The container's default command is

```
python -m uvicorn app:app --host 0.0.0.0 --port ${PORT:-10000} --proxy-headers --forwarded-allow-ips=*
```

Render routes traffic to `$PORT` (default `10000`). Keep it to **one uvicorn
worker**: in-flight render jobs and connected AI keys live in process memory.

## Free tier instead of a disk

Free web services cannot attach a persistent disk. To try the app on Free,
delete the `disk:` block and the `CASEFILE_DATA_DIR` env var from `render.yaml`
and set `plan: free`. The service still boots and the included workspace is
seeded from the image, but it spins down after 15 minutes idle, and every
redeploy or spin-up starts from the image again: producer uploads and renders
will not survive.

## Settings that matter at runtime

- **No AI key is required.** Local editing and rendering work without one. AI
  features need a key entered in the app's Settings, which is held in server
  memory per browser session, not in the repo or the environment.
- **Uploads** are capped by the app at 512 MB per file, 30 files per batch. Long
  uploads and multi-minute renders run as background jobs, so the browser is not
  waiting on one request. Render still applies its own proxy request timeout, so
  a very slow single upload can be cut off; retry with fewer/smaller files.
- **Renders are CPU-bound.** The `starter` plan is 0.5 CPU, which is slow for
  20–40 minute episodes. Use a larger plan (`standard`/`2c-4g` or above) for
  real episode work. Only one render runs at a time (`RENDER_LOCK`).
- **Restarting or redeploying interrupts in-flight jobs.** They are marked
  `interrupted` on boot and must be re-run.

## Verify a deploy

```bash
curl -s https://<service>.onrender.com/healthz
# {"ok":true,"version":"0.4.13","render":true}

curl -s https://<service>.onrender.com/api/bootstrap | head -c 200
```

`"render": true` in `/healthz` confirms `ffmpeg` is on `PATH` inside the
container. If it is `false`, episode rendering will fail even though the UI
loads.

## Local container test

```bash
cd casefile-studio
docker build -t casefile-studio .
# No disk: runs as `studio`, data inside the container.
docker run --rm -p 8000:10000 casefile-studio
# With a disk, emulating Render's root-owned mount:
mkdir -p /tmp/casefile-data
docker run --rm -p 8000:10000 -v /tmp/casefile-data:/var/data \
  -e CASEFILE_DATA_DIR=/var/data casefile-studio
```

## Tests

```bash
cd casefile-studio
python -m pytest tests/ -q \
  --ignore=tests/browser_episode.py --ignore=tests/browser_production.py \
  --ignore=tests/browser_smoke.py --ignore=tests/long_render_check.py
```

`tests/test_deployment.py` pins this contract: the storage root follows
`CASEFILE_DATA_DIR`, asset paths round-trip from either location, path traversal
is refused, `/healthz` stays cheap, and `render.yaml` keeps the disk mount and
`CASEFILE_DATA_DIR` in agreement.
