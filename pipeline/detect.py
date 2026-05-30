from ultralytics import YOLO
import cv2
from pathlib import Path

# -----------------------------
# Project root folder
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Video path
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
# Get video properties
# -----------------------------
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# -----------------------------
# Create output video writer
# -----------------------------
output_path = BASE_DIR / "data" / "output_detection.mp4"

writer = cv2.VideoWriter(
    str(output_path),
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

# -----------------------------
# Process video
# -----------------------------
while True:
    ret, frame = cap.read()

    if not ret:
        print("Video finished.")
        break

    # Detect persons only
    results = model(frame, classes=[0])

    # Draw boxes
    annotated_frame = results[0].plot()

    # Save frame
    writer.write(annotated_frame)

    # Show video
    cv2.imshow("Store Intelligence Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
writer.release()
cv2.destroyAllWindows()

print("Output video saved at:")
print(output_path)