# Engineering Decisions and Trade-offs

## YOLOv8n Selection

YOLOv8n was selected because it provides a good balance between speed and accuracy for real-time CCTV processing.

## Tracking Approach

ByteTrack was used through Ultralytics tracking support because it provides stable visitor IDs across frames.

## Event Storage

JSONL was chosen instead of a database during initial implementation because:

* Simple to inspect
* Easy to debug
* Lightweight
* Sufficient for challenge scale

## Entry/Exit Detection

A virtual line-crossing approach was used.

Advantages:

* Simple implementation
* Easy to explain
* Computationally efficient

Limitations:

* Sensitive to line placement
* Requires camera-specific calibration

## API Design

FastAPI was chosen because:

* Lightweight
* High performance
* Automatic API documentation
* Easy Docker deployment

## Future Improvements

* Zone-level analytics
* SQLite/PostgreSQL persistence
* Heatmaps
* Staff filtering
* Re-entry detection
* Multi-camera identity association
