import pygame
import EC.defines as defines
from EC.text import Txt
import random



class Entity(pygame.sprite.Sprite):
    def __init__(self,l, name, colors, x, y, life):
        pygame.sprite.Sprite.__init__(self)
        self.pok = defines.pokemon
        self.image = pygame.Surface((32,64))
        self.image.fill(colors)
        self.rect = self.image.get_rect()
        self.image.blit(self.image, self.rect)
        self.image.set_colorkey(defines.Colors.WHITE)

        self.rect.x = x
        self.rect.centery = y
        self.life = life
        self.largeur = l
        self.name = name




class Attaque(pygame.sprite.Sprite):
    def __init__(self,surf, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name_pok = 'Lugia'
        self.attribut = defines.pokemon
        self.text = Txt()
        self.text.draw_text(surf, self.attribut.attaque[0], 70, x, y, defines.Colors.BLACK)
        self.cadre = pygame.Rect.copy(self.text.text_rect)
        pygame.draw.rect(surf, defines.Colors.BLACK, self.cadre, 2)
        self.damage = random.randint(5,15)
        self.enm_dmg = random.randint(5,15)



















