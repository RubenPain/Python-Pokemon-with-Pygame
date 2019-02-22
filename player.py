import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 64))
        self.image.fill(settings.Colors.GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = settings.Screen.WIDTH / 2
        self.rect.bottom = settings.Screen.HEIGHT - 10
        self.speedX = 0
        self.speedY = 0


    def update(self):
        pygame.sprite.Sprite.update(self)

        # On récupère toutes les touches pressées à cette frame
        keys_pressed = pygame.key.get_pressed()

        # La vitesse est remise à 0 à chaque frame, sauf si on appuie sur la flèche gauche ou la flèche droite
        self.speedX = 0
        if keys_pressed[pygame.K_LEFT]:
            self.speedX = -5
        if keys_pressed[pygame.K_RIGHT]:
            self.speedX = 5

        # On bouge le vaisseau en fonction de la vitesse
        self.rect.x += self.speedX

        # On empêche le vaisseau de sortir de l'écran
        if self.rect.right > settings.Screen.WIDTH:
            self.rect.right = settings.Screen.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        # La vitesse est remise à 0 à chaque frame, sauf si on appuie sur la flèche haut ou la flèche bas
        self.speedY = 0
        if keys_pressed[pygame.K_UP]:
            self.speedY = -5
        if keys_pressed[pygame.K_DOWN]:
            self.speedY = 5

        # On bouge le vaisseau en fonction de la vitesse
        self.rect.y += self.speedY

        # On empêche le vaisseau de sortir de l'écran
        if self.rect.bottom > settings.Screen.HEIGHT:
            self.rect.bottom = settings.Screen.HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
