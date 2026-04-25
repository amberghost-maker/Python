import cv2
import requests
import numpy as np
from google.colab.patches import cv2_imshow

image_url = 'https://www.thisiscolossal.com/wp-content/uploads/2024/10/darya-9-960x1190.jpg'

try:
    response = requests.get(image_url, stream=True)
    response.raise_for_status() # Raise an exception for HTTP errors
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
except requests.exceptions.RequestException as e:
    print(f"Error downloading image: {e}")
    img = None
except Exception as e:
    print(f"Error processing image: {e}")
    img = None

if img is None:
    print("Error: Image not found or unable to load.")
    exit()
    

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray_img)
cv2.waitKey(0)
x_start, y_start = 100, 200
x_end, y_end = 300, 400
cropped_img = gray_img[y_start:y_end, x_start:x_end]
cv2_imshow(cropped_img)
cv2.waitKey(0)
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
cos = abs(rotation_matrix[0, 0])
sin = abs(rotation_matrix[0, 1])
nW = int((h * sin) + (w * cos))
nH = int((h * cos) + (w * sin))
rotation_matrix[0, 2] += (nW / 2) - center[0]
rotation_matrix[1, 2] += (nH / 2) - center[1]
rotated_img = cv2.warpAffine(img, rotation_matrix, (nW, nH))
cv2_imshow(rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()