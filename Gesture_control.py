# NOTE: I can't test this code as mediapipe is not working
import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

WIDTH, HEIGHT = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, WIDTH)
cap.set(4, HEIGHT)

shape_x, shape_y = WIDTH // 2, HEIGHT // 2
shape_size = 50
shape_color = (0, 255, 0)  
shape_type = "circle"      
prev_x, prev_y = None, None
movement_threshold = 15
thumbs_up_detected = False
open_hand_detected = False

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1) 
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    hand_detected = False
    current_x, current_y = None, None
    hand_z = 0
    if results.multi_hand_landmarks:
        hand_detected = True
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            current_x = int(wrist.x * WIDTH)
            current_y = int(wrist.y * HEIGHT)
            hand_z = wrist.z
            if prev_x is not None and prev_y is not None:
                dx = current_x - prev_x
                dy = current_y - prev_y
                
                if abs(dx) > movement_threshold or abs(dy) > movement_threshold:
                    if abs(dx) > abs(dy):
                        direction = "Right" if dx > 0 else "Left"
                    else:
                        direction = "Down" if dy > 0 else "Up"
                    shape_x += dx
                    shape_y += dx
                    shape_x = max(shape_size, min(WIDTH - shape_size, shape_x))
                    shape_y = max(shape_size, min(HEIGHT - shape_size, shape_y))
            
            prev_x, prev_y = current_x, current_y
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
            thumbs_up = (thumb_tip.y < wrist.y and 
                        abs(thumb_tip.x - wrist.x) < 0.1)
            open_hand = (index_tip.y < wrist.y and 
                        middle_tip.y < wrist.y and 
                        ring_tip.y < wrist.y and 
                        pinky_tip.y < wrist.y)
            if thumbs_up and not thumbs_up_detected:
                shape_color = (0, 0, 255)
                shape_type = "square"
                print("Thumbs up detected! Shape changed to Red Square")
                thumbs_up_detected = True
            elif not thumbs_up:
                thumbs_up_detected = False  
            if open_hand and not open_hand_detected:
                shape_color = (255, 255, 0) 
                shape_type = "circle"
                print("Open hand detected! Shape changed to Cyan Circle")
                open_hand_detected = True
            elif not open_hand:
                open_hand_detected = False
            size_factor = 1 + (-hand_z * 8) 
            dynamic_size = int(shape_size * size_factor)
            dynamic_size = max(20, min(150, dynamic_size))
            if index_tip.y < middle_tip.y - 0.05:
                shape_color = (0, 255, 255)  
            
    else:
        prev_x, prev_y = None, None
    if shape_type == "circle":
        half = dynamic_size // 2
        cv2.rectangle(frame, 
                     (shape_x - half, shape_y - half),
                     (shape_x + half, shape_y + half),
                     shape_color, -1)
    status = "Hand Detected" if hand_detected else "No Hand Detected"
    cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 
                (255, 255, 255), 2)
    
    cv2.putText(frame, f"Shape: {shape_type} | Size: {dynamic_size}", (10, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.imshow("Hand Tracking & Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()