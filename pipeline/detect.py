from ultralytics import YOLO
import cv2
from pathlib import Path

# -----------------------------
# Get project root directory
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# CCTV video path
video_path = BASE_DIR / "data" / "CAM3.mp4"

print("Video path:", video_path)
print("Exists:", video_path.exists())

# -----------------------------
# Load YOLO model
# -----------------------------
model = YOLO("yolov8n.pt")

# -----------------------------
# Open video
# -----------------------------
cap = cv2.VideoCapture(str(video_path))

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

print("Video opened successfully!")

# -----------------------------
# Process frames
# -----------------------------
while True:
    ret, frame = cap.read()

    if not ret:
        print("Video finished.")
        break

    # Detect only persons (class 0)
    results = model(frame, classes=[0])

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Show video
    cv2.imshow("Store Intelligence Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()