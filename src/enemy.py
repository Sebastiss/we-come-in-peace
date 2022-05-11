import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, name = None, movement_x = 0, movement_y = 0, x = 0, y = 0):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.direction_of_movement = 'right'
        self.lifes = 1
        self.direction_of_shoot = 'down'
        self.name = name

    def update(self):
        if not self.lifes:
            self.kill()
