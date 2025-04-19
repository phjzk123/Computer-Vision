import cv2
import mediapipe as mp
from ultralytics import YOLO

# Khởi tạo YOLO và MediaPipe
yolo_model = YOLO("yolov8m.pt")  # Hoặc mô hình đã fine-tune
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Mở webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Dự đoán Bounding Box bằng YOLO
    results = yolo_model(frame)

    for result in results:
        for box in result.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            hand_roi = frame[y1:y2, x1:x2]  # Cắt ảnh bàn tay

            # Chuyển đổi ảnh ROI sang RGB để đưa vào MediaPipe
            hand_roi_rgb = cv2.cvtColor(hand_roi, cv2.COLOR_BGR2RGB)
            results_mediapipe = hands.process(hand_roi_rgb)

            if results_mediapipe.multi_hand_landmarks:
                for hand_landmarks in results_mediapipe.multi_hand_landmarks:
                    mp_draw.draw_landmarks(hand_roi, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Vẽ Bounding Box bàn tay
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("YOLO + MediaPipe Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()