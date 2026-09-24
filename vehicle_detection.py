import cv2
from ultralytics import YOLO


def detect_vehicles(video_path):
    model = YOLO("yolo11n.pt")

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Unable to open video.")
        return 0

    total_vehicle_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.resize(frame, (800, 450))

        results = model(frame, verbose=False)

        vehicle_count = 0

        # Vehicle classes:
        # 2 = car
        # 3 = motorcycle
        # 5 = bus
        # 7 = truck
        vehicle_classes = [2, 3, 5, 7]

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])

                if class_id in vehicle_classes:

                    vehicle_count += 1

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

        total_vehicle_count = max(total_vehicle_count, vehicle_count)

        cv2.putText(
            frame,
            f"Vehicles: {vehicle_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "AI Traffic Vehicle Detection",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    return total_vehicle_count


if __name__ == "__main__":
    video_path = r"data/videos/traffic.mp4"
    detect_vehicles(video_path)