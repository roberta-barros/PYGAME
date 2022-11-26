# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
fps = 60
Clock = pygame.time.Clock()
 
W, H = 10, 20
PECA = 38
width = W * PECA
height = H * PECA
game_res = width, height
RES = 750, 600
screen = pygame.display.set_mode(RES)
game_screen = pygame.Surface(game_res)

grid = [pygame.Rect(x * PECA, y * PECA, PECA, PECA) for x in range(W) for y in range(H)]

pygame.display.set_caption('Tetris')

# ----- Inicia assets
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/universo.png').convert()
background_img_small = pygame.transform.scale(background, (width, height))

# Define as peças
figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]
    
cores = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (120, 37, 179)]

# ----- Inicia estruturas de dados
game = True
peca_x = width/2
peca_y = -PECA
peca_speedx = 1
peca_speedy = 1  # Velocidade y da peça (velocidades positivas em y significam que a peça vai se mover para baixo)

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(cores) - 1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.pecas[self.type])

# ===== Loop principal =====
while game:
    screen.fill((0, 0, 0)) # Preenche com a cor branca
    screen.blit(background_img_small, (width, 0))
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
    # Desenhar grades
    [pygame.draw.rect(screen, (40, 40, 40), i_rect, 1) for i_rect in grid]
  
    pygame.display.flip()
    Clock.tick(fps)

    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    peca_x += peca_speedx
    peca_y += peca_speedy
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados