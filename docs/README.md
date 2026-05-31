# Store Intelligence

## Setup

```bash
pip install -r requirements.txt
```

## Run API

```bash
uvicorn app.main:app --reload
```

## Endpoints

### Metrics

GET /metrics

### Funnel

GET /funnel

### Anomalies

GET /anomalies

## Pipeline

1. Person Detection (YOLOv8)
2. Person Tracking (ByteTrack)
3. Entry/Exit Event Generation
4. Event Storage
5. Metrics API

## Assumptions

* CAM3 used as entrance camera.
* Right-to-left crossing indicates entry.
* Left-to-right crossing indicates exit.
