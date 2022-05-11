import pygame
import os
import random
pygame.init()

# kolory
DARKRED = pygame.color.THECOLORS['darkred']
LIGHTRED = pygame.color.THECOLORS['palevioletred']
DARKGREEN = pygame.color.THECOLORS['darkgreen']
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
BLACK = pygame.color.THECOLORS['black']
LIGHTGREEN = pygame.color.THECOLORS['lightgreen']

#Tekst
MAIN_FONT = pygame.font.SysFont("comicsans", 50)
LOST_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)

# okno główne
os.environ['SDL_VIDEO_CENTERED'] = '1'    # centrowanie okna
SIZESCREEN = WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode(SIZESCREEN)

# tło
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))

# gracz

PLAYER = pygame.image.load(os.path.join("assets", "pixel_ship_player.png"))

# wrogowie

ENEMY_RED = pygame.image.load(os.path.join("assets", "pixel_ship_red.png"))
ENEMY_BLUE = pygame.image.load(os.path.join("assets", "pixel_ship_blue.png"))
ENEMY_GREEN = pygame.image.load(os.path.join("assets", "pixel_ship_green.png"))

# broń gracza

PLAYER_WEAPON = pygame.image.load(os.path.join("assets", "pixel_laser_player.png"))

# broń wrogów

ENEMY_RED_WEAPON = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
ENEMY_BLUE_WEAPON = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
ENEMY_GREEN_WEAPON = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))

# osłona

SHIELD_1 = pygame.image.load(os.path.join("assets", "blok.png"))
SHIELD_2 = pygame.image.load(os.path.join("assets", "blok.png"))
SHIELD_3 = pygame.image.load(os.path.join("assets", "blok.png"))

SHIELD_LIST = [SHIELD_1, SHIELD_2, SHIELD_3]