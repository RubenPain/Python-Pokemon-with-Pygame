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
    GREENBG = (20, 140, 60)

class entity:
    life_enm = random.randint(15,50)

class pokemon:
    poke_list = []
    attaque = {'Noadkoko':["Bomb-oeuf", "Charge"]}
    poke_list.append([0, "Rhinocorne", 'rhinocorne.png', 530, 140, 0])
    poke_list.append([0, "Insécateur", 'insécateur.png', 530, 140, 0])
    poke_list.append([0, "Smogo", 'smogo.png', 530, 140, 0])
    poke_list.append([0, "Scarabrute", 'scarabrute.png', 530, 140, 0])
    poke_list.append([0, "Arceus", 'arceus.png', 530, 140, 0])


