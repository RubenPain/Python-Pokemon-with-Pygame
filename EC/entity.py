import pygame
import EC.defines as defines
from EC.text import Txt
import random
from os import path


class Entity(pygame.sprite.Sprite):
    def __init__(self,l, name, img, x, y, life):
        pygame.sprite.Sprite.__init__(self)
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img/pokemon')
        self.pok = defines.pokemon
        self.image = pygame.Surface((150, 150))
        self.pok_img = pygame.image.load(path.join(img_folder, img)).convert_alpha()
        self.pok_img = pygame.transform.scale(self.pok_img, (150, 150))
        self.rect = self.image.get_rect()
        self.image.blit(self.pok_img, self.rect)
        self.image.set_colorkey(defines.Colors.BLACK)

        self.rect.x = x
        self.rect.centery = y
        self.life = life
        self.largeur = l
        self.name = name




class Attaque(pygame.sprite.Sprite):
    def __init__(self,surf, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name_pok = 'Noadkoko'
        self.attribut = defines.pokemon
        self.text = Txt()
        self.text.draw_text(surf, self.attribut.attaque[self.name_pok][0], 70, x, y, defines.Colors.BLACK)
        self.cadre = pygame.Rect.copy(self.text.text_rect)
        pygame.draw.rect(surf, defines.Colors.BLACK, self.cadre, 2)
        self.text.draw_text(surf, self.attribut.attaque[self.name_pok][1], 70, x - 300, y, defines.Colors.BLACK)
        self.cadre1 = pygame.Rect.copy(self.text.text_rect)
        pygame.draw.rect(surf, defines.Colors.BLACK, self.cadre1, 2)
        self.damage = random.randint(5,15)
        self.enm_dmg = random.randint(5,15)



















