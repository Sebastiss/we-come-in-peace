import pygame
import game_module as gm


class Menu:
    def __init__(self, text, width, height, text_colour,
                 background_colour, centerx, cenetry,
                 font_type=None, size=74):
        self.text = str(text)
        self.text_colour = text_colour
        self.font_type = font_type
        self.size = size
        self.width = width
        self.height = height
        self.background_colour = background_colour
        self.font = pygame.font.SysFont("comicsans", 70)
        # self.font = pygame.font.SysFont(self.font_type, self.size)
        self.image = self.font.render(self.text, 1, self.text_colour,
                                      self.background_colour)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = [centerx, cenetry]
        self.rect_image = self.image.get_rect()
        self.rect_image.center = self.rect.center

    def draw(self, surfece):
        surfece.fill(self.background_colour, self.rect)
        surfece.blit(self.image, self.rect_image)