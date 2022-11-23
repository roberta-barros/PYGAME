import random
import pygame
from config import WIDTH, HEIGHT, PECA1_WIDTH, PECA1_HEIGHT, PECA2_WIDTH, PECA2_HEIGHT, PECA3_WIDTH, PECA3_HEIGHT, PECA4_WIDTH, PECA4_HEIGHT, PECA5_WIDTH,PECA5_HEIGHT,PECA6_WIDTH, PECA6_HEIGHT, PECA7_WIDTH, PECA7_HEIGHT, PECA8_WIDTH, PECA8_HEIGHT, PECA9_WIDTH, PECA9_HEIGHT
from assets import PECA1_IMG, PECA2_IMG, PECA3_IMG, PECA4_IMG, PECA5_IMG, PECA6_IMG, PECA7_IMG, PECA8_IMG, PECA9_IMG

for i in range(10):
    imagem_nome = 'PECA{0}_IMG'.format(i)

class Peca(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[PECA1_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição da peça
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


