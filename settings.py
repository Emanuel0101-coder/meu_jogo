class Settings:
    "Classe para armazenar as configuracoes do jogo Invasao Alienigena"

    def __init__(self):
        #inicializa as configuracoes do jogo
        #configuracoes de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #configuracoes da velocidade da nave, bicha potente
        self.ship_speed = 2.0
        self.ship_limit = 3

        #configuracoes da bullet 
        self.bullet_speed = 5.0           #ajuste para 10, para ser divino
        self.bullet_width = 3000            #Afins de teste, mude para 3000, assim sera poderoso
        self.bullet_height = 15 
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 10

        #configuracao do alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10        #fleet_direction de 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1

        
               

        