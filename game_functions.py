import pygame

import sys

from bullet import Bullets

def check_events(user_settings, screen, stat, button, scoreboard, ship, rect_obj, bullets, fin_bullet):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, user_settings, screen, stat, scoreboard, ship, rect_obj, bullets, fin_bullet)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_button(stat, scoreboard, button, mouse_x, mouse_y, ship, rect_obj)

def check_button(stat, scoreboard, button, mouse_x, mouse_y, ship, rect_obj):
    if button.rect.collidepoint(mouse_x, mouse_y) and not stat.game_active:
        restart_game(stat, scoreboard, ship, rect_obj)   

def check_keydown_events(event, user_settings, screen, stat, scoreboard, ship, rect_obj, bullets, fin_bullet):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(user_settings, screen, stat, scoreboard, ship, rect_obj, bullets, fin_bullet)
    if event.key == pygame.K_p:
        restart_game(stat, scoreboard, ship, rect_obj)

def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def restart_game(stat, scoreboard, ship, rect_obj):
    center_stuff(ship, rect_obj)
    stat.game_active = True
    stat.reset_stats()
    scoreboard.update_board()

def fire_bullet(user_settings, screen, stat, scoreboard, ship, rect_obj, bullets, fin_bullet):
    bullet = Bullets(user_settings, screen, ship)
    if len(bullets) <= 3 and stat.shots_left >= 1:
        if stat.shots_left >= 2:
            bullets.add(bullet)
            stat.shots_left -= 1
        elif stat.shots_left == 1:
            fin_bullet.add(bullet)
            stat.shots_left -= 1
        scoreboard.update_board()

def bullet_function(stat, scoreboard, rect_obj, bullets, fin_bullet):
    for bullet in bullets:
        bullet.update_bullet()
        if pygame.sprite.spritecollideany(rect_obj, bullets):
            bullets.remove(bullet)
            stat.shots_hit += 1
            scoreboard.update_board()
        if bullet.rect.right < 0:
            bullets.remove(bullet)

    for bullet in fin_bullet:
        bullet.update_bullet()
        if pygame.sprite.spritecollideany(rect_obj, fin_bullet):
            fin_bullet.remove(bullet)
            stat.shots_hit += 1
            scoreboard.update_board()
            if stat.shots_hit == 3:
                stat.win = True
            else: stat.lose = True
        elif bullet.rect.right <= 0:
            stat.lose = True
            fin_bullet.remove(bullet)

def center_stuff(ship, rect_obj):
    ship.rect = ship.startRectY
    rect_obj.y = rect_obj.startRectY

def update_screen(user_settings, screen, stat, button, scoreboard, ship, rect_obj, bullets, fin_bullet):
    screen.fill(user_settings.bg_color)
    bullet_function(stat, scoreboard, rect_obj, bullets, fin_bullet)
    rect_obj.update()
    ship.blit_me()
    stat.check_stats()
    scoreboard.draw_board()
    if not stat.game_active:
        button.draw_button()
    pygame.display.flip()