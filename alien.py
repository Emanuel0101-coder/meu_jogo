import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #Classe para representar um unico alienigena na frota

    def __init__(self, ai_game):
        #inicializa o alienigena e define sua posicao
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Carrega a imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load('Jogo/images/alienking.png')
        self.rect = self.image.get_rect()
        
        #inicia cada alienigena perto do canto superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #armazena a posicao horizontal exata do alienigena
        self.x = float(self.rect.x)
    
    def update(self):
        #move o alien para a direita
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    def _update_aliens(self):
        self.aliens.update()

    def check_edges(self):
        #retorna os de verdade se o alien estiver na borda
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
        