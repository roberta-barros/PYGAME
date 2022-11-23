# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 360
HEIGHT = 320*2
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('tetris')

# ----- Inicia assets
PECA2_WIDTH = 125
PECA2_HEIGHT = 85
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/tetris1.png').convert_alpha()
bck_largura = background.get_rect().width*2
bck_altura = background.get_rect().height*2                   #imagem do fundo
background_img_small = pygame.transform.scale(background, (bck_largura,bck_altura))
PECA2_img = pygame.image.load('assets/img/ftetris2.png').convert_alpha()     #imagem do fundo
#peca2_largura = PECA2_img.get_rect().width*2
#peca2_altura = PECA2_img.get_rect().height*2
PECA2_img_small = pygame.image.load('assets/img/ftetris2.png').convert_alpha()
PECA2_img_small = pygame.transform.scale(PECA2_img, (PECA2_WIDTH, PECA2_HEIGHT))       #imagem do fundo

# ----- Inicia estruturas de dados
game = True
PECA2_X =38#random.randint(0, WIDTH-PECA2_WIDTH) #meteor_x = 200                                 #variável: posição x do meteoro
# y negativo significa que está acima do topo da janela. O meteoro começa fora da janela        
PECA2_y = 37.5 #meteor_y = -METEOR_HEIGHT                      #variável: posição y do meteoro (valores negativos significam que o meteoro está acima da janela. Vamos sortear valores de maneira que ele sempre comece o movimento de fora da janela, ou seja, o mais baixo possível é -METEOR_HEIGHT.)
PECA2_speedx = 0                                         #variável: velocidade x do meteoro ( se os valores da componente x da velocidade forem muito altos o meteoro vai se mover para um dos lados sem descer muito)
PECA2_speedy = 0                                   #variável: velocidade y do meteoro (velocidades positivas em y significam que o meteoro vai se mover para baixo)

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    PECA2_y += PECA2_speedy                                                         #atualiza a posição do meteoro
    # Se o meteoro passar do final da tela, volta para cima
    if PECA2_y > HEIGHT or PECA2_X + PECA2_X < 0 or PECA2_X > WIDTH:                #verifica se o meteoro saiu da tela. Nesse caso, faz ele voltar para a posição inicial.
        PECA2_X =  random.randint(0, WIDTH-PECA2_HEIGHT)                            #verifica se o meteoro saiu da tela. Nesse caso, faz ele voltar para a posição inicial.
        PECA2_Y =  random.randint(-100,-PECA2_HEIGHT)                               #verifica se o meteoro saiu da tela. Nesse caso, faz ele voltar para a posição inicial.

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background_img_small, (0,0))                                                 #desenha a imagem de fundo e depois a imagem do meteoro
    window.blit(PECA2_img_small, (PECA2_X, PECA2_y))                             #desenha a imagem de fundo e depois a imagem do meteoro                              

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

