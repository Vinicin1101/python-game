import numpy
import random
import terrain


class Terreno:
    def __init__(self, width, heigth, padding=1):
        self.WIDTH = width
        self.HEIGTH = heigth

        self.drunk = {
            'len': self.WIDTH,  # comprimento to terreno
            # Margem de segurança (em relação a borda superior e inferior do plano)
            'paddingTOP': 100,
            'paddingBOT': 10,
            'x': 0,
            'y': random.randint(0, self.HEIGTH)  # inicio da altitudo
        }

        self.map = [[]]  # terreno vazio

    def __getMapRow(self):
        return (['0'] * self.WIDTH)

    def __resetDrunk(self):
        self.drunk = {
            'len': self.WIDTH,  # comprimento to terreno
            # Margem de segurança (em relação a borda superior e inferior do plano)
            'paddingTOP': 300,
            'paddingBOT': 10,
            'x': 0,
            'y': random.randint(0, self.HEIGTH)  # inicio da altitudo
        }

    def gerarMap(self):

        self.__resetDrunk()

        # Definição da matriz
        self.map = [self.__getMapRow() for _ in range(self.HEIGTH)]

        # Estrutura de geração procedural
        while self.drunk['len'] >= 0 and self.drunk['x'] < self.WIDTH and self.drunk['y'] < self.HEIGTH:
            x = self.drunk['x']
            y = self.drunk['y']

            if self.map[y][x] == '0':
                self.map[y][x] = '1'
                self.drunk['len'] -= 1
                # afasta os pontos no eixo X
                self.drunk['x'] += 1

            roll = random.randint(1, 2)  # carga aleatória

            # Cria um relevo ou depressão
            if roll == 1 and y > self.drunk['paddingTOP']:
                # esse padding mantem a proporção
                self.drunk['y'] -= 1
            if roll == 2 and y < self.HEIGTH - 1 - self.drunk['paddingBOT']:
                self.drunk['y'] += 1

            # Cria uma "moeda"
            if roll == 3 and y > self.drunk['paddingTOP']:
                self.drunk['y'] -= 1
                coinY = y-(random.randint(0, int(y*0.7)))  # altura da moeda

                # Verifica se a altura é muito proxima do terreno
                if coinY == y or (coinY + 1) == y or (coinY - 1) == y:
                    self.map[coinY][x] = '1'
                else:
                    self.map[coinY][x] = '2'

        return (self.map)

    def getMap(self):
        copyMap = [x[:] for x in self.map]

        return copyMap

    def viewMap(self):
        view = self.getMap()
        for i, row in enumerate(view):
            for j, cell in enumerate(row):
                if cell == '0':
                    view[i][j] = ' '
                elif cell == '1':
                    view[i][j] = '.'
                elif cell == '2':
                    view[i][j] = '*'

        for row in view:
            print(' '.join(row))

    def getMapCoordinates(self):
        copy = self.getMap()
        coor = []

        for i, row in enumerate(copy):
            for j, cell in enumerate(row):
                if cell == '1':
                    coor.append((i, j))

        return coor

    def getCoinCoordinates(self):
        copy = self.getMap()
        coor = []

        for i, row in enumerate(copy):
            for j, cell in enumerate(row):
                if cell == '2':
                    coor.append((i, j))

        return coor

    def getDem(self):
        dem = {
            "x": [],
            "y": [],
            "z": [],
        }

        coor = self.getMapCoordinates()
        for p in coor:
            print(p)
            dem["x"].append(p[1])
            dem["y"].append(p[0])

        map = self.getMap()
        for row in map:
            subArray = []
            for i in row:
                subArray.append(i)

            dem["z"].append(subArray)

        return dem
