import pygame
from player import Player
import settings
from wall import Wall
from os import path
from tmap import Map
from cam import Camera
import json


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
        img_folder = path.join(game_folder, 'img')
        self.map = Map(path.join(game_folder, "map.txt"))
        self.pl_img = pygame.image.load(path.join(img_folder, settings.P1.P1_img)).convert_alpha()
        with open('img/assets/sprites.json', 'r') as f:
            self.data = json.load(f)

    def create(self):
        #On crée un groupe pour les sprites
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)


    def draw_grid(self):
        for x in range(0, settings.Screen.WIDTH, settings.Screen.TSIZE):
            pygame.draw.line(self.screen, settings.Colors.WHITE, (x, 0), (x, settings.Screen.HEIGHT))
        for y in range(0, settings.Screen.HEIGHT, settings.Screen.TSIZE):
            pygame.draw.line(self.screen, settings.Colors.WHITE, (0, y), (settings.Screen.WIDTH, y))

    def Start(self):
        running = True
        while running:
            # On fixe le jeu à 60 FPS
            self.time = self.clock.tick(settings.Screen.FPS)/1000

            # Récupération des inputes
            for event in pygame.event.get():
                # Pour fermer la fenêtre, on arrête la boucle while
                if event.type == pygame.QUIT:
                    running = False

            # Tous les sprites sont updatés
            self.all_sprites.update()
            self.camera.update(self.player)

            # Tous les sprites sont dessinés
            self.screen.fill(settings.Colors.BLACK)
            self.draw_grid()
            for sprite in self.all_sprites:
                self.screen.blit(sprite.image, self.camera.apply(sprite))


            # Une fois que tout est dessiné, on l'affiche à l'écran
            pygame.display.flip()

            # Quand on sort de la boucle, on ferme le jeu
        pygame.quit()