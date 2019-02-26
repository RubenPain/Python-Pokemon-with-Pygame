import pygame
import settings
import pytmx

class Map:
    # Premier test avec un fichier txt
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.twidth = len(self.data[0])
        self.theight = len(self.data)
        self.width = self.twidth * settings.Screen.TSIZE
        self.height = self.theight * settings.Screen.TSIZE

class Tmap:
    def __init__(self, filename):
        # Initialisation de la map et load
        tm = pytmx.load_pygame(filename, pixelalpha = True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        # Contre rendu de toutes les positions des images sur la map + affichage par blit
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

    def make_map(self):
        # Retourner la map pour l'afficher
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface