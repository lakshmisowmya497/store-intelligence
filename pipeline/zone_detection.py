from ultralytics import YOLO
import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

video_path = BASE_DIR / "data" / "CAM3.mp4"

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(str(video_path))

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(
        frame,
        persist=True,
        classes=[0],
        conf=0.25
    )

    annotated_frame = results[0].plot()

    # Test Zone
    ZONE_X1 = 150
    ZONE_Y1 = 100

    ZONE_X2 = 500
    ZONE_Y2 = 350

    cv2.rectangle(
        annotated_frame,
        (ZONE_X1, ZONE_Y1),
        (ZONE_X2, ZONE_Y2),
        (255, 0, 0),
        3
    )

    cv2.putText(
        annotated_frame,
        "TEST_ZONE",
        (ZONE_X1, ZONE_Y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    cv2.imshow("Zone Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()