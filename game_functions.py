import pygame

import sys

from bullet import Bullets

def check_events(user_settings, screen, stat, ship, rect_obj, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, user_settings, screen, stat, ship, rect_obj, bullets)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, user_settings, screen, stat, ship, rect_obj, bullets):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(user_settings, screen, stat, ship, rect_obj, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def fire_bullet(user_settings, screen, stat, ship, rect_obj, bullets):
    bullet = Bullets(user_settings, screen, ship)
    if len(bullets) <= 3:
        if stat.shots_left >= 2:
            bullets.add(bullet)
            stat.shots_left -= 1
        elif stat.shots_left == 1:
            create_final_bullet(user_settings, screen, stat, ship, rect_obj, bullets)
            print("a")

def bullet_function(stat, rect_obj, bullets):
    for bullet in bullets:
        bullet.update_bullet()
        if pygame.sprite.spritecollideany(rect_obj, bullets):
            bullets.remove(bullet)
            stat.shots_hit += 1
        if bullet.rect.right < 0:
            bullets.remove(bullet)

def create_final_bullet(user_settings, screen, stat, ship, rect_obj, bullets):
    fin_bullet = Bullets(user_settings, screen, ship)
    while True:
        fin_bullet.update_bullet()
        if fin_bullet.rect.colliderect(rect_obj):
            print("a")
            break


def update_screen(user_settings, screen, stat, ship, rect_obj, bullets):
    screen.fill(user_settings.bg_color)
    bullet_function(stat, rect_obj, bullets)
    rect_obj.update()
    ship.blit_me()
    pygame.display.flip()