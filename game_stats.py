class GameStats:
    #Identifica todas as estastisticas de Galaxy Stars

    def __init__(self, ai_game):
        #inicializa as estastisticas
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        #inicializa as estastisticas que podem mudar durante o jogo
        self.ships_left = self.settings.ship_limit
        