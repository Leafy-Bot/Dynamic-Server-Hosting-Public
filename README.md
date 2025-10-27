# LHS Panel & Agent (Basic)

Small control panel (Flask) and a simple agent (C++ HTTP server) to start/stop a Docker container and report status.

## Contents
- Panel: Main\Panel\index.html, app.py (Flask web UI)
- Agent: Main\CDaemon\main.cpp (HTTP endpoints at port 9000)

## Prerequisites
- Python 3.8+ and pip
- Flask and requests (Python packages)
- A C++ toolchain (g++/MSVC) and cpp-httplib (single-header library) for the agent
- Docker installed and running
- Administrator or elevated privileges if binding to port 80

## Install (Panel)
1. Open a terminal in Main\Panel
2. Create a venv and install deps:
   - python -m venv .venv
   - .venv\Scripts\activate
   - pip install flask requests
3. Run the panel:
   - python app.py
4. Open http://localhost/ (or http://localhost:80)

## Build & Run (Agent)
1. Open a terminal in Main\CDaemon
2. Ensure cpp-httplib single-header is available (include path)
3. Build (example with g++):
   - g++ main.cpp -std=c++17 -pthread -o agent
4. Run the agent:
   - .\agent.exe
   The agent listens on http://0.0.0.0:9000 and exposes /start, /stop, /status used by the panel.

## Endpoints used by the panel
- POST /start -> forwards to agent POST /start
- POST /stop  -> forwards to agent POST /stop
- GET /status -> forwards to agent GET /status (panel auto-updates every 5s)

## Notes / TODO
- app.py in the repo has minor bugs (Flask import/initialization and duplicated function names). Fix Flask import to `from flask import Flask, render_template, request` and `app = Flask(__name__)`. Ensure stop handler returns an appropriate message.
- main.cpp uses container names inconsistently (e.g., `McTest` vs `mc-test`). Align names used for run/stop/remove.
- Binding the Flask app to port 80 may require administrative privileges — consider using a higher port for development (e.g., 5000).

## License
Add a license file as needed.