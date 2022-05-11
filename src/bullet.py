import pygame


# klasa reprezentująca pocisk
class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, direction, rect_center_x, rect_center_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [rect_center_x, rect_center_y]
        self.direction_of_shoot = direction

    def update(self):
        if self.direction_of_shoot == 'down':
            self.rect.y += 5
        else:
            self.rect.y -= 10
