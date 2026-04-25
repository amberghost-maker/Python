# JUST A WARNING I DON'T KNOW IF THIS ACTUALLY WORKS BECAUSE MEADIAPIPE DOESN'T WORK
import cv2
import mediapipe as mp
import time
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
scroll_speed = 1  
scroll_delay = 1.0  
last_scroll_time = 0
def detect_gesture(hand_landmarks):
    return None
cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    if not success:
        break
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    gesture = None
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand_landmarks)
            current_time = time.time()
            if gesture in ['scroll_up', 'scroll_down']:
                if current_time - last_scroll_time > scroll_delay:
                    if gesture == 'scroll_up':
                        print("Scroll Up")
                    elif gesture == 'scroll_down':
                        print("Scroll Down")
                    last_scroll_time = current_time
    cv2.imshow("Hand Gesture Recognition", frame)
    key = cv2.waitKey(1)
    if key == 27:  
        break
cap.release()
cv2.destroyAllWindows()