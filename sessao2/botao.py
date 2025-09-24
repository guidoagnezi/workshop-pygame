# Arquivo para abstração da classe Button
# Modificado por: Guido Agnezi Deniz

import pygame

class Button():
                                           
    def __init__(self, image, x_pos, y_pos, indice, image_cursor):
            self.image = image
            self.x_pos = x_pos
            self.y_pos = y_pos             # Aqui, a origem do desenho é no centro
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.image_cursor = image_cursor
            self.indice = indice
    
    # Render do botao
    def update(self, janela):
            janela.blit(self.image, self.rect)

    # Checagem de input do botão pelo Mouse
    # Não será utilizado nesse tutorial
    def checkForInput(self, position): # Mouse
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                print("Botão Pressionado!")
                return True
    
    # Desenha o cursor sobre o botão
    # Aqui, a origem do render é no canto superior esquerdo, não no centro
    # Utilize imagens de cursor que se encaixam bem a partir dessa origem
    def desenharCursor(self, janela, indice):
          if indice == self.indice:            # Canto superior esquerdo
                janela.blit(self.image_cursor, (self.rect.x, self.rect.y))

    # Checagem de input pelo cursor
    # Na main, a checagem é feito pelo botão Z do teclado
    def checkInputCursor(self, indice):
          if indice == self.indice:
                print("Botão Pressionado!")
                return True
    