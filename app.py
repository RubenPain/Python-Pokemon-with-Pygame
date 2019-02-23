import pygame
from player import Player
import settings
from wall import Wall
from os import path

class App():
    def __init__(self):
        #On initialise pygame et on crée la fenêtre grâce aux variables WIDTH et HEIGHT
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((settings.Screen.WIDTH, settings.Screen.HEIGHT))
        pygame.display.set_caption("PyGame")
        self.clock = pygame.time.Clock()
        self.load()

    def load(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def create(self):
        #On crée un groupe pour les sprites
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)

        #... et on l'ajoute au groupe de sprites
        #self.all_sprites.add(self.player)

        #self.all_sprites.add(self.w)
        #self.walls.add(self.w)

    def draw_grid(self):
        for x in range(0, settings.Screen.WIDTH, settings.Screen.TSIZE):
            pygame.draw.line(self.screen, settings.Colors.WHITE, (x, 0), (x, settings.Screen.HEIGHT))
        for y in range(0, settings.Screen.HEIGHT, settings.Screen.TSIZE):
            pygame.draw.line(self.screen, settings.Colors.WHITE, (0, y), (settings.Screen.WIDTH, y))

    def Start(self):
        running = True
        while running:
            # On fixe le jeu à 60 FPS
            self.clock.tick(settings.Screen.FPS)

            # Récupération des inputes
            for event in pygame.event.get():
                # Pour fermer la fenêtre, on arrête la boucle while
                if event.type == pygame.QUIT:
                    running = False

            # Tous les sprites sont updatés
            self.all_sprites.update()

            # Tous les sprites sont dessinés
            self.screen.fill(settings.Colors.BLACK)
            self.draw_grid()
            self.all_sprites.draw(self.screen)


            # Une fois que tout est dessiné, on l'affiche à l'écran
            pygame.display.flip()

            # Quand on sort de la boucle, on ferme le jeu
        pygame.quit()