# Arquivo para a abstração da classe Personagem
# Autor: Guido Agnezi Deniz
import pygame

# 5 - Personagens

class Personagem():
    def __init__(self, image, x_pos, y_pos, vida, ataque, defesa):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        
    # Render do personagem na tela
    # Utilizado na função de batalha
    def update(self, janela):
        janela.blit(self.image, self.rect)
    
    # Set de posicao do personagem
    # Utilizado exatamente antes de avançar para a função de batalha
    def setPosicao(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
