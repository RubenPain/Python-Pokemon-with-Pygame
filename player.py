import pygame
import settings
# Pour transmettre deux coordonées plus simplement
spd = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, app, x, y):
        # Directement add au group
        self.groups = app.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.app = app
        #création du joueur et sa surface
        self.image = pygame.Surface((settings.Screen.TSIZE, settings.Screen.TSIZE))
        self.rect = self.image.get_rect()
        self.spd = spd(0, 0)
        self.pos = spd(x, y)
        self.currentFrame = 2
        self.cells = []
        self.frames = []
        for i in range(15):

            # On crée une case
            cell = (self.app.datared[i]['x'], self.app.datared[i]['y'], self.app.datared[i]['width'], self.app.datared[i]['height'])

            # On crée une Surface de la taille d'une case
            frame = pygame.surface.Surface((self.app.datared[i]['width'], self.app.datared[i]['height']))
            # Sur laquelle on dessine la case de la spritesheet qui nous intéresse
            frame.blit(self.app.pl_img, (0, 0), cell)
            frame = pygame.transform.scale(frame,(settings.Screen.TSIZE,settings.Screen.TSIZE))

            # On ajoute la frame à une liste
            self.frames.append(frame)

            # Et pareil pour la case (pour garder ton fonctionnement à toi ou tu reblit une image à chaque frame)
            self.cells.append(cell)



    def collide_with_walls(self, dir):
        # Test des collisions sur x et y en fct des positions player et wall
        if dir == 'x':
            hit = pygame.sprite.spritecollide(self, self.app.walls, False)
            if hit:
                if self.spd.x > 0:
                    self.pos.x = hit[0].rect.left - self.rect.width
                if self.spd.x < 0:
                    self.pos.x = hit[0].rect.right
                self.spd.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hit = pygame.sprite.spritecollide(self, self.app.walls, False)
            if hit:
                if self.spd.y > 0:
                    self.pos.y = hit[0].rect.top - self.rect.height
                if self.spd.y < 0:
                    self.pos.y = hit[0].rect.bottom
                self.spd.y = 0
                self.rect.y = self.pos.y


    def update(self):
        pygame.sprite.Sprite.update(self)

        # On récupère toutes les touches pressées à cette frame
        keys_pressed = pygame.key.get_pressed()
        self.image = self.frames[self.currentFrame]
        self.image.set_colorkey(settings.Colors.BLACK)


        # La vitesse est remise à 0 à chaque frame, sauf si on appuie sur la flèche gauche ou la flèche droite
        self.spd = spd(0,0)
        if keys_pressed[pygame.K_LEFT]:
            # Update des frames pour que celles que l'on souhaite utiliser tourne en boucle
            # Exemple qd on va à gauche notre player n'est pas sur sa frame qui va vers le haut
            self.currentFrame += 1
            if self.currentFrame >= 7 or self.currentFrame < 4:
                self.currentFrame = 4
            self.spd.x = -settings.P1.P1_Speed
            self.image = self.frames[self.currentFrame]
            self.image.set_colorkey(settings.Colors.BLACK)
            # Délai sinon actualisation trop rapide des frames juste pour que ce soit fluide au visu
            pygame.time.delay(130)

        elif keys_pressed[pygame.K_RIGHT]:
            self.currentFrame += 1
            if self.currentFrame >= 11 or self.currentFrame < 8:
                self.currentFrame = 8
            self.spd.x = settings.P1.P1_Speed
            self.image = self.frames[self.currentFrame]
            self.image.set_colorkey(settings.Colors.BLACK)
            pygame.time.delay(130)


        elif keys_pressed[pygame.K_UP]:
            self.currentFrame += 1
            if self.currentFrame >= 15 or self.currentFrame < 12:
                self.currentFrame = 12
            self.spd.y = -settings.P1.P1_Speed
            self.image = self.frames[self.currentFrame]
            self.image.set_colorkey(settings.Colors.BLACK)
            pygame.time.delay(130)

        elif keys_pressed[pygame.K_DOWN]:
            self.currentFrame += 1
            if self.currentFrame >= 3:
                self.currentFrame = 0
            self.spd.y = settings.P1.P1_Speed
            self.image = self.frames[self.currentFrame]
            self.image.set_colorkey(settings.Colors.BLACK)
            pygame.time.delay(130)



        # On bouge le player en fonction de la vitesse multiplié par les FPS pour la fluidité
        self.pos += self.spd * self.app.time

        # Actualisation des positions pour renvoyer les infos à la fct des collisions
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')

