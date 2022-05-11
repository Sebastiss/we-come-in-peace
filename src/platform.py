import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, image_list, width, height, rect_x, rect_y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.image_list = image_list

    def draw(self, surface):
        if self.width == 70:
            surface.blit(self.image_list[0], self.rect)
        else:
            surface.blit(self.image_list[1], self.rect)
            for i in range(70, self.width - 70, 70):
                surface.blit(self.image_list[2], [self.rect.x + i, self.rect.y])
            surface.blit(self.image_list[2], [self.rect.x + self.width - 70, self.rect.y])
