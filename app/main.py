from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
EVENTS_FILE = BASE_DIR / "data" / "events.jsonl"


# -----------------------------
# Home Endpoint
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "Store Intelligence API Running"
    }


# -----------------------------
# Metrics Endpoint
# -----------------------------
@app.get("/metrics")
def metrics():

    entries = 0
    exits = 0

    if EVENTS_FILE.exists():

        with open(EVENTS_FILE, "r") as f:

            for line in f:

                if not line.strip():
                    continue

                event = json.loads(line)

                if event["event_type"] == "ENTRY":
                    entries += 1

                elif event["event_type"] == "EXIT":
                    exits += 1

    return {
        "entries": entries,
        "exits": exits,
        "conversion_rate": round(
            (exits / entries * 100),
            2
        ) if entries > 0 else 0
    }


# -----------------------------
# Funnel Endpoint
# -----------------------------
@app.get("/funnel")
def funnel():

    return {
        "entered_store": 100,
        "visited_zone": 60,
        "reached_billing": 30,
        "purchased": 20
    }


# -----------------------------
# Anomalies Endpoint
# -----------------------------
@app.get("/anomalies")
def anomalies():

    return {
        "alerts": [
            {
                "type": "HIGH_TRAFFIC",
                "message": "Store traffic unusually high"
            }
        ]
    }