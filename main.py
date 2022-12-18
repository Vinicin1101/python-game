import pygame
import math

# screen size
screen_width = 400
screen_heigth = 300

# pygame window
    window = pygame.display.set_mode((400,300))

run = True
while run:

    # close event
    for e in pygame.event.get():
        if e.type() == pygame.QUIT:
            run = False

pygame.quit()
