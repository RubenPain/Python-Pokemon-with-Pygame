import pygame
import settings

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.twidth = len(self.data[0])
        self.theight = len(self.data)
        self.width = self.twidth * settings.Screen.TSIZE
        self.height = self.theight * settings.Screen.TSIZE

