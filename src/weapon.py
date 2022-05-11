import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    # Move of the bullet
    def move(self, speed):
        self.y += speed

    # Check if the bullet goes out of the game window
    def beyond_the_screen(self, height):
        return not(height >= self.y >= 0)

    def position(self):
        return self
