import pygame
import game_module as gm


# ogólna klasa planszy
class Level:
    def __init__(self, player):
        self.set_of_platforms = pygame.sprite.Group()
        self.set_of_bullets = pygame.sprite.Group()
        self.set_of_enemies = pygame.sprite.Group()
        self.set_of_enemies_bullets = pygame.sprite.Group()
        self.player = player
        self.enemies_cross_line = False

    def update(self):
        self._delete_bullet()

        self.set_of_platforms.update()

        self.set_of_bullets.update()
        self.set_of_enemies.update()
        self.set_of_enemies_bullets.update()

    def draw(self, surface):
        self.set_of_platforms.draw(surface)

        self.set_of_bullets.draw(surface)
        self.set_of_enemies.draw(surface)
        self.set_of_enemies_bullets.draw(surface)
        # print(self.set_of_enemies.sprites())
        print(self.player.lifes)
        for i in range(self.player.lifes + 1):
            lives_label = gm.MAIN_FONT.render(f"Lives: {self.player.lifes}", 1, (255, 255, 255))
            level_label = gm.MAIN_FONT.render(f"Score: {self.player.points:0>4}", 1, (255, 255, 255))
            gm.screen.blit(lives_label, (10, 10))
            gm.screen.blit(level_label, (gm.WIDTH - level_label.get_width() - 10, 10))

    def _delete_bullet(self):
        for bullet in self.set_of_bullets:
            # sprwadzamy kolizje z platformami i usuwamy pocisk
            if pygame.sprite.spritecollideany(bullet, self.set_of_platforms):
                bullet.kill()
            # sprwadzamy czy pocisk wyleciał poza planszę i usuwamy pocisk
            if bullet.rect.bottom < 0:
                bullet.kill()

            colliding_enemies = pygame.sprite.spritecollide(
                bullet, self.set_of_enemies, False)
            for enemy in colliding_enemies:
                bullet.kill()
                self.player.points += 50
                if enemy.lifes:
                    enemy.lifes -= 1
            for pl in self.set_of_platforms:
                colliding_platforms = pygame.sprite.collide_rect(bullet, pl)
                if colliding_platforms:
                    pl.kill()
        for bullet in self.set_of_enemies_bullets:
            # sprwadzamy kolizje z platformami i usuwamy pocisk
            if pygame.sprite.spritecollideany(bullet, self.set_of_platforms):
                bullet.kill()
            # sprwadzamy czy pocisk wyleciał poza planszę i usuwamy pocisk
            if bullet.rect.top > gm.HEIGHT:
                bullet.kill()
            colliding_player = pygame.sprite.collide_rect(bullet, self.player)
            if colliding_player:
                bullet.kill()
                self.player.lifes -= 1
            for b in self.set_of_bullets:
                colliding_bullets = pygame.sprite.collide_rect(bullet, b)
                if colliding_bullets:
                    bullet.kill()
                    b.kill()
            for pl in self.set_of_platforms:
                colliding_platforms = pygame.sprite.collide_rect(bullet, pl)
                if colliding_platforms:
                    pl.kill()
        # sprawdzanie kolizji wrogów z platformami
        for enemy in self.set_of_enemies:
            enemy_crash = pygame.sprite.spritecollide(enemy, self.set_of_platforms, False)
            if enemy_crash:
                enemy.kill()
                self.player.lifes -= 1
            if enemy.rect.bottom > gm.HEIGHT - 150:
                print(enemy.rect.bottom)
                print(gm.HEIGHT - 150)
                self.enemies_cross_line = True
