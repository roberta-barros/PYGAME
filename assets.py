import pygame
import os
from config import width, height, W, H, RES, game_res, IMG_DIR, SND_DIR, FNT_DIR

LOGO='logo'
BACKGROUND_if = 'backgroundi'
SCORE_FONT = 'score_font'
BACKGROUND_SOUND = 'background_sound'
TETRIS_SOUND = 'tetris sound'
TECLAS = 'teclas'
ICONE = 'icone'
TECLADO = 'teclado'
ESPAÇO = 'espaço'
ENTER = 'enter'

def load_assets():
    assets = {}
    assets[LOGO] = pygame.image.load(os.path.join(IMG_DIR, 'logo2-removebg-preview.png')).convert()
    assets[BACKGROUND_if] = pygame.image.load(os.path.join(IMG_DIR, 'fundo_inicio_fim2.png')).convert()
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    assets[TECLAS] = pygame.image.load(os.path.join(IMG_DIR, 'Desenho sem título-PhotoRoom.png')).convert_alpha()
    assets[ICONE] = pygame.image.load(os.path.join(IMG_DIR, 'icone.png')).convert_alpha()
    assets[TECLAS] = pygame.image.load(os.path.join(IMG_DIR, 'Desenho sem título-PhotoRoom.png')).convert_alpha()
    assets[TECLADO] = pygame.image.load(os.path.join(IMG_DIR, 'teclado.png')).convert_alpha()
    assets[ESPAÇO] = pygame.image.load(os.path.join(IMG_DIR, 'espaço.png')).convert_alpha()
    assets[ENTER] = pygame.image.load(os.path.join(IMG_DIR, 'enter.png')).convert_alpha()

    

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'Tetris.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[TETRIS_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'tetris.wav'))
    return assets