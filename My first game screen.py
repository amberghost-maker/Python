import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game screen")
BG_COLOR = (58, 58, 58)
image = pygame.image.load("http://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8BWYiaBGncEEvWGAil2AS-BEf4yY4JIATBA&s")
image = pygame.transform.scale(image, (300, 300))
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BG_COLOR)
    screen.blit(image, image_rect)
    pygame.display.flip()
pygame.quit()
sys.exit()