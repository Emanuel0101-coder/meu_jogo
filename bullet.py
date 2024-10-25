import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #Classe para gerenciar os projeteis disparados da nave
    def __init__(self, ai_game):
        #cria um objeto bullet na posicao atual
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #cria um bullet rect em (0, 0) e, em seguida, define a posicao correta
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.centerx = ai_game.ship.rect.centerx
        self.rect.top = ai_game.ship.rect.top

        #Armazena a posicao do projetil como float
        self.y = float(self.rect.y)
    
    def update(self):
        #Desloca o projetil verticalmente na tela, fazendo parecer que a nave está atirando
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        