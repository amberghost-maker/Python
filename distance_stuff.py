#Meadiapipe isn't installed so the code won't run
import cv2
import mediapipe as mp
import numpy as np
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_min, vol_max = volume.GetVolumeRange()[:2]
def set_brightness(level):
    print(f"Brightness set to: {level}")
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
def get_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))
cap = cv2.VideoCapture(0)
prev_volume = None
prev_brightness = None
gesture_delay = 0.5 
last_gesture_time = 0
while True:
    success, frame = cap.read()
    if not success:
        break
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    volume_percent = None
    brightness_level = None
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            thumb_tip = (int(landmarks[4].x * w), int(landmarks[4].y * h))
            index_tip = (int(landmarks[8].x * w), int(landmarks[8].y * h))
            cv2.circle(frame, thumb_tip, 10, (255, 0, 0), -1)
            cv2.circle(frame, index_tip, 10, (0, 255, 0), -1)
            dist = get_distance(thumb_tip, index_tip)
            current_time = time.time()
            if current_time - last_gesture_time > gesture_delay:
                min_dist = 20
                max_dist = 200
                dist_clipped = np.clip(dist, min_dist, max_dist)
                volume_level = np.interp(dist_clipped, [min_dist, max_dist], [vol_min, vol_max])
                volume.SetMasterVolumeLevel(volume_level, None)
                last_gesture_time = current_time
                volume_percent = int(np.interp(dist_clipped, [min_dist, max_dist], [0, 100]))
                cv2.putText(frame, f'Volume: {volume_percent}%', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                brightness_level = np.interp(dist_clipped, [min_dist, max_dist], [0, 100])
                set_brightness(brightness_level)
                cv2.putText(frame, f'Brightness: {int(brightness_level)}%', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv2.imshow("Hand Gesture Control", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()