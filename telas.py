import pygame
import random
from os import path
from game_screen import game_screen

from config import IMG_DIR, FPS, GAME, QUIT

pygame.init()

def inicio(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background_if = pygame.image.load(path.join(IMG_DIR, 'fundo_inicio_fim.png')).convert()
    background_rect = background_if.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background_if, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

def final(screen):

    pygame.display.set_caption('GAME OVER')
    font = pygame.font.SysFont(None, 48)  #  fonte e tamanho de texto
    text = font.render('GAME OVER', True, (0, 0, 255))

    # ----- Inicia estruturas de dados
    game = True

    # ===== Loop principal =====
    while game:
        # ----- Trata eventos
        for event in pygame.event.get():
            print(event) #o que são os eventos
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

        # ----- Gera saídas
        screen.fill((255, 255, 255))  # Preenche com a cor branca
        x = 135
        y = 10
        screen.blit(text, (x, y))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
