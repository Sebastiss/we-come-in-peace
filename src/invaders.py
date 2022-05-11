import pygame, os
from ships import Ship

# Load the images to the game
# Player & NPC
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue.png"))
# Weapon
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))


class SpaceInvader(Ship):
    # Dictionary of images names connected with color invader
    INVADER_COLORS = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, game, x, y, color, health=100):
        super().__init__(game, x, y, health)
        self.ship_img, self.laser_img = self.INVADER_COLORS[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, fall):
        self.y += fall

