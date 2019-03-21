import pygame
from wall import *
from app import *

import settings


class NPC(pygame.sprite.Sprite):
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

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.npc = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'NPC':
                NPC(self, tile_object.x, tile_object.y)
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'Wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False
        self.run()