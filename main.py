import pygame
import random
from player import Player
import settings

class App():
    def __init__(self):
        #On initialise pygame et on crée la fenêtre grâce aux variables WIDTH et HEIGHT
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((settings.Screen.WIDTH, settings.Screen.HEIGHT))
        pygame.display.set_caption("PyGame")
        self.clock = pygame.time.Clock()

        #On crée un groupe pour les sprites
        self.all_sprites = pygame.sprite.Group()

        #On crée une instance de la classe Player
        self.player = Player()
        #... et on l'ajoute au groupe de sprites
        self.all_sprites.add(self.player)


App = App()

running = True
while running:
    # On fixe le jeu à 60 FPS
    App.clock.tick(settings.Screen.FPS)

    # Récupération des inputes
    for event in pygame.event.get():
        # Pour fermer la fenêtre, on arrête la boucle while
        if event.type == pygame.QUIT:
            running = False

    # Tous les sprites sont updatés
    App.all_sprites.update()

    # Tous les sprites sont dessinés
    App.screen.fill(settings.Colors.BLACK)
    App.all_sprites.draw(App.screen)

    # Une fois que tout est dessiné, on l'affiche à l'écran
    pygame.display.flip()

    # Quand on sort de la boucle, on ferme le jeu
pygame.quit()