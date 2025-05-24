import cv2
import time
from ultralytics import YOLO
import torch

def main():
    model = YOLO('yolov8n.pt')
    model.fuse() 



    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam.")

    frame_counter = 0
    fps = 0
    start_time = time.time()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame, imgsz=320, verbose=False)
            boxes = results[0].boxes
            annotated_frame = frame.copy()

            if boxes is not None:
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = float(box.conf[0])
                    cls = int(box.cls[0])
                    label = f"{model.names[cls]} {conf:.2f}"
                    color = (0, 255, 0)
                    cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(annotated_frame, label, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            frame_counter += 1
            elapsed = time.time() - start_time
            if elapsed >= 1.0:
                fps = frame_counter / elapsed
                frame_counter = 0
                start_time = time.time()

            cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            cv2.imshow("YOLOv8 Real-Time Detection", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
