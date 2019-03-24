import pygame
import EC.defines as defines
from EC.text import Txt
import random
from os import path


class Entity(pygame.sprite.Sprite):
    def __init__(self,l, name, colors, x, y, life):
        pygame.sprite.Sprite.__init__(self)
        game_folder = path.dirname(__file__)
        self.pl_img = pygame.image.load(path.join(game_folder, "test.png")).convert_alpha()
        self.pl_img = pygame.transform.scale(self.pl_img,(64,64))
        self.pl_img = pygame.transform.flip(self.pl_img, 180, 0)
        self.pok = defines.pokemon
        self.image = pygame.Surface((64,64))
        self.image.fill(colors)
        self.rect = self.image.get_rect()
        self.image.blit(self.pl_img, self.rect)
        self.image.set_colorkey(defines.Colors.WHITE)

        self.rect.x = x
        self.rect.centery = y
        self.life = life
        self.largeur = l
        self.name = self.pok.poke_dict[name]




class Attaque(pygame.sprite.Sprite):
    def __init__(self,surf, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name_pok = 'Lugia'
        self.attribut = defines.pokemon
        self.text = Txt()
        self.text.draw_text(surf, self.attribut.poke_dict[self.name_pok][0], 70, x, y, defines.Colors.BLACK)
        self.cadre = pygame.Rect.copy(self.text.text_rect)
        pygame.draw.rect(surf, defines.Colors.BLACK, self.cadre, 2)
        self.damage = random.randint(self.attribut.poke_dict[self.name_pok][1][0], self.attribut.poke_dict[self.name_pok][1][1])#self.attribut.poke_dict[self.name_pok][1]




















