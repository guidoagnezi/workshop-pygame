# Sessão 0 -Estrutura básica de Pygame, Loop de Jogo
# Organização de código: input, atualização, renderização
# Itens
# 1 - Cabeçalho
# 2 - Funcao Jogo
# 3 - Desenho de Imagem (blit, update, tuplas)
# 4 - Input (eventos)
# Autor: Guido Agnezi Deniz

import pygame

# 1 - Cabeçalho
clock = pygame.time.Clock()
fps = 60

largura = 1024
altura = 768

janela = pygame.display.set_mode((largura, altura))

# 3 - Desenho de Imagem
img_personagem = pygame.image.load("imagem/personagem/amigo/0.png").convert_alpha()


# 2 - Funcao Jogo
def jogo():

    # Posicao inicial do personagem
    x_pos = 100
    y_pos = 300
    # Velocidade do personagem nos eixos x e y
    vel_x = 0
    vel_y = 0
    # Modulo da velocidade
    vel = 5

    # Loop de Jogo

    while(True):

        # Cabeçalho Jogo (Clock, event, update)
        clock.tick(fps)

        #Input

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # 4 - Inputs e Updates
            # Perceba como é muito ruim controlar o personagem.
            # Para jogos com esse tipo de movimento, é necessario um sistema mais
            # elaborado, porém, esse não é o foco desse tutorial, aqui apenas estamos 
            # demonstrando como os eventos e teclas funcionam.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    vel_x = vel
                elif event.key == pygame.K_LEFT:
                    vel_x = -vel
                elif event.key == pygame.K_UP:
                    vel_y = -vel
                elif event.key == pygame.K_DOWN:
                    vel_y = vel
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    vel_x = 0
                elif event.key == pygame.K_LEFT:
                    vel_x = 0
                elif event.key == pygame.K_UP:
                    vel_y = 0
                elif event.key == pygame.K_DOWN:
                    vel_y = 0
        
        #Atualizacao
        x_pos += vel_x
        y_pos += vel_y

        #Renderização

        janela.fill("white")        #X      Y
        janela.blit(img_personagem, (x_pos, y_pos))
        pygame.display.flip()
        

jogo()