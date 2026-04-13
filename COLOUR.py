import cv2
import numpy as np
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800, 100))
pygame.display.set_caption("Image Processing Controls - Press keys to toggle")
font = pygame.font.SysFont("Arial", 24)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
red_tint = False
green_tint = False
blue_tint = False
edge_mode = None
running = True
print("Controls:")
print("R - Toggle Red tint")
print("G - Toggle Green tint")
print("B - Toggle Blue tint")
print("S - Toggle Sobel edge detection")
print("C - Toggle Canny edge detection")
print("E - Disable edge detection")
print("ESC - Quit")
while running:
    ret, frame = cap.read()
    if not ret:
        break
    processed = frame.copy()
    if red_tint:
        processed[:, :, 0] = 0
        processed[:, :, 1] = 0
    if green_tint:
        processed[:, :, 0] = 0
        processed[:, :, 2] = 0
    if blue_tint:
        processed[:, :, 1] = 0
        processed[:, :, 2] = 0
    gray = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
    if edge_mode == "sobel":
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sobel = cv2.magnitude(sobelx, sobely)
        sobel = np.uint8(np.clip(sobel, 0, 255))
        processed = cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR)
    elif edge_mode == "canny":
        edges = cv2.Canny(gray, 100, 200)
        processed = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cv2.imshow("Real-time Image Processing (Press ESC to quit)", processed)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[K_r]:
        red_tint = not red_tint
        pygame.time.wait(200)
    if keys[K_g]:
        green_tint = not green_tint
        pygame.time.wait(200)
    if keys[K_b]:
        blue_tint = not blue_tint
        pygame.time.wait(200)
    if keys[K_s]:
        edge_mode = "sobel" if edge_mode != "sobel" else None
        pygame.time.wait(200)
    if keys[K_c]:
        edge_mode = "canny" if edge_mode != "canny" else None
        pygame.time.wait(200)
    if keys[K_e]:
        edge_mode = None
        pygame.time.wait(200)
    if keys[K_ESCAPE]:
        running = False
    screen.fill((30, 30, 30))
    status = f"Red: {'ON' if red_tint else 'OFF'} | Green: {'ON' if green_tint else 'OFF'} | "
    status += f"Blue: {'ON' if blue_tint else 'OFF'} | Edge: {edge_mode if edge_mode else 'OFF'}"
    text = font.render(status, True, (255, 255, 255))
    screen.blit(text, (20, 20))
    pygame.display.flip()
    if cv2.waitKey(1) & 0xFF == 27:
        running = False
cap.release()
cv2.destroyAllWindows()
pygame.quit()