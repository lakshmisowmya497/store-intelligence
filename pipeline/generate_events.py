import json
from datetime import datetime

EVENTS_FILE = "../data/events.jsonl"

def save_event(visitor_id, event_type):

    event = {
        "visitor_id": visitor_id,
        "event_type": event_type,
        "timestamp": datetime.now().isoformat()
    }

    with open(EVENTS_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

    print("Saved:", event)


# Test events
save_event(11, "ENTRY")
save_event(11, "EXIT")