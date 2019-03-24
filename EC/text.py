import pygame

class Txt(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font_name = pygame.font.match_font('pokemon')

    def draw_text(self, surface, text, size, x, y, colors):
        self.font = pygame.font.Font(self.font_name, size)
        self.text_surface = self.font.render(text, True, colors)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midleft = (x, y)
        surface.blit(self.text_surface, self.text_rect)
