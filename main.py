import pygame
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)
import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util

import sys
import time
import math

import rocket
import terrain


# Variaveis Globais
GAME_TITLE = "não sei"
FPS = 60
spriteFPS = 10

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

# Carrega os sprites do foguete
foguete_sprites = [
    pygame.image.load("sprites/foguete/foguete_1.png"),
    pygame.image.load("sprites/foguete/foguete_2.png"),
    pygame.image.load("sprites/foguete/foguete_3.png")
]

# Corrigindo a posição do sprite
imagem = foguete_sprites[0]
largura, altura = imagem.get_size()

spritePosition = (0, 0)

# Índice atual do sprite do foguete
foguete_indice_sprite = 0


def velocityHUD():
    msg = 'Velocidade: ' + str(rocket.getVelocity()) + 'Km/h'
    return msg


def angleHUD():
    msg = 'Angulo: ' + str(rocket.getAngle() * -1) + '°'
    return msg


run = True
while run:

    # Taxa de atualização
    clock.tick(FPS)
    screen.fill(pygame.Color("black"))

    # Taxa de atualização dos sprites
    sprite_index = (int(time.time() * spriteFPS) + 1) % len(foguete_sprites)

    # HUD
    screen.blit(roboto.render(velocityHUD(), True,
                pygame.Color("white")), (20, 580))

    screen.blit(roboto.render(angleHUD(), True,
                              pygame.Color("white")), (20, 560))

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

                sprite_index = (int(time.time() * spriteFPS) +
                                1) % len(foguete_sprites)

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

        for i in range(foguete_indice_sprite):
            if i == 0:
                sprite_index = (int(time.time() * spriteFPS) +
                                1) % len(foguete_sprites)
            foguete_indice_sprite += 1

    # Teclas simultâneas
    elif keys[pygame.K_LEFT] and keys[pygame.K_SPACE]:
        rocket.angle -= 5
        rocket.change_direction(0)
        rocket.impulse()

        for i in range(foguete_indice_sprite):
            if i == 0:
                sprite_index = (int(time.time() * spriteFPS) +
                                1) % len(foguete_sprites)
            foguete_indice_sprite += 1

    elif keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]:
        rocket.angle += 5
        rocket.change_direction(1)
        rocket.impulse()

        for i in range(foguete_indice_sprite):
            if i == 0:
                sprite_index = (int(time.time() * spriteFPS) +
                                1) % len(foguete_sprites)
            foguete_indice_sprite += 1

    # Desenha o terreno
    for i in range(0, (len(mapPoints)-1)):
        # Virando o plano (y, x) -> (x, y)
        p1 = mapPoints[i]
        p1 = p1[1], p1[0]

        pygame.draw.circle(screen, pygame.Color(
            "white"), (p1[0]*50, p1[1]*25), 1)

    # Desenha o sprite do foguete na tela
    spritePosition = \
        (rocket.body.position[0] - largura/2), \
        (rocket.body.position[1] - altura + 15)

    # Rotacione a imagem do sprite com base no ângulo do objeto Pymunk
    angle = rocket.getAngle()

    foguete_sp = pygame.transform.rotate(
        foguete_sprites[foguete_indice_sprite], angle)

    foguete_sp = pygame.transform.rotozoom(foguete_sp, 0, 1)
    screen.blit(foguete_sp, spritePosition)

    # Debug PyMunk
    # space.debug_draw(draw_options)

    # Update
    dt = 1.0 / FPS
    space.step(dt)

    pygame.display.update()


pygame.quit()
