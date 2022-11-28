import pygame
import os
from config import WIDTH, HEIGHT, PECA_WIDTH, PECA_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR

LOGO='logo'
BACKGROUND_if = 'backgroundi'
BACKGROUND1 = 'background1'
BACKGROUND2 = 'background2'
BACKGROUND3 = 'background3'
PECA1_IMG = 'peca1'
PECA2_IMG = 'peca2'
PECA3_IMG = 'peca3'
PECA4_IMG = 'peca4'
PECA5_IMG = 'peca5'
PECA6_IMG = 'peca6'
PECA7_IMG = 'peca7'
PECA8_IMG = 'peca8'
SCORE_FONT = 'score_font'
BACKGROUND_SOUND = 'background_sound'
GAMEOVER_SOUND = 'gameover_sound'

def load_assets():
    assets = {}
    assets[LOGO] = pygame.image.load(os.path.join(IMG_DIR, 'logo.png')).convert()
    assets[BACKGROUND_if] = pygame.image.load(os.path.join(IMG_DIR, 'fundo_inicio_fim.png')).convert()
    assets[BACKGROUND1] = pygame.image.load(os.path.join(IMG_DIR, 'tetris1.png')).convert()
    assets[BACKGROUND2] = pygame.image.load(os.path.join(IMG_DIR, 'tetris_nivel2.png')).convert()
    assets[BACKGROUND3] = pygame.image.load(os.path.join(IMG_DIR, 'tetris_nivel3.png')).convert()
    assets[PECA1_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'peca1.png')).convert_alpha()
    assets[PECA1_IMG] = pygame.transform.scale(assets['peca1'], (PECA_WIDTH, PECA_HEIGHT))
    assets[PECA2_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'peca2.png')).convert_alpha()
    assets[PECA2_IMG] = pygame.transform.scale(assets['peca2'], (PECA_WIDTH, PECA_HEIGHT))
    assets[PECA3_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'peca3.png')).convert_alpha()
    assets[PECA3_IMG] = pygame.transform.scale(assets['peca3'], (PECA_WIDTH, PECA_HEIGHT))
    assets[PECA4_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'peca4.png')).convert_alpha()
    assets[PECA4_IMG] = pygame.transform.scale(assets['peca4'], (PECA_WIDTH, PECA_HEIGHT))
    assets[PECA5_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'peca5.png')).convert_alpha()
    assets[PECA5_IMG] = pygame.transform.scale(assets['peca5'], (PECA_WIDTH, PECA_HEIGHT))
    assets[PECA6_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'peca6.png')).convert_alpha()
    assets[PECA6_IMG] = pygame.transform.scale(assets['peca6'], (PECA_WIDTH, PECA_HEIGHT))
    assets[PECA7_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'peca7.png')).convert_alpha()
    assets[PECA7_IMG] = pygame.transform.scale(assets['peca7'], (PECA_WIDTH, PECA_HEIGHT))
    assets[PECA8_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'peca8.png')).convert_alpha()
    assets[PECA8_IMG] = pygame.transform.scale(assets['peca8'], (PECA_WIDTH, PECA_HEIGHT))
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'Tetris.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[GAMEOVER_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'game-over.wav'))
    return assets