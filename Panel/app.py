from flask import flash, render_template, request
import requests

AGENT_URL = "http://localhost:9000"

app = flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/start")
def start_srv():
    requests.post(f"{AGENT_URL}/start")
    return "Started<br><a href='/'>Back</a>"

@app.post("/stop")
def start_srv():
    requests.post(f"{AGENT_URL}/stop")
    return "Started<br><a href='/'>Back</a>"

@app.get("/status")
def status_srv():
    status = requests.get(f"{AGENT_URL}/status").json()
    return f"Status: {status['status']}<br><a href='/'>Back</a>"

app.run(port=80)