# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from sprites import Block, Tetris
from os import path
from config import IMG_DIR,FPS, GAME, QUIT, cores
from pygame import mixer 
from assets import *

def game_screen(screen):
    replay = True

    while replay:

        # Antes de começar o jogo, uma tela de início deve aparecer para introduzir ao jogador o jogo
        estado = 'inicio'
        if estado == 'inicio': 

            clock = pygame.time.Clock()

            # Carrega o fundo da tela inicial
            #fundo
            background_if = pygame.image.load(path.join(IMG_DIR, 'fundo2.png')).convert_alpha()
            background_rect = background_if.get_rect()
            tamanho_background = pygame.transform.scale(background_if, (width*2,height))  
            #logo
            LOGO = pygame.image.load(path.join(IMG_DIR, 'logo2-removebg-preview.png')).convert_alpha()
            tamanho_logo = pygame.transform.scale(LOGO, (550,400)) #345,300
            logo_rect = LOGO.get_rect()
            logo_x = 90
            logo_y = 150   
            #icone
            ICONE = pygame.image.load(path.join(IMG_DIR, 'icone-removebg-preview.png')).convert_alpha()
            tamanho_icone = pygame.transform.scale(ICONE, (60,60))
            icone_x = 10
            icone_y = 10 
            #texto
            font = pygame.font.SysFont('Britannic Bold', 40, True, False) 
            texto = font.render('Aperte qualquer tecla para começar!', True, (150, 50, 250)) 
            texto_x = 85
            texto_y = 580

            inicio = True
            while inicio:

                # Ajusta a velocidade do jogo.
                clock.tick(FPS)

                # Processa os eventos (mouse, teclado, botão, etc).
                for event in pygame.event.get():
                    # Verifica se foi fechado.
                    if event.type == pygame.QUIT:
                        state = QUIT
                        inicio = False
                        pygame.quit()

                    if event.type == pygame.KEYUP:
                        state = GAME
                        inicio = False

                # A cada loop, redesenha o fundo e os sprites
                screen.blit(tamanho_background, background_rect)
                screen.blit(tamanho_logo, (logo_x,logo_y))
                screen.blit(texto, (texto_x, texto_y)) 
                screen.blit(tamanho_icone, (icone_x,icone_y))

                # Depois de desenhar tudo, inverte o display.
                pygame.display.flip()


        # após inicío, haverá uma tela de instruções
        estado = 'manual'
        if estado == 'manual':
            clock = pygame.time.Clock()

            # Carrega o fundo da tela inicial
            #fundo
            background_if = pygame.image.load(path.join(IMG_DIR, 'fundo2.png')).convert_alpha()
            background_rect = background_if.get_rect()
            tamanho_background = pygame.transform.scale(background_if, (width*2,height))  
            #logo
            LOGO = pygame.image.load(path.join(IMG_DIR, 'logo2-removebg-preview.png')).convert_alpha()
            tamanho_logo = pygame.transform.scale(LOGO, (130,100)) #345,300
            logo_rect = LOGO.get_rect()
            logo_x = 600
            logo_y = 10   
            #icone
            ICONE = pygame.image.load(path.join(IMG_DIR, 'icone-removebg-preview.png')).convert_alpha()
            tamanho_icone = pygame.transform.scale(ICONE, (60,60))
            icone_x = 10
            icone_y = 10
            #texto
            font = pygame.font.SysFont('Britannic Bold', 50, True, False) 
            texto1 = font.render('instruções', True, (150, 50, 250)) 
            texto1_x = 85
            texto1_y = 100 
            #tecla
            TECLA = pygame.image.load(path.join(IMG_DIR, 'teclado.png')).convert_alpha()
            tamanho_tecla = pygame.transform.scale(TECLA, (600,300))
            tecla_x = 80
            tecla_y = 150
            #teclas
            TECLAS = pygame.image.load(path.join(IMG_DIR, 'Desenho sem título-PhotoRoom.png')).convert_alpha()
            tamanho_teclas = pygame.transform.scale(TECLAS, (100,50))
            teclas_x = 80
            teclas_y = 480
            #enter
            ENTER = pygame.image.load(path.join(IMG_DIR, 'enter.png')).convert_alpha()
            tamanho_enter = pygame.transform.scale(ENTER, (100,50))
            enter_x = 80
            enter_y = 540
            #espaço
            ESPACO= pygame.image.load(path.join(IMG_DIR, 'espaço.png')).convert_alpha()
            tamanho_espaco = pygame.transform.scale(ESPACO, (100,50))
            espaco_x = 80
            espaco_y = 600
            #texto2
            font = pygame.font.SysFont('Britannic Bold', 30, True, False) 
            texto2 = font.render('mover esquerda/direita + acelerar', True, (150, 50, 250)) 
            texto2_x = 110
            texto2_y = 500 
            #texto3
            font = pygame.font.SysFont('Britannic Bold', 30, True, False) 
            texto3 = font.render('reiniciar quando acabar', True, (150, 50, 250)) 
            texto3_x = 180
            texto3_y = 560  
            #texto4
            font = pygame.font.SysFont('Britannic Bold', 30, True, False) 
            texto4 = font.render('girar a peça', True, (150, 50, 250)) 
            texto4_x = 180
            texto4_y = 610   
            #texto
            font = pygame.font.SysFont('Britannic Bold', 40, True, False) 
            texto = font.render('Aperte qualquer tecla para começar!', True, (150, 50, 250)) 
            texto_x = 85
            texto_y = 660

            inicio = True
            while inicio:

                # Ajusta a velocidade do jogo.
                clock.tick(FPS)

                # Processa os eventos (mouse, teclado, botão, etc).
                for event in pygame.event.get():
                    # Verifica se foi fechado.
                    if event.type == pygame.QUIT:
                        state = QUIT
                        inicio = False
                        pygame.quit()

                    if event.type == pygame.KEYUP:
                        state = GAME
                        inicio = False

                # A cada loop, redesenha o fundo e os sprites
                screen.blit(tamanho_background, background_rect)
                screen.blit(tamanho_logo, (logo_x,logo_y))
                screen.blit(texto1, (texto1_x, texto1_y))
                screen.blit(texto, (texto_x, texto_y)) 
                screen.blit(texto2, (texto2_x, texto2_y))
                screen.blit(texto3, (texto3_x, texto3_y))
                screen.blit(texto4, (texto4_x, texto4_y)) 
                screen.blit(tamanho_icone, (icone_x,icone_y))
                screen.blit(tamanho_tecla, (tecla_x,tecla_y))
                screen.blit(tamanho_teclas, (teclas_x,teclas_y))
                screen.blit(tamanho_enter, (enter_x,enter_y))
                screen.blit(tamanho_espaco, (espaco_x,espaco_y))

                # Depois de desenhar tudo, inverte o display.
                pygame.display.flip()


        #após a instruçao, o jogo devera começar 
        # ===== Loop principal =====

        estado = 'continua'
        done = False
        game = Tetris(20, 10)
        counter = 0
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        go_down = False
    
    #música de fundo
        pygame.mixer.music.load(os.path.join(SND_DIR, 'Tetris.wav'))
        pygame.mixer.music.set_volume(0.7) 
        pygame.mixer.music.play() 
        pygame.mixer.music.play(loops=-1)

        while not done:
            screen.fill(BLACK)
            screen.blit(background_img_small, (width, 0))
            if game.figure is None:
                game.nova_peca()
            counter += 1
            if counter > 100000:
                counter = 0

            if counter % (FPS // game.level // 2) == 0 or go_down:
                if game.state == "start":
                    game.down()

        # saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True # DONE
                    pygame.quit()

        # comandos do jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        go_down = True
                    if event.key == pygame.K_LEFT:
                        game.side(-1)
                    if event.key == pygame.K_RIGHT:
                        game.side(1)
                    if event.key == pygame.K_SPACE:
                        game.rotate()
                    if event.key == pygame.K_ESCAPE:
                        game.__init__(20, 10)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    go_down = False

    #desenhos da peça no jogo
            for i in range(game.height):
                for j in range(game.width):
                    pygame.draw.rect(screen, WHITE, [game.x + game.PECA * j, game.y + game.PECA * i, game.PECA, game.PECA], 1)
                    if game.grid[i][j] > 0:
                        pygame.draw.rect(screen, cores[game.grid[i][j]],
                                        [game.x + game.PECA * j + 1, game.y + game.PECA * i + 1, game.PECA - 2, game.PECA - 1])

            if game.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i*4 + j
                        if p in game.figure.image():
                            pygame.draw.rect(screen, cores[game.figure.color],
                                            [game.x + game.PECA * (j + game.figure.x) + 1,
                                            game.y + game.PECA * (i + game.figure.y) + 1,
                                            game.PECA - 2, game.PECA - 2])
    # score
            font = pygame.font.SysFont('Britannia Bold', 40, True, False)
            font1 = pygame.font.SysFont('Britannia Bold', 65, True, False)
            text = font.render("Score: " + str(game.score), True, BLACK)
    #game over
            screen.blit(text, [400, 0])
            if game.state == "gameover":
                done = True # DONE
            
            pygame.display.flip()
            Clock.tick(FPS)

        #Quando o jogador perder, uma tela de game over deve aparecer
        if done == True:
            clock = pygame.time.Clock()

            # Carrega o fundo da tela inicial
            #fundo
            background_if = pygame.image.load(path.join(IMG_DIR, 'fundo_inicio_fim2.png')).convert_alpha()
            background_rect = background_if.get_rect()
            tamanho_background = pygame.transform.scale(background_if, (width*2,height))  
            #logo
            LOGO = pygame.image.load(path.join(IMG_DIR, 'logo2-removebg-preview.png')).convert_alpha()
            tamanho_logo = pygame.transform.scale(LOGO, (550,400)) #345,300
            logo_rect = LOGO.get_rect()
            logo_x = 90
            logo_y = 50   
            #icone
            ICONE = pygame.image.load(path.join(IMG_DIR, 'icone-removebg-preview.png')).convert_alpha()
            tamanho_icone = pygame.transform.scale(ICONE, (60,60))
            icone_x = 10
            icone_y = 10 
            #texto
            font1 = pygame.font.SysFont('Britannic Bold', 50, True, False) 
            texto1 = font1.render('FIM DE JOGO!', True, (0, 0, 0)) 
            texto1_x = 250
            texto1_y = 540

            font2 = pygame.font.SysFont('Britannic Bold', 40, True, False)
            texto2 = font2.render('Aperte ENTER para jogar novamente', True, (0, 0, 0)) 
            texto2_x = 100
            texto2_y = 620

            texto3 = font2.render('Aperte ESPAÇO para sair', True, (0, 0, 0)) 
            texto3_x = 170
            texto3_y = 670

            text = font.render("Score final: " + str(game.score), True, WHITE)

            # ----- Inicia estruturas de dados
            perdeu = True

            # ===== Loop principal =====
            while perdeu:
                # Processa os eventos (mouse, teclado, botão, etc).
                for event in pygame.event.get():
                    # Verifica se foi fechado.
                    if event.type == pygame.QUIT:
                        
                        state = QUIT
                        perdeu = False
                        pygame.quit()
                    
                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_SPACE:
                            done = True
                            estado = 'fim'
                            perdeu = False
                            replay = False
                            pygame.quit()

                        if event.key == pygame.K_RETURN:
                            done = False
                            estado = 'inicio'
                            perdeu = False
                            replay = True

                screen.blit(tamanho_background, background_rect)
                screen.blit(tamanho_logo, (logo_x,logo_y))
                screen.blit(texto1, (texto1_x, texto1_y)) 
                screen.blit(texto2, (texto2_x, texto2_y))
                screen.blit(texto3, (texto3_x, texto3_y))
                screen.blit(tamanho_icone, (icone_x,icone_y))
                screen.blit(text, [270, 470])
                # ----- Atualiza estado do jogo
                pygame.display.update()  # Mostra o novo frame para o jogador


    # ===== Finalização =====
    pygame.quit()   # Função do PyGame que finaliza os recursos utilizados