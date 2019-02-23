import pygame
from settings import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, app, x, y):
        self.groups = app.all_sprites, app.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((Screen.TSIZE, Screen.TSIZE))
        self.image.fill(Colors.RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * Screen.TSIZE
        self.rect.y = y * Screen.TSIZE
