import pygame
import os
from config import WIDTH, HEIGHT, PECA1_WIDTH, PECA1_HEIGHT, PECA2_WIDTH, PECA2_HEIGHT, PECA3_WIDTH, PECA3_HEIGHT, PECA4_WIDTH, PECA4_HEIGHT, PECA5_WIDTH,PECA5_HEIGHT,PECA6_WIDTH, PECA6_HEIGHT, PECA7_WIDTH, PECA7_HEIGHT, PECA8_WIDTH, PECA8_HEIGHT, PECA9_WIDTH, PECA9_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR


BACKGROUND1 = 'background1'
BACKGROUND2 = 'background2'
BACKGROUND3 = 'background3'
PECA1_IMG = 'tetris2'
PECA2_IMG = 'tetris2-removebg-preview'
PECA3_IMG = 'tetris3'
PECA4_IMG = 'tetris4'
PECA5_IMG = 'tetris5'
PECA6_IMG = 'tetris6'
PECA7_IMG = 'tetris7'
PECA8_IMG = 'tetris8'
PECA9_IMG = 'tetris9'
SCORE_FONT = 'score_font'
BACKGROUND_SOUND = 'background_sound'
GAMEOVER_SOUND = 'gameover_sound'

def load_assets():
    assets = {}
    assets[BACKGROUND1] = pygame.image.load(os.path.join(IMG_DIR, 'tetris1.png')).convert()
    assets[BACKGROUND2] = pygame.image.load(os.path.join(IMG_DIR, 'tetris_nivel2.png')).convert()
    assets[BACKGROUND3] = pygame.image.load(os.path.join(IMG_DIR, 'tetris_nivel3.png')).convert()
    assets[PECA1_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'tetris2.png')).convert_alpha()
    assets[PECA1_IMG] = pygame.transform.scale(assets['meteor_img'], (METEOR_WIDTH, METEOR_HEIGHT))
    assets[PECA2_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'playerShip1_orange.png')).convert_alpha()
    assets[PECA2_IMG] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
    assets[PECA3_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()
    assets[PECA3_IMG] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
    assets[PECA4_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()
    assets[PECA4_IMG] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
    assets[PECA5_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()
    assets[PECA5_IMG] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
    assets[PECA6_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()
    assets[PECA6_IMG] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
    assets[PECA7_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()
    assets[PECA7_IMG] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
    assets[PECA8_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()
    assets[PECA8_IMG] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
    assets[PECA9_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()
    assets[PECA9_IMG] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'Tetris.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[GAMEOVER_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    return assets