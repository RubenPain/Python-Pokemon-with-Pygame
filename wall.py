import pygame
from settings import *


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200, 50))
        self.image.fill(Colors.RED)
        self.rect = self.image.get_rect()
        self.rect.x = Screen.WIDTH/2
        self.rect.y = Screen.HEIGHT/2