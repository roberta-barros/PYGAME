import random
import pygame
from config import WIDTH, HEIGHT, PECA1_WIDTH, PECA1_HEIGHT, PECA2_WIDTH, PECA2_HEIGHT, PECA3_WIDTH, PECA3_HEIGHT, PECA4_WIDTH, PECA4_HEIGHT, PECA5_WIDTH,PECA5_HEIGHT,PECA6_WIDTH, PECA6_HEIGHT, PECA7_WIDTH, PECA7_HEIGHT, PECA8_WIDTH, PECA8_HEIGHT, PECA9_WIDTH, PECA9_HEIGHT
from assets import PECA1_IMG, PECA2_IMG, PECA3_IMG, PECA4_IMG, PECA5_IMG, PECA6_IMG, PECA7_IMG, PECA8_IMG, PECA9_IMG


pecas_largura = [PECA1_WIDTH, PECA2_WIDTH, PECA3_WIDTH, PECA4_WIDTH, PECA5_WIDTH, PECA6_WIDTH, PECA7_WIDTH, PECA8_WIDTH, PECA]

for i in range(1,10):
    name_file = 'PECA{0}_IMG'.format(i)
    PECA_WIDTH = 
class Peca(pygame.sprite.Sprite):
    def __init__(self, groups, assets, name_file):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[name_file]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2
        self.rect.y = 43
        self.speedy = 5
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição da peça
        self.rect.y += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
             
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom = 