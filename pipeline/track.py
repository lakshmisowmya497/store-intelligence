from ultralytics import YOLO
import cv2
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Input video
video_path = BASE_DIR / "data" / "CAM3.mp4"

# Output video
output_path = BASE_DIR / "data" / "tracking_output.mp4"

# Load model
model = YOLO("yolov8n.pt")

# Open video
cap = cv2.VideoCapture(str(video_path))

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create output writer
writer = cv2.VideoWriter(
    str(output_path),
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

print("Processing video...")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Tracking
    results = model.track(
        frame,
        persist=True,
        classes=[0],
        conf=0.25
    )

    # Draw IDs and boxes
    annotated_frame = results[0].plot()

    # Save frame
    writer.write(annotated_frame)

    # Show video
    cv2.imshow("Tracking", annotated_frame)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
writer.release()
cv2.destroyAllWindows()

print("Tracking video saved successfully!")
print(output_path)