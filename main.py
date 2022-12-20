import pygame
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)
import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util

import sys
import math

import rocket
import terrain


# Variaveis Globais
GAME_TITLE = "não sei"
FPS = 60

# Tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600


# tela do pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption(GAME_TITLE)
pygame.display.set_icon(pygame.image.load('icon.png'))
clock = pygame.time.Clock()

pygame.font.init()

roboto = pygame.font.Font("font\Roboto-Light.ttf", 12)

# Terreno (sem fisica)
terreno = terrain.Terreno(int(SCREEN_WIDTH/1), 20)
terreno.gerarMap()
mapPoints = terreno.getMapCoordinates()

# física com o PyMunk
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = (0, 100)

# Chão (físico, porém reto)
# ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
# ground_shape = pymunk.Segment(
#     ground_body, (0, (SCREEN_HEIGTH/2)), (SCREEN_WIDTH, (SCREEN_HEIGTH/2)), 1.0)
# ground_shape.color = (pygame.Color("white"))
# space.add(ground_body, ground_shape)

# Desenha os pontos do terreno
for i in range(0, (len(mapPoints)-1)):
    # Virando o plano (y, x) -> (x, y)
    p1 = mapPoints[i]
    p1 = p1[1], p1[0]
    p2 = mapPoints[i+1]
    p2 = p1[1], p1[0]

    ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    ground_shape = pymunk.Segment(
        ground_body, ((p1[0]*50, p1[1]*25)), (p2[1]*50, p2[0]*25), 1.0)
    ground_shape.color = (pygame.Color("white"))
    space.add(ground_body, ground_shape)

# Foguetinho
rocket = rocket.Rocket((400, 100))
space.add(rocket.body, rocket.shape)

# Carrega o sprite do foguete
foguete_sprite = pygame.image.load("sprites/foguete/foguete.png")


def velocityHUD():
    msg = 'Velocidade: ' + str(rocket.getVelocity()) + 'Km/h'
    return msg


run = True
while run:

    # Taxa de atualização
    clock.tick(FPS)
    screen.fill(pygame.Color("black"))

    # HUD
    screen.blit(roboto.render(velocityHUD(), True,
                pygame.Color("white")), (20, 580))

    # close event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            sys.audit('quit')

        # Left Mouse Click
        # elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:

        # Reseta o impulso quando solta o espaço
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_SPACE:
                rocket.resetPropultion()

    keys = pygame.key.get_pressed()  # Ouve a tecla pressionada

    # Movimentação
    if keys[pygame.K_LEFT]:
        rocket.angle -= 5
        rocket.change_direction(0)
    elif keys[pygame.K_RIGHT]:
        rocket.angle += 5
        rocket.change_direction(1)

    # Faz o foguetinho subir
    elif keys[pygame.K_SPACE]:
        rocket.impulse()

    # Teclas simultâneas
    elif keys[pygame.K_LEFT] and keys[pygame.K_SPACE]:
        rocket.angle -= 5
        rocket.change_direction(0)
        rocket.impulse()
    elif keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]:
        rocket.angle += 5
        rocket.change_direction(1)
        rocket.impulse()

    # Desenha o terreno
    for i in range(0, (len(mapPoints)-1)):
        # Virando o plano (y, x) -> (x, y)
        p1 = mapPoints[i]
        p1 = p1[1], p1[0]

        pygame.draw.circle(screen, pygame.Color(
            "white"), (p1[0]*50, p1[1]*25), 1)

    # Desenha o sprite do foguete na tela
    screen.blit(foguete_sprite, rocket.body.position)

    # Update
    dt = 1.0 / FPS
    space.step(dt)

    pygame.display.update()


pygame.quit()
