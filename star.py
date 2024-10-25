import random
import pygame

class Star:
    def __init__(self, x, y, speed, screen_height, screen_width):
        self.x = x
        self.y = y
        self.size = random.randint(1, 3)
        self.speed = speed
        self.screen_height = screen_height
        self.screen_width = screen_width

    def update(self):
        self.y -= self.speed    
        if self.y < 0:
            self.y = random.randint(self.screen_height, self.screen_height + 50)
            self.x = random.randint(0, self.screen_width)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.size)