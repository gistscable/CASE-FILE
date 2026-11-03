# Hosting Casefile Studio on Render

The repo ships a [Render Blueprint](https://render.com/docs/blueprint-spec) at
`render.yaml` (repo root). It builds `casefile-studio/Dockerfile` and creates one
web service.

> **Use the Blueprint, not "New → Web Service".**
> A service created by hand ignores `render.yaml` entirely. It builds from the
> repo root with Render's default Python build command and fails with
> `Exited with status 1 while building your code` because `requirements.txt`
> lives in `casefile-studio/`, not at the root. See
> [If you already created a service by hand](#if-you-already-created-a-service-by-hand).

## Deploy

1. Merge this branch to `main`.
2. In the Render Dashboard: **New → Blueprint**, pick the `gistscable/CASE-FILE`
   repo, and select `main` (or the branch containing `render.yaml`).
3. Render asks for two environment values (`BASIC_AUTH_USER`,
   `BASIC_AUTH_PASSWORD`). **Fill both in** — they become the username and
   password the browser asks for when opening the site. The app has no login
   of its own; leaving these empty means anyone who finds the URL can open,
   edit, and download your projects. (Both empty = gate off, for local runs.)
4. Render reads `render.yaml`, builds the image, and starts the service. First
   build takes a few minutes on Free (apt + pip).
5. Open the `onrender.com` URL. `GET /healthz` should return
   `{"ok": true, ...}`.

## If you already created a service by hand

This is what the failed deploy in the Render dashboard is. Its source is
`ba4176f` from the merged `arena/80ddbdde-case-file` branch, with no root
directory and no Dockerfile, so the build could not find `requirements.txt`.

Pick one:

- **Recommended — delete and recreate as a Blueprint.** Service **Settings →
  Delete Web Service**, then **New → Blueprint** as above. This gives you the
  Docker image (with `ffmpeg`) and the `/healthz` health check.
- **Or patch the existing service by hand.** In **Settings**: set **Language**
  to *Docker*, **Root Directory** to `casefile-studio`, **Dockerfile Path** to
  `./Dockerfile`, **Docker Build Context Directory** to `.`, and **Health Check
  Path** to `/healthz`. Also switch the tracked branch from the merged feature
  branch to `main`, or it will keep deploying the old code.

## What the blueprint does

| Setting | Value | Why |
| --- | --- | --- |
| `runtime` | `docker` | The renderer shells out to `ffmpeg`/`ffprobe` and draws captions with DejaVu fonts. The Dockerfile installs both; Render's native Python runtime does not. |
| `rootDir` | `casefile-studio` | The app, `requirements.txt`, and `Dockerfile` are all in this subdirectory. Docker paths resolve relative to it, and it keeps the large proof videos at the repo root out of the build context. |
| `healthCheckPath` | `/healthz` | Cheap, media-free liveness endpoint. |
| `plan` | `free` | Works out of the box. See storage below for the tradeoff. |

### Storage: what survives

The storage root is `CASEFILE_DATA_DIR` if set, otherwise `casefile-studio/data`
inside the image. It holds `projects/`, `media/` (uploads), `exports/` (rendered
MP4s and sidecars), and `jobs/`.

On the **Free plan** there is no persistent disk, so:

- The image ships the committed projects and exports, so the app is fully usable
  on every boot — the demo project, `Bismilah`, and the earlier cases.
- **Uploads, new projects, and renders are lost** on redeploy, restart, or when
  Render spins the service down after 15 minutes idle.

To keep producer data, upgrade the instance to `starter` (the smallest plan that
supports a disk) and switch on the commented block in `render.yaml`:

```yaml
plan: starter
envVars:
  - key: CASEFILE_DATA_DIR
    value: /var/data
disk:
  name: casefile-data
  mountPath: /var/data
  sizeGB: 10
```

On first boot with a disk, `docker-entrypoint.sh` copies the image's workspace
onto the empty disk, drops a `.volume-initialized` marker, and never copies
again. Later deploys keep whatever is on the disk.

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

## Settings that matter at runtime

- **No AI key is required.** Local editing and rendering work without one. AI
  features need a key entered in the app's Settings, which is held in server
  memory per browser session, not in the repo or the environment.
- **Cold starts.** A free instance spins down after 15 minutes without traffic
  and takes ~50 seconds to answer the next request.
- **Uploads** are capped by the app at 512 MB per file, 30 files per batch. Long
  uploads and multi-minute renders run as background jobs, so the browser is not
  waiting on one request. Render still applies its own proxy request timeout, so
  a very slow single upload can be cut off; retry with fewer/smaller files.
- **Renders are CPU-bound.** Free and `starter` are 0.5 CPU, which is slow for
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

`"render": true` confirms `ffmpeg` is on `PATH` inside the container. If it is
`false`, episode rendering will fail even though the UI loads.

## Local container test

```bash
cd casefile-studio
docker build -t casefile-studio .
# Free-plan behaviour: data inside the image, nothing persists.
docker run --rm -p 8000:10000 casefile-studio
# Disk behaviour, emulating Render's root-owned mount:
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
is refused, `/healthz` stays cheap, and the blueprint keeps `rootDir` and the
disk mount consistent.
