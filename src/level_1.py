from level import Level
import game_module as gm
import platform as pl
import invader as inv
import random
import bullet as bl
import platfrorms as pla
import pygame


# klasa planszy nr 1
class Level_1(Level):
    def __init__(self, player=None):
        super().__init__(player)
        self.create_platforms()
        self.create_enemies_blue()
        self.create_enemies_green()
        self.create_enemies_red()
        self.enemy_shoot()
        self.enemy_movement()

    def create_platforms(self):
        # platforma 1
        for x in range(140, 290, 50):
            for y in range(510, 610, 20):
                self.set_of_platforms.add(pla.Platforms(gm.SHIELD_1, "shield", 0, 0, x, y))

        # platforma 2
        for x in range(540, 690, 50):
            for y in range(510, 610, 20):
                self.set_of_platforms.add(pla.Platforms(gm.SHIELD_1, "shield", 0, 0, x, y))

        # platforma 3
        for x in range(940, 1090, 50):
            for y in range(510, 610, 20):
                self.set_of_platforms.add(pla.Platforms(gm.SHIELD_1, "shield", 0, 0, x, y))

    def create_enemies_blue(self):
        for x in range(10, 560, 60):
            blue_enemy = [inv.Invader(gm.ENEMY_BLUE, "blue", 2, 0, x, 60)]
            self.set_of_enemies.add(blue_enemy)

    def create_enemies_green(self):
        for x in range(0, 550, 60):
            green_enemy = [inv.Invader(gm.ENEMY_GREEN, "green", 2, 0, x, 120)]
            self.set_of_enemies.add(green_enemy)

    def create_enemies_red(self):
        for x in range(0, 550, 60):
            red_enemy = [inv.Invader(gm.ENEMY_RED, "red", 2, 0, x, 180)]
            self.set_of_enemies.add(red_enemy)

    def enemy_movement(self):
        for enemy in self.set_of_enemies:
            if enemy.direction_of_movement == "right":
                if enemy.rect.right >= gm.WIDTH:
                    for e in self.set_of_enemies:
                        e.direction_of_movement = "left"
                        e.rect.y += 50
                if len(self.set_of_enemies) >= 15:
                    enemy.rect.x += 1
                else:
                    enemy.rect.x += 2

            elif enemy.direction_of_movement == "left":
                if enemy.rect.left <= 0:
                    for e in self.set_of_enemies:
                        e.direction_of_movement = "right"
                        e.rect.y += 50
                if len(self.set_of_enemies) >= 15:
                    enemy.rect.x -= 1
                else:
                    enemy.rect.x -= 2

    def enemy_shoot(self):
        for enemy in self.set_of_enemies:
            r = random.randrange(0, 10000)
            if r < 5:
                if len(self.set_of_enemies_bullets) < 2:
                    if enemy.name == 'blue':
                        bullet = bl.Bullet(gm.ENEMY_BLUE_WEAPON, enemy.direction_of_shoot, enemy.rect.centerx, enemy.rect.centery + 30)
                    elif enemy.name == 'red':
                        bullet = bl.Bullet(gm.ENEMY_RED_WEAPON, enemy.direction_of_shoot, enemy.rect.centerx, enemy.rect.centery + 30)
                    else:
                        bullet = bl.Bullet(gm.ENEMY_GREEN_WEAPON, enemy.direction_of_shoot, enemy.rect.centerx, enemy.rect.centery + 30)
                    self.set_of_enemies_bullets.add(bullet)

