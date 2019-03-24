import pygame
import EC.defines as defines
from EC.text import Txt
from EC.entity import Entity, Attaque
from EC.life import Life






class EC(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((700,350))
        self.image.fill(defines.Colors.BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = defines.Screen.WIDTH/2
        self.rect.centery = defines.Screen.HEIGHT/2

        self.menu = Menu(self.image.get_width() / 2, self.image.get_height())
        self.player = Entity(100, 'Lugia', defines.Colors.GREEN, 32, 150, 100)
        self.enm = Entity(50, 'Raikou', defines.Colors.RED, 580, 150, 50)
        self.life = Life()

        self.selct_att = False
        self.selct_base = True
        self.choose_att = True
        self.att = 0
        self.start_tick = 1000000
        self.enms = pygame.sprite.Group()
        self.enms.add(self.enm)





    def update(self):
        pygame.sprite.Sprite.update(self)

        keys_pressed = pygame.key.get_pressed()
        self.draw()

        if keys_pressed[pygame.K_LEFT] and self.selct_base:
            pygame.draw.rect(self.menu.image, defines.Colors.RED, self.menu.cadre, 2)
            pygame.draw.rect(self.menu.image, defines.Colors.BLACK, self.menu.cadre1, 2)
            self.selct_att = True

        if keys_pressed[pygame.K_RIGHT] and self.selct_base:
            pygame.draw.rect(self.menu.image, defines.Colors.RED, self.menu.cadre1, 2)
            pygame.draw.rect(self.menu.image, defines.Colors.BLACK, self.menu.cadre, 2)
            self.selct_att = False

        if keys_pressed[pygame.K_RETURN] and self.selct_att == True:
            self.selct_base = False
            self.menu.image.fill(defines.Colors.WHITE)
            self.attaque = Attaque(self.menu.image, self.menu.x+15, self.menu.y)

        if keys_pressed[pygame.K_RIGHT] and self.selct_att == True:
            pygame.draw.rect(self.menu.image, defines.Colors.RED, self.attaque.cadre, 2)
            self.att = 1

        if keys_pressed[pygame.K_RETURN] and self.att == 1:
            self.dmg = self.attaque.damage
            self.menu.image.fill(defines.Colors.WHITE)
            self.menu.text.draw_text(self.menu.image, "Vous avez infligé " + str(self.dmg) + " points de dégâts !", 35,
                                     100, self.menu.image.get_height() / 2, defines.Colors.BLACK)
            self.enm.life = self.enm.life - self.dmg
            self.selct_att = False
            self.att = 0
            self.start_tick = pygame.time.get_ticks()

        if (pygame.time.get_ticks()-self.start_tick)/1000>2:
            self.menu.image.fill(defines.Colors.WHITE)
            self.menu.draw()
            self.selct_base = True
        if (pygame.time.get_ticks()-self.start_tick)/1000>3 and self.enm.life > 0:
            self.enm_dmg = self.attaque.damage
            self.player.life = self.player.life - self.enm_dmg
            self.start_tick = 1000000

        if self.enm.life <= 0:
            self.enm.kill()









    def draw(self):
        self.image.fill(defines.Colors.BLUE)
        self.image.blit(self.player.image, self.player.rect)
        self.enms.draw(self.image)
        self.life.draw_life_bar(self.player.largeur, self.image, self.player.rect.x, self.player.rect.y - 15,
                                self.player.life)
        self.menu.text.draw_text(self.image, str(self.player.life) + "/" + str(self.player.largeur), 20, self.player.rect.x,
                                 self.player.rect.y - 25, defines.Colors.BLACK)
        if self.enm.life > 0:
            self.life.draw_life_bar(self.enm.largeur, self.image, self.enm.rect.x,
                                    self.enm.rect.y - 15, self.enm.life)
            self.menu.text.draw_text(self.image, str(self.enm.life)+"/"+str(self.enm.largeur), 20,
                                     self.enm.rect.x, self.enm.rect.y - 25, defines.Colors.BLACK)
        self.image.blit(self.menu.image, self.menu.rect)



class Menu(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.text = Txt()

        self.image = pygame.Surface((700, 125))
        self.image.fill(defines.Colors.WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        self.x = self.image.get_rect().centerx
        self.y = self.image.get_rect().centery
        self.draw()

    def draw(self):
        self.text.draw_text(self.image, "ATTAQUE", 70, self.x - 300, self.y, defines.Colors.BLACK)
        self.cadre = pygame.Rect.copy(self.text.text_rect)
        self.text.draw_text(self.image, "CAPTURE", 70, self.x + 50, self.y, defines.Colors.BLACK)
        self.cadre1 = pygame.Rect.copy(self.text.text_rect)
        pygame.draw.rect(self.image, defines.Colors.BLACK, self.cadre, 2)
        pygame.draw.rect(self.image, defines.Colors.BLACK, self.cadre1, 2)






