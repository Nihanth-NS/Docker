from flask import Flask, jsonify
import signal
import sys
import time

app = Flask(__name__)
shutting_down = False

@app.route("/healthz")
def healthz():
    status = 503 if shutting_down else 200
    return ("ok" if status == 200 else "shutting_down"), status

@app.route("/api/hello")
def hello():
    return jsonify(message="Hello from Flask API")

def handle_sigterm(signum, frame):
    global shutting_down
    shutting_down = True
    # simulate cleanup
    time.sleep(1)
    sys.exit(0)

if __name__ == "__main__":
    # For local testing: python app.py
    signal.signal(signal.SIGTERM, handle_sigterm)
    signal.signal(signal.SIGINT, handle_sigterm)
    app.run(host="0.0.0.0", port=8000)
