import random
import pygame
from config import WIDTH, HEIGHT, PECA_HEIGHT, PECA_WIDTH
from assets import PECA1_IMG, PECA2_IMG, PECA3_IMG, PECA4_IMG, PECA5_IMG, PECA6_IMG, PECA7_IMG, PECA8_IMG


pecas_largura = [PECA1_IMG, PECA2_IMG, PECA3_IMG, PECA4_IMG, PECA5_IMG, PECA6_IMG, PECA7_IMG, PECA8_IMG]

for i in range(1,10):
    name_file = 'PECA{0}_IMG'.format(i)
    PECA_WIDTH = pecas_largura[i]
class Peca(pygame.sprite.Sprite):
    def __init__(self, groups, assets, name_file):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[name_file]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2
        self.rect.y = 42.5
        self.speedy = 5
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição da peça
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
             
        if self.rect.left < 0:
            self.rect.left = 0
        
        if i == 1:

            if self.rect.bottom > HEIGHT - 42.5:
                self.rect.bottom = HEIGHT - 42.5

            if 