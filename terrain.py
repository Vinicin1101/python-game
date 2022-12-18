import numpy
import random

# Dimensões do plano
WIDTH = 60
HEIGTH = 20

drunk = {
    'map': WIDTH,  # comprimento to terreno
    'padding': 5,  # Margem de segurança (em relação a borda do plano)
    'x': 0,
    'y': random.randint(0, HEIGTH),  # inicio da altitudo
}

# Função de criação de linhas (por algum mistério o comentario ta afastado da função, deve ser coisa do Prettier)


def getLevelRow():
    return [' '] * WIDTH


# Definição da matriz
level = [getLevelRow() for _ in range(HEIGTH)]

# Estrutura de geração procedural
while drunk['map'] >= 0 and drunk['x'] < WIDTH:
    x = drunk['x']
    y = drunk['y']

    if level[y][x] == ' ':
        level[y][x] = '.'
        drunk['map'] -= 1
        drunk['x'] += 1

    roll = random.randint(1, 4)  # carga aleatória

    # Cria um relevo ou depressão
    if roll == 1 and y > drunk['padding']:
        drunk['y'] -= 1
    if roll == 2 and y < HEIGTH - 1 - drunk['padding']:
        drunk['y'] += 1

    # Cria uma "moeda"
    if roll == 4 and y > drunk['padding']:
        drunk['y'] -= 1
        coinY = y-(random.randint(0, int(y*0.7)))  # altura da moeda

        # Verifica se a altura é muito proxima do terreno
        if coinY == y or (coinY + 1) == y or (coinY - 1) == y:
            level[coinY][x] = '.'
        else:
            level[coinY][x] = '*'

for row in level:
    print(''.join(row))
