import pygame
from weapon import Weapon


class Ship:
    def __init__(self, game, x, y, health=100):
        self.game = game
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self):
        self.game.screen.blit(self.ship_img, (self.x, self.y))
        # pygame.draw.rect(self.game.screen, (255, 0, 0), (self.x, self.y, 40, 40))
        for bullet in self.lasers:
            bullet.draw(self.game.screen)

    # Dimensions of the image
    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    # Use the ship weapon
    def shoot(self):
        if self.cool_down_counter == 0:
            bullet = Weapon(self.game.screen, self.x, self.y, self.laser_img)
            self.lasers.append(bullet)
            self.cool_down_counter = 1
