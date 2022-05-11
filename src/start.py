import pygame
import os
import game_module as gm
from player import Player
import level_1 as LV_1
from menu import Menu

os.environ['SDL_VIDEO_CENTERED'] = '1'          # centrowanie okna
pygame.init()

## ustawienia ekranu i gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
FPS = 60

# inicjalizacja
gracz = Player()
current_level = LV_1.Level_1(gracz)
gracz.level = current_level
gracz.rect.center = (int(gm.WIDTH/2), int(gm.HEIGHT-50))
menu = Menu("Space Invaders - Main Menu", 750, 150, gm.LIGHTRED, gm.BLACK, gm.WIDTH/2, gm.HEIGHT/2, font_type='Arial', size=74)
game_over = Menu("Game over - You lost!!!", 850, 150, gm.LIGHTRED, gm.BLACK, gm.WIDTH/2, gm.HEIGHT/2, font_type='Arial', size=74)
win = Menu("Congratulation you won", 850, 150, gm.DARKGREEN, gm.BLACK, gm.WIDTH/2, gm.HEIGHT/2, font_type="Arial", size=74)

# głowna pętla gry
window_open = True
active_game = False
while window_open:
    screen.blit(gm.BG, (0, 0))
    # pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        elif event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                active_game = True
                pygame.mouse.set_visible(False)
                pygame.time.delay(500)

        if active_game:
            gracz.get_event(event)

    if active_game:
        if gracz.lifes < 0:
            pygame.time.delay(500)
            game_over.draw(screen)
            window_open = False
        # sprawdzanie czy wróg przekroczył linię platform
        if current_level.enemies_cross_line:
            pygame.time.delay(500)
            game_over.draw(screen)
            window_open = False
        if not current_level.set_of_enemies:
            pygame.time.delay(500)
            win.draw(screen)
            window_open = False

        # rysowanie i aktualizacja obiektów
        current_level.update()
        gracz.update()
        current_level.draw(screen)
        gracz.draw(screen)
        current_level.enemy_movement()
        current_level.enemy_shoot()
    else:
        menu.draw(screen)

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(FPS)

pygame.display.flip()
pygame.time.delay(2000)
pygame.quit()