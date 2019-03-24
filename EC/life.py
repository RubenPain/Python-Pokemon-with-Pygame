import pygame
import EC.defines as defines



class Life(pygame.sprite.Sprite):
    def draw_life_bar(self, l, surf, x, y, pct):
        if pct < 0:
            pct = 0
        self.BAR_LENGTH = l
        self.BAR_HEIGHT = 10
        self.fill = (pct/self.BAR_LENGTH)*self.BAR_LENGTH
        self.outline_rect = pygame.Rect(x, y, self.BAR_LENGTH, self.BAR_HEIGHT)
        self.fill_rect = pygame.Rect(x, y, self.fill, self.BAR_HEIGHT)
        pygame.draw.rect(surf, defines.Colors.GREEN, self.fill_rect)
        pygame.draw.rect(surf, defines.Colors.WHITE, self.outline_rect, 2)