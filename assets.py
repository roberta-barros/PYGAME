import pygame
import os
from config import width, height, W, H, RES, game_res, IMG_DIR, SND_DIR, FNT_DIR

LOGO='logo'
BACKGROUND_if = 'backgroundi'
SCORE_FONT = 'score_font'
BACKGROUND_SOUND = 'background_sound'
GAMEOVER_SOUND = 'gameover_sound'

def load_assets():
    assets = {}
    assets[LOGO] = pygame.image.load(os.path.join(IMG_DIR, 'logo.png')).convert()
    assets[BACKGROUND_if] = pygame.image.load(os.path.join(IMG_DIR, 'fundo_inicio_fim2.png')).convert()
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'Tetris.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[GAMEOVER_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'game-over.wav'))
    return assets