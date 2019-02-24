import pygame
import settings

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(settings.Screen.WIDTH/2)
        y = -target.rect.y + int(settings.Screen.HEIGHT/2)
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - settings.Screen.WIDTH), x)
        y = max(-(self.height - settings.Screen.HEIGHT), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)