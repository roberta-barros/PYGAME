# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 360
HEIGHT = 640
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('tetris')

# ----- Inicia assets
peca_width = 125
peca_height = 85
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/tetris1.png').convert()       #imagem do fundo
background_img_small = pygame.transform.scale(background, (WIDTH,HEIGHT))
PECA2_img = pygame.image.load('assets/img/ftetris2.png').convert_alpha()
PECA2_img = pygame.transform.scale(PECA2_img, (peca_width, peca_height))

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class pecas(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 37
        self.speedx = 0
        self.speedy = 3

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = 120
            self.rect.y = 37
            self.speedx = 0
            self.speedy = 3

        # Mantem dentro da tela
        if self.rect.right > WIDTH-37:
            self.rect.right = WIDTH-37
        if self.rect.left < 37:
            self.rect.left = 37


game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
# Criando o jogador
player = pecas(PECA2_img)
all_sprites.add(player)
# Criando os meteoros
for i in range(0):
    p = pecas(PECA2_img)
    all_sprites.add(p)

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 9   
            if event.key == pygame.K_RIGHT:
                player.speedx += 9
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 9
            if event.key == pygame.K_RIGHT:
                player.speedx -= 9

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background_img_small, (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

