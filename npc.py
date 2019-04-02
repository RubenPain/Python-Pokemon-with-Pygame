import pygame
from wall import *
import settings


class NPC(pygame.sprite.Sprite):
    def __init__(self, app, x, y):
        #self.groups = app.walls, app.all_sprites
        pygame.sprite.Sprite.__init__(self)#, self.groups)
        self.app = app
        # création du joueur et sa surface
        self.image = pygame.Surface((settings.Screen.TSIZE, settings.Screen.TSIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pygame.sprite.Sprite.update(self)
