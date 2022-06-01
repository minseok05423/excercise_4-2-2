import pygame

from settings import Settings
import game_functions as f
from ship import Ship
from rectangle import Rect
from pygame.sprite import Group
from gamestat import Gamestat

def run_game():
    pygame.init()
    user_settings = Settings()
    screen = pygame.display.set_mode((user_settings.screen_width, user_settings.screen_height))
    pygame.display.set_caption('practice')

    ship = Ship(screen)
    rect_obj = Rect(user_settings, screen)
    bullets = Group()
    stat = Gamestat()

    while True:
        f.check_events(user_settings, screen, stat, ship, rect_obj, bullets)
        stat.check_shots()
        ship.check_flags(user_settings)
        f.update_screen(user_settings, screen, stat, ship, rect_obj, bullets)

run_game()