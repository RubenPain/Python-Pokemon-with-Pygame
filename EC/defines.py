import random

class Screen:
    #On définit les variables concernant notre jeu
    WIDTH = 1024
    HEIGHT = 720
    FPS = 60

class Colors:
    # On définit des couleurs à utiliser plus tard
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    X = (125, 125, 125)
    Y = (0, 125, 255)
    Z = (255, 0, 100)

class entity:
    life_enm = random.randint(15,50)

class pokemon:
    poke_list = []
    attaque = ["Charge", "Tonnerre", "Lance-Flamme"]
    poke_list.append([0, "Nosferapti", Colors.Z, 580, 150, 0])
    poke_list.append([0, "Roucool", Colors.Y, 580, 150, 0])
    poke_list.append([0, "Zigzaton", Colors.X, 580, 150, 0])


