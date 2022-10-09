import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (230, 230, 230)
D_GREY = (190, 190, 190)
RED = (214, 0, 0)
GREEN = (0, 102, 51)
BLUE = (0, 0, 155)
L_AQUA = (0, 230, 230)
YELLOW = (255, 255, 0)
ORANGE = (255, 150, 0)
PURPLE = (51, 0, 102)
D_BROWN = (61, 35, 0)
PINK = (255, 204, 229)
BROWN = (153, 76, 0)
L_Y= (255, 255, 153)
L_GREEN =(157, 229, 94)
L_GREEEN =(153, 255, 204)
L_BLUE = (153, 204, 255)
L_P = (204, 153, 255)
MAROON = (153, 0, 0)
AQUA = (0, 102, 102)
GREEEN = (0, 153, 0)
SKIN = (255, 204, 153)
BABY_RED = (255, 153, 153)

FPS = 240

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 150
PIXEL_SIZE = WIDTH //ROWS

TOOLBAR_HEIGHT = HEIGHT - WIDTH
BG_COLOR = WHITE

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("franklingothicmedium", size)





