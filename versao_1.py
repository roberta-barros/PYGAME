# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
fps = 60
Clock = pygame.time.Clock()
 
W, H = 10, 20
PECA = 38
width = W * PECA
height = H * PECA
screen = pygame.display.set_mode((width, height))

grid = [pygame.Rect(x * PECA, y * PECA, PECA, PECA) for x in range(W) for y in range(H)]

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    screen.fill((0, 0, 0)) # Preenche com a cor branca
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
    # Desenhar grades
    [pygame.draw.rect(screen, (40, 40, 40), i_rect, 1) for i_rect in grid]
  
    pygame.display.flip()
    Clock.tick(fps)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados