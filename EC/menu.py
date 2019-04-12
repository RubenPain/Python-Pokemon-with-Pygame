import pygame
import EC.defines as defines
from EC.text import Txt
from EC.entity import Entity, Attaque
from EC.life import Life
import random
from os import path






class EC(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((700,350))
        self.image.fill(defines.Colors.GREENBG)

        self.rect = self.image.get_rect()
        self.r = pygame.Rect.copy(self.rect)
        pygame.draw.rect(self.image, defines.Colors.BLACK, self.r, 2)

        self.rect.centerx = defines.Screen.WIDTH/2
        self.rect.centery = defines.Screen.HEIGHT/2

        self.menu = Menu(self.image.get_width() / 2, self.image.get_height())
        self.player = Entity(50, 'Noadkoko', 'noadkoko.png', 32, 140, 50)
        self.player.image = pygame.transform.flip(self.player.image, 180, 0)
        self.rdm = random.randint(0, len(defines.pokemon.poke_list)-1)
        self.life_rdm = random.randint(20, 35)
        self.tirage = 0
        if self.rdm == len(defines.pokemon.poke_list)-1:
            self.tirage = random.randrange(0,2)
            if self.tirage == 1:
                self.life_rdm = 65
                pass
            else:
                self.rdm = random.randint(0, len(defines.pokemon.poke_list)-1)
        defines.pokemon.poke_list[self.rdm][0] = self.life_rdm
        defines.pokemon.poke_list[self.rdm][5] = self.life_rdm
        self.enm = Entity(*defines.pokemon.poke_list[self.rdm])
        self.life = Life()

        self.selct_att = False
        self.selct_base = True
        self.choose_att = True
        self.att = 0
        self.start_tick = 1000000
        self.end_tick = 1000000
        self.kill_enm_tick = 1000000
        self.kill_pl_tick = 1000000
        self.enms = pygame.sprite.Group()
        self.enms.add(self.enm)
        self.end_enm = False
        self.end_pl = False
        self.suite_enm_0 = False
        self.enm_0 = True
        self.suite_player_0 = False
        self.player_0 = True






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
            pygame.draw.rect(self.menu.image, defines.Colors.BLACK, self.menu.r, 2)
            self.attaque = Attaque(self.menu.image, self.menu.x+15, self.menu.y)

        if keys_pressed[pygame.K_RIGHT] and self.selct_att == True:
            pygame.draw.rect(self.menu.image, defines.Colors.RED, self.attaque.cadre, 2)
            pygame.draw.rect(self.menu.image, defines.Colors.BLACK, self.attaque.cadre1, 2)
            self.att = 1
        elif keys_pressed[pygame.K_LEFT] and self.selct_att == True and self.selct_base == False:
            pygame.draw.rect(self.menu.image, defines.Colors.RED, self.attaque.cadre1, 2)
            pygame.draw.rect(self.menu.image, defines.Colors.BLACK, self.attaque.cadre, 2)
            self.att = 1

        if keys_pressed[pygame.K_RETURN] and self.att == 1:
            self.dmg = self.attaque.damage
            self.menu.image.fill(defines.Colors.WHITE)
            pygame.draw.rect(self.menu.image, defines.Colors.BLACK, self.menu.r, 2)
            self.enm.life = self.enm.life - self.dmg
            self.selct_att = False
            self.att = 0
            self.start_tick = pygame.time.get_ticks()
            if self.enm.life > 0:
                self.menu.text.draw_text(self.menu.image, "Vous avez infligé " + str(self.dmg) + " points de dégâts !", 35,
                                     120, self.menu.image.get_height() / 2, defines.Colors.BLACK)

        if (pygame.time.get_ticks()-self.start_tick)/1000>2 and self.enm.life > 0:
            self.enm_dmg = self.attaque.enm_dmg
            self.player.life = self.player.life - self.enm_dmg
            self.start_tick = 1000000
            if self.player.life > 0:
                self.menu.image.fill(defines.Colors.WHITE)
                pygame.draw.rect(self.menu.image, defines.Colors.BLACK, self.menu.r, 2)
                self.menu.text.draw_text(self.menu.image, "Vous avez subi " + str(self.enm_dmg) + " points de dégâts !", 35,
                                         120, self.menu.image.get_height() / 2, defines.Colors.BLACK)
                self.end_tick = pygame.time.get_ticks()



        if (pygame.time.get_ticks()-self.end_tick)/1000>2:
            self.menu.image.fill(defines.Colors.WHITE)
            pygame.draw.rect(self.menu.image, defines.Colors.BLACK, self.menu.r, 2)
            self.menu.draw()
            self.selct_base = True
            self.end_tick = 1000000

        if self.enm.life <= 0 and self.enm_0:
            self.menu.text.draw_text(self.menu.image, "Vous avez infligé " + str(self.dmg)+ " points de dégats." , 35,
                                     120, self.menu.image.get_height() / 2, defines.Colors.BLACK)
            self.menu.text.draw_text(self.menu.image, self.enm.name + " est KO !", 35,
                                     230, (self.menu.image.get_height() / 2)+30, defines.Colors.BLACK)
            self.suite_enm_0 = True
            self.enm_0 = False


        if self.suite_enm_0:
            self.suite_enm_0 = False
            self.kill_enm_tick = pygame.time.get_ticks()

        if (pygame.time.get_ticks()-self.kill_enm_tick)/1000 > 3:
            self.enm.kill()
            self.end_enm = True
            self.kill()
            self.kill_enm_tick = 100000




        if self.player.life <= 0 and self.player_0:
            self.menu.image.fill(defines.Colors.WHITE)
            pygame.draw.rect(self.menu.image, defines.Colors.BLACK, self.menu.r, 2)
            self.menu.text.draw_text(self.menu.image, "Vous avez subi " + str(self.enm_dmg)+ " points de dégats." , 35,
                                     120, self.menu.image.get_height() / 2, defines.Colors.BLACK)
            self.menu.text.draw_text(self.menu.image, self.player.name + " est KO !", 35,
                                     230, (self.menu.image.get_height() / 2)+30, defines.Colors.BLACK)
            self.suite_player_0 = True
            self.player_0 = False


        if self.suite_player_0:
            self.suite_player_0 = False
            self.kill_pl_tick = pygame.time.get_ticks()

        if (pygame.time.get_ticks()-self.kill_pl_tick)/1000 > 3:
            self.end_pl = True
            self.kill_pl_tick = 100000
            self.kill()




    def draw(self):
        self.image.fill(defines.Colors.GREENBG)
        pygame.draw.rect(self.image, defines.Colors.BLACK, self.r, 2)


        if self.player.life > 0:
            self.life.draw_life_bar(self.player.largeur, self.image, self.player.rect.x, self.player.rect.y - 15,
                                self.player.life)
            self.menu.text.draw_text(self.image, self.player.name, 30, self.player.rect.x, self.player.rect.y - 45,
                                     defines.Colors.BLACK)
            self.menu.text.draw_text(self.image, str(self.player.life) + "/" + str(self.player.largeur), 20, self.player.rect.x,
                                 self.player.rect.y - 25, defines.Colors.BLACK)
            self.image.blit(self.player.image, self.player.rect)
        if self.enm.life > 0:
            self.life.draw_life_bar(self.enm.largeur, self.image, self.enm.rect.x,
                                    self.enm.rect.y - 15, self.enm.life)
            self.menu.text.draw_text(self.image, self.enm.name, 30, self.enm.rect.x, self.enm.rect.y - 45, defines.Colors.BLACK)
            self.menu.text.draw_text(self.image, str(self.enm.life)+"/"+str(self.enm.largeur), 20,
                                     self.enm.rect.x, self.enm.rect.y - 25, defines.Colors.BLACK)
            self.enms.draw(self.image)
        self.image.blit(self.menu.image, self.menu.rect)



class Menu(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.text = Txt()

        self.image = pygame.Surface((700, 125))
        self.image.fill(defines.Colors.WHITE)
        self.rect = self.image.get_rect()
        self.r = pygame.Rect.copy(self.rect)
        pygame.draw.rect(self.image, defines.Colors.BLACK, self.r, 2)
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






