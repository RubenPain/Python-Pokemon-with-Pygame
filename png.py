import pygame
import settings

class Png(pygame.sprite.Sprite):
    def __init__(self, app, x, y):
        self.groups = app.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.app = app
        # création du joueur et sa surface
        self.image = pygame.Surface((settings.Screen.TSIZE, settings.Screen.TSIZE))
        self.rect = self.image.get_rect()
        self.posX = x
        self.posY = y
        self.currentFrame = 2
        self.cells = []
        self.frames = []