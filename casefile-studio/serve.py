"""Run Casefile Studio on a single dual-stack socket (IPv4 and IPv6, same port).

`uvicorn --host 0.0.0.0` listens on IPv4 only, and `--host ::` on this image
came up IPv6-only. Neither accepts a proxy that dials `localhost` and resolves
the other family, which makes a live preview look dead while `127.0.0.1` works.
Binding one AF_INET6 socket with IPV6_V6ONLY=0 serves both.

Usage:  PORT=8123 python serve.py
"""

from __future__ import annotations

import os
import socket
import sys

PORT = int(os.environ.get("PORT", "8000"))
HOST = os.environ.get("HOST", "::")

# The ASGI app ("app:app") lives next to this file, not in Python's default path.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
sock.bind((HOST, PORT))
sock.listen(2048)
sock.set_inheritable(True)

import uvicorn  # noqa: E402  (import after the socket so failures are obvious)

uvicorn.run(
    "app:app",
    fd=sock.fileno(),
    proxy_headers=True,
    forwarded_allow_ips="*",
    log_level=os.environ.get("LOG_LEVEL", "info"),
)
