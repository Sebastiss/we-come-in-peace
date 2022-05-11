import pygame
import game_module as gm
import bullet as bl


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ship_img = gm.PLAYER
        self.laser_img = gm.PLAYER_WEAPON
        self.rect = self.ship_img.get_rect()
        # Domyślna ilość żyć
        self.lifes = 3
        self.move_x = 0
        self.level = None
        self.direction_of_shoot = 'up'
        self.points = 0

    def turn_right(self):
        self.move_x = 5

    def turn_left(self):
        self.move_x = -5

    def stop(self):
        self.move_x = 0

    def update(self):
        self.rect.x += self.move_x
        # kolizja
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)

        for p in colliding_platforms:
            if self.move_x > 0:
                self.rect.right = p.rect.left
            if self.move_x < 0:
                self.rect.left = p.rect.right
        if not self.lifes:
            self.kill()

    def draw(self, surface):
        surface.blit(self.ship_img, self.rect)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.turn_right()
            if event.key == pygame.K_a:
                self.turn_left()
            if event.key == pygame.K_SPACE:
                self.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and self.move_x > 0:
                self.stop()
            if event.key == pygame.K_a and self.move_x < 0:
                self.stop()

    def shoot(self):
        if len(self.level.set_of_bullets) < 1:
            bullet = bl.Bullet(gm.PLAYER_WEAPON, self.direction_of_shoot, self.rect.centerx, self.rect.centery-30)
            self.level.set_of_bullets.add(bullet)
