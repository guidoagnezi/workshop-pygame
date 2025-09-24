# Sessão 2 - Batalha
# Implementação de inimigos, ações e passagem de turnos
# Itens: 
# 1 - Inimigos
# 2 - Hud de Batalha
# 3 - Ações e Lógica de Turno
# Usaremos o código da sessão 2
# Autor: Guido Agnezi Deniz

import pygame
import botao as bt
import personagem as ps
import random

clock = pygame.time.Clock()
fps = 60

largura = 1024
altura = 768

janela = pygame.display.set_mode((largura, altura))

# 2 - Hud de Batalha
pygame.font.init()
fonte = pygame.font.Font("fonte/pixel.ttf")
# Imagem de fundo
img_fundo_background = pygame.image.load("imagem/fundo/selecao_fundo.webp").convert_alpha() # Atencao ao formato do arquivo
img_fundo_background = pygame.transform.scale(img_fundo_background, (largura, altura))

# Imagem do botao de personagem
img_quadro = pygame.image.load("imagem/fundo/quadro.png").convert_alpha()

# Imagem do cursor do botao de personagem
img_cursor = pygame.image.load("imagem/fundo/cursor.png").convert_alpha()
                                                
bt_personagem1 = bt.Button(img_quadro, 150, 135, 1, img_cursor)
bt_personagem2 = bt.Button(img_quadro, 360, 135, 2, img_cursor)
bt_personagem3 = bt.Button(img_quadro, 150, 385, 3, img_cursor)
bt_personagem4 = bt.Button(img_quadro, 360, 385, 4, img_cursor)
bt_personagem5 = bt.Button(img_quadro, 150, 635, 5, img_cursor)

# Lista de botões dos personagens
bt_personagem_lista = [bt_personagem1, bt_personagem2,
                       bt_personagem3, bt_personagem4,
                       bt_personagem5]

# Botão de confirmação
img_go = pygame.image.load("imagem/fundo/go.png").convert_alpha()
img_go_verde = pygame.image.load("imagem/fundo/go_verde.png").convert_alpha()
bt_go = bt.Button(img_go, 360, 635, 6, img_go_verde)

# Personagens
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

# Declaracao dos personagens jogaveis
# Mude as variaveis para deixar os personagens mais únicos!
# Ideias de implementação: ataques e magias únicas para cada personagem
# Implemente novos botões, personagens e inimigos
amigo = ps.Personagem(img_amigo, 0, 0, 100, 30, 10)
rogerio = ps.Personagem(img_rogerio, 0, 0, 100, 30, 10)
ico = ps.Personagem(img_ico, 0, 0, 100, 30, 10)
bicho = ps.Personagem(img_bicho, 0, 0, 100, 30, 10)
adiburai = ps.Personagem(img_adiburai, 0, 0, 100, 30, 10)

# Atribuicao de um personagem para cada botão
# Não é recomendado fazer assim, POREM, eu estou com preguiça de pensar um jeito melhor
bt_personagem1.personagem = amigo
bt_personagem2.personagem = rogerio
bt_personagem3.personagem = ico
bt_personagem4.personagem = bicho
bt_personagem5.personagem = adiburai

# Lista de personagens selecionados pelo jogador, inicializa-se vazia
personagens_selecionados = []

# 1 - Inimigos

img_inimigo1 = pygame.image.load("imagem/personagem/inimigo1/0.png")
img_inimigo2 = pygame.image.load("imagem/personagem/inimigo2/0.png")

inimigo1 = ps.Personagem(img_inimigo1, 0, 0, 100, 30, 10)
inimigo2 = ps.Personagem(img_inimigo2, 0, 0, 100, 30, 10)

# Imagem de apresentação do time selecionado
board_time = pygame.image.load("imagem/fundo/seu_time.png").convert_alpha()

# Aqui, define-se as posições dos personagens na tela de batalha

def definir_posicao():

    x_pos = 190
    y_pos = 240
    for ps in personagens_selecionados:
        ps.setPosicao(x_pos, y_pos)
        y_pos += 200 
    
    inimigo1.setPosicao(800, 340)
    inimigo2.setPosicao(800, 540)

# Tela de seleção

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
                # Navegação: seleção do botão
                if event.key == pygame.K_z:
                    pressionou = True

        # Atualizacao

        # Correcao do Indice
        if indice < 1:
            indice = 5
        elif indice > 6:
            indice = 1

        if pressionou:
            for bt in bt_personagem_lista:
                if bt.checkInputCursor(indice):
                    # Adiciona ou retira os personagens da lista de selecionados
                    if not bt.personagem in personagens_selecionados:
                        if len(personagens_selecionados) < 3:
                            personagens_selecionados.append(bt.personagem)
                    else:
                        personagens_selecionados.remove(bt.personagem)

            # Confirma o time e avança para a proxima tela
            # Somente se o time tiver 3 membros
            if bt_go.checkInputCursor(indice) and len(personagens_selecionados) == 3:
                definir_posicao()
                # Proxima tela
                batalha()
                
            
            pressionou = False

        # Render
        janela.blit(img_fundo_background, (0, 0))

        janela.blit(board_time, (500, 60))
        # Render botoes de personagem
        for bt in bt_personagem_lista:
            bt.update(janela)
            # Desenho do cursor
            bt.desenharCursor(janela, indice)
        
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

# 2 - Hud de Batalha

# Imagem do Hud
img_hud = pygame.image.load("imagem/fundo/battle_hud.png")

# Imagem dos botoes
img_ataque = pygame.image.load("imagem/fundo/ataque.png")
img_ataque_sel = pygame.image.load("imagem/fundo/ataque_sel.png") 
img_defesa = pygame.image.load("imagem/fundo/defesa.png")
img_defesa_sel = pygame.image.load("imagem/fundo/defesa_sel.png")

# Declaração dos botoes
bt_atq = bt.Button(img_ataque, 140, 82, 1, img_ataque_sel)
bt_def =  bt.Button(img_defesa, 310, 82, 2, img_defesa_sel)

img_cursor_inimigo = pygame.image.load("imagem/fundo/alvo.png")
# Ordem de atividade dos personagens
ordem = []

def atacar(atacante, defensor):
    dano = atacante.ataque - defensor.defesa

    if dano < 0:
        dano = 0

    defensor.vida -= dano

# Defender ainda não está implementado
# Implemente defender e outros tipos de ações durante o turno!
def defender(personagem):
    pass
def batalha():
    
    # 3 - Ações e Lógica de Turno
    ordem.extend(personagens_selecionados)
    ordem.append(inimigo1)
    ordem.append(inimigo2)

    indice_botoes = 1
    indice_inimigos = 1

    state_atacando = False
    state_vezJogador = True
    state_novoTurno = False
    pressionou = 0
    turno = 0

    personagem_da_vez = ordem[0]

    cooldown_count = 0
    cooldown_limit = 50

    while(True):

        clock.tick(fps)

        # Input

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # 3 - Ações e Lógica de Turno
            if event.type == pygame.KEYDOWN:
                # Navegação dos botoes do hud
                if not state_atacando and state_vezJogador:
                    if event.key == pygame.K_RIGHT:
                        indice_botoes += 1
                    if event.key == pygame.K_LEFT:
                        indice_botoes -= 1
                # Navegação do cursor sobre os inimigos quando estiver atacando
                if state_atacando and state_vezJogador:
                    if event.key == pygame.K_DOWN:
                        indice_inimigos += 1
                    if event.key == pygame.K_UP:
                        indice_inimigos -= 1
                if event.key == pygame.K_z:
                    pressionou = True

        # Atualizacao
        # Correcao Indice

        if indice_botoes > 2:
            indice_botoes = 1
        elif indice_botoes < 1:
            indice_botoes = 2
        
        if indice_inimigos > 2:
            indice_inimigos = 1
        if indice_inimigos < 1:
            indice_inimigos = 2

        # Gera um novo turno
        # Checa se é a vez do jogador (se o personagem da vez é um dos 3 primeiros da lista)
        # Checa se o personagem está vivo, se não, pula a vez dele
        if state_novoTurno:
            turno += 1
            personagem_da_vez = ordem[turno % 5]
            if (turno % 5) > 2:
                state_vezJogador = False
            else:
                state_vezJogador = True
            if personagem_da_vez.vida > 0:
                state_novoTurno = False

        # Ações do jogador
        # Só são possiveis se for a vez de um personagem jogável
        if not state_novoTurno and state_vezJogador:
            if pressionou:

                # Selecionando alvo
                if state_atacando:
                    if indice_inimigos == 1 and inimigo1.vida > 0:
                        atacar(personagem_da_vez, inimigo1)
                        state_atacando = False
                        state_novoTurno = True
                    elif indice_inimigos == 2 and inimigo2.vida > 0:
                        atacar(personagem_da_vez, inimigo2)
                        state_atacando = False
                        state_novoTurno = True

                # Iniciar seleção de alvo
                if bt_atq.checkInputCursor(indice_botoes) and not state_atacando and not state_novoTurno:
                    state_atacando = True

                pressionou = False
        # Vez do inimigo
        # Aqui eles selecionarão um personagem do jogador aleatorio para atacar somente, mesmo se ele já estiver morto
        # Experimente com o código e tente aprimorá-lo vocÊ mesmo
        # Faça que os inimigos posso tomar outras ações durante o turno deles para deixar o jogo mais desafiador
        if not state_novoTurno and not state_vezJogador:  
            if cooldown_count > cooldown_limit:
                atacar(personagem_da_vez, ordem[random.randint(0, 2)])
                state_novoTurno = True
                cooldown_count = 0
            else:
                cooldown_count += 1     

        # Render

        janela.fill("white")
        
        # Desenhando os personagens na tela
        for ps in personagens_selecionados:
            if ps.vida > 0:
                ps.update(janela)
        if inimigo1.vida > 0:
            inimigo1.update(janela)
        if inimigo2.vida > 0:
            inimigo2.update(janela)

        # Desenhando a HUD
        janela.blit(img_hud, (50, 50))
        bt_atq.update(janela)
        bt_def.update(janela)
        # Desenhando cursor da HUD
        bt_atq.desenharCursor(janela, indice_botoes)
        bt_def.desenharCursor(janela, indice_botoes)
        # Desenhando o personagem da vez
        rect = personagem_da_vez.image.get_rect(center=(600, 83))
        janela.blit(personagem_da_vez.image, rect)
        # Desenhando cursor inimigo
        if state_atacando:
            if indice_inimigos == 1:
                rect_alvo = img_cursor_inimigo.get_rect(center=(inimigo1.x_pos, inimigo1.y_pos - 110))
                vida_inim = fonte.render(f"{inimigo1.vida}/{inimigo1.vidamax}", True, "black")
                rect_texto = vida_inim.get_rect(center=(inimigo1.x_pos, inimigo1.y_pos - 80))
            if indice_inimigos == 2:
                rect_alvo = img_cursor_inimigo.get_rect(center=(inimigo2.x_pos, inimigo2.y_pos - 110))
                vida_inim = fonte.render(f"{inimigo2.vida}/{inimigo2.vidamax}", True, "black")
                rect_texto = vida_inim.get_rect(center=(inimigo2.x_pos, inimigo2.y_pos - 80))
            janela.blit(img_cursor_inimigo, rect_alvo)
            janela.blit(vida_inim, rect_texto)
        
        pygame.display.update()
        

selecao()