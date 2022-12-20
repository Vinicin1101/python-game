import pymunk
import pygame
import math


class Rocket:

    def __init__(self, position, mass=100, propultion=-50, moment=None, angle=0):
        self.mass = mass
        self.propultion = propultion
        self.angle = 0
        self.moment = moment
        self.propultion_magnitude = 1

        # Calculate moment if not provided
        if self.moment is None:
            self.moment = pymunk.moment_for_circle(self.mass, 0, 10)

        # Create body and shape for the rocket
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = position
        vertices = [(-10, 10), (10, 10), (10, -25), (-10, -25), (0, -40)]
        self.shape = pymunk.Poly(self.body, vertices)
        self.shape.color = (pygame.Color("white"))

    def impulse(self):
        if self.propultion <= -50 and self.propultion > -299:
            self.propultion = self.propultion * 1.25

        # Rotacionando a matriz de força para o angulo do foguete
        self.body.angular_velocity = 0
        # Matriz de rotação
        angle = math.radians(self.angle)
        rotation_matrix = [[math.cos(angle), -math.sin(angle)],
                           [math.sin(angle), math.cos(angle)]]

        # Matriz da força
        thrust_force = pymunk.Vec2d(0, (self.propultion))

        # Rotacionando
        rotacionada = pymunk.Vec2d(rotation_matrix[0][0] * thrust_force[0] + rotation_matrix[0][1]
                                   * thrust_force[1], rotation_matrix[1][0] * thrust_force[0] + rotation_matrix[1][1] * thrust_force[1])

        # Aplicando a força no foguetinho
        local_point = (0, 10)  # Base dele

        self.body.apply_impulse_at_local_point(
            rotacionada, local_point)

    def resetPropultion(self):
        self.propultion = -50

    def change_direction(self, direction):
        self.angle = 0

        if direction == 0:
            self.angle -= 5

            # aplica a forca na parte superior esquerda do fogete
            impulse_force = pymunk.Vec2d(-100, 0)
            local_point = pymunk.Vec2d(-10, -10)

            self.body.apply_impulse_at_local_point(impulse_force, local_point)

        elif direction == 1:
            self.angle += 5

            # aplica a forca na parte supeerior direita do fogete
            impulse_force = pymunk.Vec2d(100, 0)
            local_point = pymunk.Vec2d(-10, -10)

            self.body.apply_impulse_at_local_point(impulse_force, local_point)

        self.angle = math.radians(self.angle)
