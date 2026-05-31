import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

EVENTS_FILE = BASE_DIR / "data" / "events.jsonl"

def save_event(visitor_id, event_type):

    event = {
        "visitor_id": visitor_id,
        "event_type": event_type,
        "timestamp": datetime.now().isoformat()
    }

    with open(EVENTS_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

    print("Saved:", event)