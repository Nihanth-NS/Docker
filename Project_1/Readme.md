This project is a minimal Flask REST API served by Gunicorn and containerized with Docker following production‑minded best practices:

Non‑root user at runtime
Deterministic dependency layers
Proper port binding
Graceful shutdown & PID‑1 handling
Health endpoint for probes


Endpoints:

GET /api/hello → returns JSON greeting
GET /healthz → liveness/readiness probe



📁 Project Structure
.
├── app.py
├── requirements.txt
└── Dockerfile



Base image: python:3.12-slim → Smaller and safer than Ubuntu; Python preinstalled.
No virtualenv: A container image is already an isolated environment; venv adds complexity and size.
Layer caching: Copy requirements.txt before code → avoids reinstalling deps on every small code change.
Non‑root user: Reduces blast radius if app is compromised.
EXPOSE 8000: Documentation only; you still map ports with -p.
Gunicorn: Production WSGI server; Flask’s built‑in server is for development only.
