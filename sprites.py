import random
from os import path
from config import IMG_DIR,FPS, GAME, QUIT, cores
from pygame import mixer 
from assets import *

# Definição dos blocos
class Block(pygame.sprite.Sprite):

# Matriz de peças e suas rotações
    pecas = [
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 2, 5, 6]],
    ]

# Sorteio da peça e da cor
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.pecas) - 1)
        self.color = random.randint(1, len(cores) - 1)
        self.rotation = 0

    def image(self):
        return self.pecas[self.type][self.rotation]

# Define a rotação da figura
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.pecas[self.type])

# Definições do jogo
class Tetris:
    W, H = 10, 20
    x = 0
    y = 0
    PECA = 38
    width = W * PECA
    height = H * PECA
    level = 2 #(velocidade)
    score = 0
    state = "start"
    grid = []
    figure = None
# Criação da tela
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.grid = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            newline = []
            for j in range(width):
                newline.append(0)
            self.grid.append(newline)

    def nova_peca(self): # Cria uma nova peça e posiciona em x = 3 e y = 0
        self.figure = Block(3, 0)

    def intersects(self): # Verifica se a peça atual encosta em algo fixo na tela
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.grid[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self): # Quebra a linha se a fileira horizontal estiver completa
        lines = 0
        for i in range(1, self.height):
            z = 0
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    z += 1
            if z == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.grid[i1][j] = self.grid[i1 - 1][j]
        self.score += lines**2 # Guarda a pontuação

    def down(self): # Aumenta a velocidade da peça quando aperta a tecla down
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self): # Congela a peça quando ela toca no chão ou intersecciona outra peça
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.grid[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.nova_peca()
        if self.intersects():
            self.state = "gameover"

    def side(self, dx): # Move a peça para a esquerda ou para a direita
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self): # Rotaciona a peça quando aperta espaço
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation