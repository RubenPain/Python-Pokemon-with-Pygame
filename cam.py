import pygame
import settings

class Camera:
    def __init__(self, width, height):
        # Création de notre caméra
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Savoir où il faut dessiner l'entity en fct de l'offset * TSIZE
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        # Same
        return rect.move(self.camera.topleft)

    def update(self, target):
        # Déplacement de la caméra en fct des offsets (offsets est l'inverse du déplacement du player)
        x = -target.rect.x + int(settings.Screen.WIDTH/2)
        y = -target.rect.y + int(settings.Screen.HEIGHT/2)
        # Définir les limites pour que la caméra s'arrête en bordure de map
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - settings.Screen.WIDTH), x)
        y = max(-(self.height - settings.Screen.HEIGHT), y)
        # Update la caméra en fonction de ce que l'on souhaite à chaque frame
        self.camera = pygame.Rect(x, y, self.width, self.height)