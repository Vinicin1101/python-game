from mpl_toolkits.mplot3d import Axes3D
import math
import random
import matplotlib.pyplot as plt
import numpy as np
from noise import pnoise2


class Terrain():
    def __init__(self, width, height, seed=0):
        self.points = []
        self.width, self.height = width, height
        self.seed = seed

    def perlinNoise(self, octaves, base, persistance):
        # criação da matriz de zeros
        terrain = np.zeros((self.width, self.height))

        # preenchimento da matriz com os valores do Perlin Noise
        for i in range(self.width):
            for j in range(self.height):
                terrain[i][j] = pnoise2(
                    i / 10, j / 10, octaves=octaves, base=base, persistence=persistance)

        return terrain


# Teste

width, height = 100, 100  # Dimensões

t = Terrain(width=width, height=height, seed=1)  # Instância

terreno = t.perlinNoise(40, 9, 0.2)  # Geração


# Plotagem do Perlin Noise
plt.imshow(terreno, cmap='gray', origin='lower')
plt.show()


# Plotagem 3D

# criação dos arrays de coordenadas
x = np.arange(width)
y = np.arange(height)

# criação das matrizes de coordenadas
X, Y = np.meshgrid(x, y)

# transformação da matriz em um array unidimensional
z = terreno.flatten()
z = z.reshape((width, height))


# criação do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plotagem da superfície
ax.plot_surface(X, Y, z, cmap="Purples")

# exibição do gráfico
plt.show()
