# PYGAME
1. Título
Tetris
2. Integrantes
Camilla Junqueira, Fernanda Valesca, Roberta Barros
3. explicação do código
• gera tela principal
- estabelecimento de tamanhos 
   - telas (principal e secundária) 
   - grade
   - peças
   - nome
   - imagem 
   - cores
   - velocidades e posições

• estabelecimento de classes
- peças
   - formato
   - velocidade
   - cores
   - rotações
- jogo
   - pontos 
   - linhas
   - criação das peças
   - inicialização
   - movimentação de peças
   - parar a peça
   - destruição de linhas

• incialização do jogo
  • introdução
   - play
   - carrega imagens do inicio
   - looping para jogo para que se a pessoa perca e queira 
voltar a jogar
   - fechar se sair
  • o jogo
   - plotar peça
   - movimentar a peça
   - encontro de peças: parar
   - acabar o jogo quando não couber mais 
  • fim de jogo
   - imagens
   - acabar/retornar 

4. teclas para jogar/rodar 
necessidade de apertar o play/run inicialmente
apertar qualquer tecla para começar a jogar 
  - espaço para rodar
  - setas esquerda/direita para movimentar
  - baixo para acelerar
espaço para sair ao final do jogo
enter para recomeçar
5. links
link para o video do jogo funcionando
https://www.youtube.com/watch?v=BjbQFPUDJu85
Código extraído de (referência):
https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318
6. o que está contido:
- Tela de menu/início de jogo e tela de final de jogo
- Contagem de pontuação
- instruções
- fundo musical
- telas de instrução
7. executar
arquivo versão_3.py
8. rascunhos
versao 1
versao 2
assets
config
game_screen
init_screen
peca(1-8), tetris_nivel2, tetris_nivel3, universo, fundo1, fundo, fundo_inicio_fim/1