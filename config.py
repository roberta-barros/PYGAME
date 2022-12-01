from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'sound')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Define tamanhos das peças e os dados gerais do jogo
W, H = 10, 20
PECA = 38
width = W * PECA
height = H * PECA
RES = 750, 760 
game_res = width, height
FPS = 60

# Define algumas variáveis com as cores básicas
cores = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (120, 37, 179)]

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2