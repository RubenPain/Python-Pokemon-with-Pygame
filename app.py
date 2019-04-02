import pygame
from player import Player
import settings
from wall import Obstacle, HH
from os import path
from tmap import Tmap
from cam import Camera
from npc import NPC
import json
import EC.menu, EC.entity
import random


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
        self.npc_img = pygame.image.load(path.join(img_folder, settings.NPC.NPC_img)).convert_alpha()
        with open('img/assets/npc.json', 'r') as g:
            self.datanpc = json.load(g)



    def create(self):
        # On crée un groupe pour les sprites
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.hh = pygame.sprite.Group()
        self.combat = pygame.sprite.Group()
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
            if t_objet.name == 'hh':
                HH(self, t_objet.x, t_objet.y, t_objet.width, t_objet.height)
        # Création de la caméra
        self.camera = Camera(self.map.width, self.map.height)
        self.EC = EC.menu.EC()
        self.combat.add(self.EC)
        self.count_fade = True
        self.start_tick = 1000000

    def draw_grid(self):
        # Pour quadriller la map
        for x in range(0, settings.Screen.WIDTH, settings.Screen.TSIZE):
            pygame.draw.line(self.screen, settings.Colors.WHITE, (x, 0), (x, settings.Screen.HEIGHT))
        for y in range(0, settings.Screen.HEIGHT, settings.Screen.TSIZE):
            pygame.draw.line(self.screen, settings.Colors.WHITE, (0, y), (settings.Screen.WIDTH, y))

    def fade(self, surf, width, height):
        fade_white = pygame.Surface((width, height))
        fade_white.fill((255, 255, 255))
        fade_black = pygame.Surface((width, height))
        fade_black.fill((0, 0, 0))
        for alpha in range(0, 300):
            fade_black.set_alpha(alpha)
            surf.blit(fade_black, (0, 0))
            pygame.display.update()
            pygame.time.delay(1)
            fade_white.set_alpha(alpha)
            surf.blit(fade_white, (0, 0))
            pygame.display.update()
            pygame.time.delay(1)


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


            if self.player.hh != 2:
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

            if self.player.hh == 2:
                if self.count_fade:
                    self.fade(self.screen, 1500, 1500)
                    self.count_fade = False
                self.combat.draw(self.screen)
                self.EC.update()
                if self.EC.end_enm:
                    self.count_fade = True
                    self.EC.end_enm = False
                    self.player.hh = 0
                    self.life_now = self.EC.player.life
                    self.EC = EC.menu.EC()
                    self.EC.player.life = 10#self.life_now
                    self.combat.add(self.EC)
                if self.EC.end_pl:
                    self.count_fade = True
                    self.EC.end_pl = False
                    self.player.hh = 0
                    self.player.kill()
                    self.EC = EC.menu.EC()
                    self.combat.add(self.EC)
                    for t_objet in self.map.tmxdata.objects:
                        if t_objet.name == 'player':
                            self.player = Player(self, t_objet.x, t_objet.y)

                if (pygame.time.get_ticks() - self.start_tick) / 1000 > 5:
                    for t_objet in self.map.tmxdata.objects:
                        if t_objet.name == 'hh':
                            HH(self, t_objet.x, t_objet.y, t_objet.width, t_objet.height)
                    self.start_tick = 1000000




            # Une fois que tout est dessiné, on l'affiche à l'écran
            pygame.display.flip()


            # Quand on sort de la boucle, on ferme le jeu
        pygame.quit()