import pygame

from settings import Settings
import game_functions as f
from ship import Ship
from rectangle import Rect
from pygame.sprite import Group
from gamestat import Gamestat
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    user_settings = Settings()
    screen = pygame.display.set_mode((user_settings.screen_width, user_settings.screen_height))
    pygame.display.set_caption('practice')

    msg = "START"

    ship = Ship(screen)
    rect_obj = Rect(user_settings, screen)
    bullets = Group()
    fin_bullet = Group()
    stat = Gamestat(ship, rect_obj)
    button = Button(screen, msg)
    scoreboard = Scoreboard(user_settings, screen, stat)


    while True:
        f.check_events(user_settings, screen, stat, button, scoreboard, ship, rect_obj, bullets, fin_bullet)
        if stat.game_active:
            ship.check_flags(user_settings)
            f.update_screen(user_settings, screen, stat, button, scoreboard, ship, rect_obj, bullets, fin_bullet)

run_game()