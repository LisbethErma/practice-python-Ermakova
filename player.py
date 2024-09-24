import pygame
from settings import GREEN, WIDTH, HEIGHT

class Player:
    def __init__(self, name):
        self.name = name
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.width = 50
        self.height = 50
        self.color = GREEN
        self.speed = 5
        self.score = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
