import pygame

class Ship:
    #Classe para cuidar da espaconave

    def __init__(self, ai_game):
        #Inicializa a nave e defina sua posicao inicial
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #sobe a imagem da nave e obtem seu rect
        self.image = pygame.image.load('Jogo/images/aeronave-removebg-preview.png')
        self.rect = self.image.get_rect()
        #comece cada espaconave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        #flags de movimento da nave
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    
    def blitme(self):
        #desenha a espaconave em sua localizacal atual
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #centraliza a nave na tela
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        

