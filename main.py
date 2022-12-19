import pygame
import math
import terrain

# Variaveis Globais
GAME_TITLE = "não sei"
FPS = 60

# Tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600


# pygame window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption(GAME_TITLE)
pygame.display.set_icon(pygame.image.load('icon.png'))
clock = pygame.time.Clock()

# Terreno
terreno = terrain.Terreno(50, 40)
terreno.gerarMap()
mapPoints = terreno.getMapCoordinates()

run = True
while run:

    clock.tick(FPS)

    # close event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            terreno.gerarMap()
            mapPoints = terreno.getMapCoordinates()
            print("Left Click")

    window.fill(pygame.Color("black"))

    for p in mapPoints:
        pygame.draw.circle(window, pygame.Color(
            "white"), (p[0]*10, p[1]*10), 3)

    pygame.display.update()

pygame.quit()
