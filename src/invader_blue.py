from enemy import Enemy
import game_module as gm


class Invader_Blue(Enemy):
    def __init__(self, image, movement_x = 0, movement_y = 0, x = 0, y = 0):
        super().__init__(image, movement_x, movement_y, x, y)
        self.image = image

