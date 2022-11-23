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
meteor_img = pygame.image.load('assets/img/ftetris2.png').convert_alpha()
meteor_img = pygame.transform.scale(meteor_img, (peca_width, peca_height))

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class pecas(pygame.sprite.Sprite):   
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 360/3   #sortear a posição do meteoro
        self.rect.y = 37    #sortear a posição do meteoro
        self.speedx = 0
        self.speedy = 3

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = 360/3
            self.rect.y = 37
            self.speedx =0
            self.speedy =3   #24 - 46: definição da classe Meteor

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando dois meteoros
peca1 = pecas(meteor_img)     #54 e 55: criação de dois meteoros


# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    peca1.update()  # 69 e 70: atualização da posição dos meteoros.


    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background_img_small, (0, 0))
    # Desenhando meteoros
    window.blit(peca1.image, peca1.rect)   #76 e 77: desenhando os meteoros.


    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

