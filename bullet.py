import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    def __init__(self, user_settings, screen, ship):
        super().__init__()

        self.screen = screen
        self.user_settings = user_settings
        self.rect = pygame.Rect((50, 50), (self.user_settings.bullet_width, self.user_settings.bullet_height))
        self.rect.center = ship.image_rect.center


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.user_settings.bullet_color, self.rect)

    def update_bullet(self):
        self.draw_bullet()
        self.rect.x -= self.user_settings.bullet_speed


