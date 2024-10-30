import pygame.font

class Button:
    #para criar botoes no jogo
    def __init__(self, ai_game, msg):
        #inicializa os atributos do botao
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #define as dimensoes e propriedades do botao
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Cria o objeto rect do botao e o centraliza
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #a mensagem do botao precisa ser preparada apenas uma vez
        self._prep_msg(msg)

    def _prep_msg(self, msm):
        #transforma msm em uma imagem renderizada e centraliza o texto no botao
        self.msg_image = self.font.render(msm, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #desenha o botao em branco e dps desenhe a mensagem
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


