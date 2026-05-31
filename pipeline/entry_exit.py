from ultralytics import YOLO
import cv2
from pathlib import Path
from event_utils import save_event

# -----------------------------
# Project root folder
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Video path
video_path = BASE_DIR / "data" / "CAM3.mp4"

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open video
cap = cv2.VideoCapture(str(video_path))

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

print("Video opened successfully!")

# Store previous positions
track_history = {}

# Store already crossed IDs
crossed_ids = set()

# -----------------------------
# Process video
# -----------------------------
while True:

    ret, frame = cap.read()

    if not ret:
        print("Video finished.")
        break

    # Tracking
    results = model.track(
        frame,
        persist=True,
        classes=[0],
        conf=0.25
    )

    # Draw tracking boxes
    annotated_frame = results[0].plot()

    # -----------------------------
    # Draw Entry/Exit Line
    # -----------------------------
    height, width = annotated_frame.shape[:2]

    LINE_X = int(width * 0.75)

    cv2.line(
        annotated_frame,
        (LINE_X, 0),
        (LINE_X, height),
        (0, 0, 255),
        3
    )

    cv2.putText(
        annotated_frame,
        "ENTRY/EXIT LINE",
        (LINE_X - 180, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    # -----------------------------
    # Track person center points
    # -----------------------------
    if results[0].boxes.id is not None:

        boxes = results[0].boxes.xyxy.cpu().numpy()
        track_ids = results[0].boxes.id.cpu().numpy().astype(int)

        for box, track_id in zip(boxes, track_ids):

            x1, y1, x2, y2 = box

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            # Draw green center point
            cv2.circle(
                annotated_frame,
                (center_x, center_y),
                5,
                (0, 255, 0),
                -1
            )

            # First time seeing this ID
            if track_id not in track_history:
                track_history[track_id] = center_x

            previous_x = track_history[track_id]

            # -----------------------------
            # ENTRY Detection
            # Right -> Left
            # -----------------------------
            if (
                previous_x > LINE_X
                and center_x <= LINE_X
                and track_id not in crossed_ids
            ):
                print(f"ENTRY: Visitor {track_id}")
                save_event(track_id, "ENTRY")
                crossed_ids.add(track_id)

            # -----------------------------
            # EXIT Detection
            # Left -> Right
            # -----------------------------
            elif (
                previous_x < LINE_X
                and center_x >= LINE_X
                and track_id not in crossed_ids
            ):
                print(f"EXIT: Visitor {track_id}")
                save_event(track_id, "EXIT")
                crossed_ids.add(track_id)

            print(
                f"ID={track_id} "
                f"Previous={previous_x} "
                f"Current={center_x}"
            )

            # Update latest position
            track_history[track_id] = center_x

    # Show video
    cv2.imshow(
        "Entry Exit Detection",
        annotated_frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()

print("Program finished successfully!")