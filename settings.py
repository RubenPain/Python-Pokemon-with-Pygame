

class Screen:
    #On définit les variables concernant notre jeu
    WIDTH = 1024
    HEIGHT = 768
    FPS = 60
    TSIZE = 48
    GRIDWIDTH = WIDTH / TSIZE
    GRIDHEIGHT = HEIGHT / TSIZE

class Colors:
    # On définit des couleurs à utiliser plus tard
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

class P1:
    P1_Speed = 300
    P1_img = 'RED.png'
    P1_json = 'sprites.json'