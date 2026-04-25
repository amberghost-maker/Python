import cv2
import mediapipe as mp
import numpy as np
import time
import os
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
filters = ["Normal", "Gray", "Sepia", "Negative", "Blur"]
current_filter = 0
last_action_time = 0
DEBOUNCE_DELAY = 1  
if not os.path.exists("photos"):
    os.makedirs("photos")
def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))
def apply_filter(frame, filter_name):
    if filter_name == "Gray":
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filter_name == "Sepia":
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        sepia = cv2.transform(frame, kernel)
        return np.clip(sepia, 0, 255).astype(np.uint8)
    elif filter_name == "Negative":
        return cv2.bitwise_not(frame)
    elif filter_name == "Blur":
        return cv2.GaussianBlur(frame, (15, 15), 0)
    return frame
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    h, w, _ = frame.shape
    action_text = ""
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm = []
            for id, lm_point in enumerate(handLms.landmark):
                cx, cy = int(lm_point.x * w), int(lm_point.y * h)
                lm.append((cx, cy))
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            thumb = lm[4]
            index = lm[8]
            middle = lm[12]
            ring = lm[16]
            pinky = lm[20]
            now = time.time()
            if now - last_action_time > DEBOUNCE_DELAY:
                if distance(thumb, index) < 40:
                    filename = f"photos/photo_{int(time.time())}.png"
                    cv2.imwrite(filename, frame)
                    action_text = "Photo Captured!"
                    last_action_time = now
                elif distance(thumb, middle) < 40:
                    current_filter = (current_filter + 1) % len(filters)
                    action_text = f"Filter: {filters[current_filter]}"
                    last_action_time = now
                elif distance(thumb, ring) < 40:
                    current_filter = (current_filter - 1) % len(filters)
                    action_text = f"Filter: {filters[current_filter]}"
                    last_action_time = now
                elif distance(thumb, pinky) < 40:
                    current_filter = 0
                    action_text = "Filter Reset"
                    last_action_time = now
    filtered = apply_filter(frame, filters[current_filter])
    if filters[current_filter] == "Gray":
        filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2BGR)
    cv2.putText(filtered, f"Filter: {filters[current_filter]}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    if action_text:
        cv2.putText(filtered, action_text, (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Gesture Camera", filtered)
    if cv2.waitKey(1) & 0xFF == 27: 
        break

cap.release()
cv2.destroyAllWindows()