import pygame
from player import Player
import settings
from wall import Obstacle
from os import path
from tmap import Tmap
from cam import Camera
from npc import NPC
import json


class App():
    def __init__(self):
        # On initialise pygame et les fichiers grâce à load et on crée la fenêtre grâce aux variables WIDTH et HEIGHT
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((settings.Screen.WIDTH, settings.Screen.HEIGHT))
        pygame.display.set_caption("PyGame")
        self.clock = pygame.time.Clock()
        self.load()


    def load(self):
        # Fonction qui load tous les fichiers (map, images, json)
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img/assets')
        map_folder = path.join(game_folder, 'map')
        self.map = Tmap(path.join(map_folder, "map.tmx"))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.pl_img = pygame.image.load(path.join(img_folder, settings.P1.P1_img)).convert_alpha()
        with open('img/assets/red.json', 'r') as f:
            self.datared = json.load(f)

    def create(self):
        # On crée un groupe pour les sprites
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        '''
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
        '''
        # Pour chaque objet dans la map on le fait apparaitre quand on tombe sur son nom
        for t_objet in self.map.tmxdata.objects:
            if t_objet.name == 'player':
                self.player = Player(self, t_objet.x, t_objet.y)
            if t_objet.name == 'wall':
                Obstacle(self, t_objet.x, t_objet.y, t_objet.width, t_objet.height)
            if t_objet.name == 'npc':
                NPC(self, t_objet.x, t_objet.y)
        # Création de la caméra
        self.camera = Camera(self.map.width, self.map.height)


    def draw_grid(self):
        # Pour quadriller la map
        for x in range(0, settings.Screen.WIDTH, settings.Screen.TSIZE):
            pygame.draw.line(self.screen, settings.Colors.WHITE, (x, 0), (x, settings.Screen.HEIGHT))
        for y in range(0, settings.Screen.HEIGHT, settings.Screen.TSIZE):
            pygame.draw.line(self.screen, settings.Colors.WHITE, (0, y), (settings.Screen.WIDTH, y))

    def Start(self):
        running = True
        while running:
            # On fixe les FPS du jeu
            self.time = self.clock.tick(settings.Screen.FPS)/1000

            # Récupération des inputes
            for event in pygame.event.get():
                # Pour fermer la fenêtre, on arrête la boucle while
                if event.type == pygame.QUIT:
                    running = False

            # Tous les sprites sont updatés
            self.all_sprites.update()
            # Update de la caméra en fonction du joueur puisqu'elle le suit
            self.camera.update(self.player)

            # La map est dessinée
            self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
            # self.draw_grid()
            # Tous les sprites dans le grp sont dessinés
            for sprite in self.all_sprites:
                self.screen.blit(sprite.image, self.camera.apply(sprite))


            # Une fois que tout est dessiné, on l'affiche à l'écran
            pygame.display.flip()

            # Quand on sort de la boucle, on ferme le jeu
        pygame.quit()