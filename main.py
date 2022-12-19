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
terreno = terrain.Terreno(80, 60)
terreno.gerarMap()
mapPoints = terreno.getMapCoordinates()

run = True
while run:

    # Taxa de update
    clock.tick(FPS)

    # close event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        # Left Mouse Click
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            terreno.gerarMap()
            mapPoints = terreno.getMapCoordinates()

    window.fill(pygame.Color("black"))

    for i in range(0, (len(mapPoints)-1)):
        # Virando o plano (y, x) -> (x, y)
        p1 = mapPoints[i]
        p1 = p1[1], p1[0]
        p2 = mapPoints[i+1]
        p2 = p1[1], p1[0]

        # Liga dois pontos
        pygame.draw.line(window, pygame.Color(
            "white"), (p1[0]*10, p1[1]*10), (p2[1]*10, p2[0]*10), 2)

    pygame.display.update()

pygame.quit()
