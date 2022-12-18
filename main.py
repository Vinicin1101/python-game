import pygame
import math

# Variaveis Globais
GAME_TITLE = "não sei"
FPS = 60
# screen size
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600



# pygame window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption(GAME_TITLE)
pygame.display.set_icon(pygame.image.load('icon.png'))

run = True
while run:

    # close event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

pygame.quit()
