# Sessão 1 - Menus e Funções de jogo
# Como desenvolver muitiplas telas de jogo
# Menu de selecao
# Classes e arquivos
# Itens: 
# 1 - Telas de jogo
# 2 - Imagem de fundo (origem de render, transform)
# 4 - Classe Botao
# 5 - Personagens
# 6 - Batalha (somente a transicao de tela, a batalha em si será elaborada na proxima sessão)
# Usaremos o cabeçalho da sessão 0
# Autor: Guido Agnezi Deniz

import pygame
import botao as bt
import personagem as ps

clock = pygame.time.Clock()
fps = 60

largura = 1024
altura = 768

janela = pygame.display.set_mode((largura, altura))

# 2 - Imagem de fundo
img_fundo_background = pygame.image.load("imagem/fundo/selecao_fundo.webp").convert_alpha() # Atencao ao formato do arquivo
img_fundo_background = pygame.transform.scale(img_fundo_background, (largura, altura))

# 3 - Classe botão
img_quadro = pygame.image.load("imagem/fundo/quadro.png").convert_alpha()

# 4 - Pressionar Botao (img_cursor)
img_cursor = pygame.image.load("imagem/fundo/cursor.png").convert_alpha()
                                                
# Volte nessa sessão para adicionar a dectecção de input no botão (4 - Pressionar Botao)
                                                # 4 - Pressionar Botao
bt_personagem1 = bt.Button(img_quadro, 150, 135, 1, img_cursor)
bt_personagem2 = bt.Button(img_quadro, 360, 135, 2, img_cursor)
bt_personagem3 = bt.Button(img_quadro, 150, 385, 3, img_cursor)
bt_personagem4 = bt.Button(img_quadro, 360, 385, 4, img_cursor)
bt_personagem5 = bt.Button(img_quadro, 150, 635, 5, img_cursor)

# Lista de botões dos personagens
bt_personagem_lista = [bt_personagem1, bt_personagem2,
                       bt_personagem3, bt_personagem4,
                       bt_personagem5]

# Botão de confirmação (Usado em 6 - Organização da batalha)
img_go = pygame.image.load("imagem/fundo/go.png").convert_alpha()
img_go_verde = pygame.image.load("imagem/fundo/go_verde.png").convert_alpha()
bt_go = bt.Button(img_go, 360, 635, 6, img_go_verde)

# 5 - Personagens
# As nuances dessa classe serão usadas na próxima sessão
# Por enquanto, usaremos para seleção de personagem

# Aqui, declaramos a imagem e o retangulo da imagem para servir de icone aos botoes.
# A declaração do retangulo é opcional.
# Aqui foi utilizado para centralizar corretamente a imagem do personagem e do botao.
# Quando queremos que a origem do render seja no centro da imagem, 
# declaramos um rect a partir das dimensões da imagem
# e indicamos seu centro (center = (x, y)).
# Quando queremos que a origem do render seja no canto superior esquerdo, não é necessário rect,
# uma tupla já basta.
# Ex.: janela.blit(img, rect) -> origem central
#      janela.blit(img, (x, y)) -> origem no canto superior esquerdo
# Experimente e utilize o que o seu código necessitar.

img_amigo = pygame.image.load("imagem/personagem/amigo/0.png").convert_alpha() # Imagem
img_amigo_rect = img_amigo.get_rect(center=(150, 135)) # Retangulo
img_rogerio = pygame.image.load("imagem/personagem/rogerio/0.png").convert_alpha()
img_rogerio_rect = img_rogerio.get_rect(center=(360, 135))
img_ico = pygame.image.load("imagem/personagem/ico/0.png").convert_alpha()
img_ico_rect = img_ico.get_rect(center=(150, 385))
img_bicho = pygame.image.load("imagem/personagem/bicho/0.png").convert_alpha()
img_bicho_rect = img_bicho.get_rect(center=(360, 385))
img_adiburai = pygame.image.load("imagem/personagem/adiburai/0.png").convert_alpha()
img_adiburai_rect = img_adiburai.get_rect(center=(150, 635))

# Lista de icones
icones_lista = [img_amigo, img_rogerio,
                img_ico, img_bicho,
                img_adiburai]

# Declaracao dos personagens de facto
amigo = ps.Personagem(img_amigo, 0, 0, 100, 30, 30)
rogerio = ps.Personagem(img_rogerio, 0, 0, 100, 30, 30)
ico = ps.Personagem(img_ico, 0, 0, 100, 30, 30)
bicho = ps.Personagem(img_bicho, 0, 0, 100, 30, 30)
adiburai = ps.Personagem(img_adiburai, 0, 0, 100, 30, 30)

# Atribuicao de um personagem para cada botão
# Não é recomendado fazer assim, POREM, eu estou com preguiça de pensar um jeito melhor
bt_personagem1.personagem = amigo
bt_personagem2.personagem = rogerio
bt_personagem3.personagem = ico
bt_personagem4.personagem = bicho
bt_personagem5.personagem = adiburai

# Lista de personagens selecionados pelo jogador, inicializa-se vazia
personagens_selecionados = []

# Imagem de apresentação do time selecionado
board_time = pygame.image.load("imagem/fundo/seu_time.png").convert_alpha()

# Aqui, define-se as posições dos personagens na tela de batalha

def definir_posicao():
    x_pos = 190
    y_pos = 240
    for ps in personagens_selecionados:
        ps.setPosicao(x_pos, y_pos)
        y_pos += 200 

# 1 - Nova função de jogo: tela de seleção

def selecao():

    pressionou = False
    indice = 1

    while(True):

        clock.tick(fps)

        # Input

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # Navegação: mudança de posição do cursor
                if event.key == pygame.K_RIGHT:
                    indice += 1
                if event.key == pygame.K_LEFT:
                    indice -= 1
                if event.key == pygame.K_DOWN:
                    indice += 2
                if event.key == pygame.K_UP:
                    indice -= 2
                # Navegação: seleção do botão (5 - Pressionar Botao)
                if event.key == pygame.K_z:
                    pressionou = True

        # Atualizacao

        # Correcao do Indice
        if indice < 1:
            indice = 5
        elif indice > 6:
            indice = 1

        # 4 - Pressionar Botao
        if pressionou:
            for bt in bt_personagem_lista:
                if bt.checkInputCursor(indice):
                    # Adiciona ou retira os personagens da lista de selecionados (5 - Personagens)
                    if not bt.personagem in personagens_selecionados:
                        if len(personagens_selecionados) < 3:
                            personagens_selecionados.append(bt.personagem)
                    else:
                        personagens_selecionados.remove(bt.personagem)

            # Confirma o time e avança para a proxima tela
            # Somente se o time tiver 3 membros
            if bt_go.checkInputCursor(indice) and len(personagens_selecionados) == 3:
                definir_posicao()
                # Proxima tela (6 - Batalha)
                batalha()
                
            
            pressionou = False

        # Render
        janela.blit(img_fundo_background, (0, 0))

        janela.blit(board_time, (500, 60))
        # 3 - Classe botão (render na tela)
        for bt in bt_personagem_lista:
            bt.update(janela)
            # Desenho do cursor (5 - Pressionar Botao)
            bt.desenharCursor(janela, indice)
        
        # 5 - Personagem (icone nos botoes)
        # Render dos icones nos botoes
        janela.blit(img_adiburai, img_adiburai_rect)
        janela.blit(img_rogerio, img_rogerio_rect)
        janela.blit(img_bicho, img_bicho_rect)
        janela.blit(img_ico, img_ico_rect)
        janela.blit(img_amigo, img_amigo_rect)

        pos_x_time = 710
        pos_y_time = 250

        # Render dos personagens selecionados pelo jogador
        for personagem in personagens_selecionados:
            rect = personagem.image.get_rect(center=(pos_x_time,pos_y_time))
            janela.blit(personagem.image, rect)
            pos_y_time += 130

        # Render do botao GO
        bt_go.update(janela)
        bt_go.desenharCursor(janela, indice)

        pygame.display.update()

# 6 - Organizacao da batalha
# Essa função será desenvolvida completamente na proxima sessão

def batalha():
    
    while(True):

        clock.tick(fps)

        # Input

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Atualizacao
        # Não há atualizações de jogo por enquanto
        # Render

        janela.fill("white")
        
        # Desenhando os personagens na tela
        for ps in personagens_selecionados:
            ps.update(janela)
        
        pygame.display.update()
        

selecao()