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
        classes=[0]
    )

    annotated_frame = results[0].plot()

    cv2.imshow("Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()