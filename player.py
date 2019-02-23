import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, app, x , y):
        self.groups = app.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.app = app
        self.image = pygame.Surface((settings.Screen.TSIZE, settings.Screen.TSIZE))
        self.image.fill(settings.Colors.GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0


    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.app.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        pygame.sprite.Sprite.update(self)

        # On récupère toutes les touches pressées à cette frame
        keys_pressed = pygame.key.get_pressed()

        # La vitesse est remise à 0 à chaque frame, sauf si on appuie sur la flèche gauche ou la flèche droite
        self.speedX = 0
        if keys_pressed[pygame.K_LEFT]:
            self.speedX = -1
        if keys_pressed[pygame.K_RIGHT]:
            self.speedX = 1

        # On empêche le vaisseau de sortir de l'écran
        if self.rect.right > settings.Screen.WIDTH:
            self.rect.right = settings.Screen.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        # La vitesse est remise à 0 à chaque frame, sauf si on appuie sur la flèche haut ou la flèche bas
        self.speedY = 0
        if keys_pressed[pygame.K_UP]:
            self.speedY = -1
        if keys_pressed[pygame.K_DOWN]:
            self.speedY = 1

        # On bouge le vaisseau en fonction de la vitesse
        if not self.collide_with_walls(self.speedX, self.speedY):
            self.x += self.speedX
            self.y += self.speedY

        self.rect.x = self.x * settings.Screen.TSIZE
        self.rect.y = self.y * settings.Screen.TSIZE


        # On empêche le vaisseau de sortir de l'écran
        if self.rect.bottom > settings.Screen.HEIGHT:
            self.rect.bottom = settings.Screen.HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
