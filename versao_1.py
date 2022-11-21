# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('tetris!')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
image1 = pygame.image.load('tetris/tetris1.png').convert_alpha()  #colocar imagem
                                                                   # .convert() acelerar
                                                                   # .convert_alpha() quando a imagem possui transparência.
image1 = pygame.transform.scale(image1, (180,320)) # diminuir o tamanho da imagem

image2 = pygame.image.load('tetris/tetris2.png').convert_alpha()  #colocar imagem
                                                                   # .convert() acelerar
                                                                   # .convert_alpha() quando a imagem possui transparência.
image2 = pygame.transform.scale(image2, (180,320)) # diminuir o tamanho da imagem

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image1, (0, 0))
    window.blit(image2, (10, 10))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

