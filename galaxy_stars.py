import sys
import random
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from game_stats import GameStats
from button import Button
import pygame

class GalaxyStars:
    # classe geral para gerenciar ativos e comportamento do jogo

    def __init__(self): 
        # inicializa o jogo e cria recursos do jogo
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.stats = GameStats(self)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Galaxy Stars")
        self.stars = []
        self._create_stars(400) 
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.clock = pygame.time.Clock()
        # define a cor do background
        self.bg_color = (230, 230, 230)  # Certifique-se de usar isso ou o da Settings
        self.game_active = False         #Incializa o jogo em estado inativo
        self.play_button = Button(self, "Play")

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:              #PRESSIONOU 1 VEZ SÓ CARA
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:               #TA SEGURANDO PQ?
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        #inicia um jogo novo quando pressionado
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.reset_stats()
            self.game_active = True

            #Descarta quaisquer projeties e aliens
            self.bullets.empty()
            self.aliens.empty()

            #cria uma nova frota e centrealiza
            self._create_fleet()
            self.ship.center_ship()
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        #cria um novo projetil
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        #vamos verificar se algum projetil atingiu um fudido
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)          #Se quiser ser o tiro divino, só colocar o primeiro argumento como false
        if not self.aliens:
            #destroi os projeteis existentes
            self.bullets.empty()
            self._create_fleet()

    def _create_stars(self, num_stars):
        for _ in range(num_stars):
            x = random.randint(0, self.settings.screen_width)
            y = random.randint(0, self.settings.screen_height)
            speed = random.uniform(1, 3)
            star = Star(x, y, speed, self.settings.screen_height, self.settings.screen_width)
            self.stars.append(star)

    def _update_stars(self):
        for star in self.stars:
            star.update()

    def _draw_stars(self):
        for star in self.stars:
            star.draw(self.screen)

    def _create_fleet(self):
        #cria uma frota de alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            #termina uma fileira, e redefini o valor de x e incrementa o valor de y
            current_x = alien_width
            current_y += 2 * alien_height

    def _check_fleet_edges(self):
        #responde apropriamente se algum alien é de direita
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        #faz toda a frota descer e mudar de lado, esquerdistas
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, x_position, y_position):
        #cria alien e posiciona no campo de batalha
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        #verifica se algum alien chegou na parte inferior da tela
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _ship_hit(self):
        #responde a espaconave sendo abatida por um alien
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active = False


    def _update_screen(self):
        #atualiza as imagens na tela e mude para a nova tela
        self.screen.fill(self.settings.bg_color)
        self._draw_stars()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
    
    def run_game(self):
        # inicia o loop principal do jogo
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_stars()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

if __name__ == '__main__':
    # cria uma instância do jogo e executa o jogo
    ai = GalaxyStars()
    ai.run_game()
    