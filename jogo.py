# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import *
from game_screen import game_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')

game_screen(screen)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados