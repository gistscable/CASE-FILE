FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg fonts-dejavu-core gosu && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd --create-home --uid 10001 studio
COPY --chown=studio:studio . /app
# The entrypoint starts as root only to hand a mounted data disk (Render mounts
# it root-owned) to `studio`, then drops privileges before the server starts.
# With no mounted disk it runs as `studio` from the start.
RUN mkdir -p /app/data && chown -R studio:studio /app \
    && chmod +x /app/docker-entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]
# Bind to $PORT (Render's routing port, default 10000). One worker only: the app
# keeps in-flight jobs and AI sessions in process memory.
CMD ["sh", "-c", "exec python -m uvicorn app:app --host 0.0.0.0 --port ${PORT:-10000} --proxy-headers --forwarded-allow-ips=*"]
EXPOSE 10000
