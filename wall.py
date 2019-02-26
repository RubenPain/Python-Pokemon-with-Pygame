import pygame
from settings import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, app, x, y):
        # Wall de la map txt
        self.groups = app.all_sprites, app.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((Screen.TSIZE, Screen.TSIZE))
        self.image.fill(Colors.RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * Screen.TSIZE
        self.rect.y = y * Screen.TSIZE

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, app, x, y, w, h):
        # Création des obstacles et add au groupe
        self.groups = app.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.app = app
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
