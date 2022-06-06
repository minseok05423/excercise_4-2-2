import pygame

from pygame.sprite import Sprite

class Rect(Sprite):
    def __init__(self, user_settings, screen):
        super().__init__()
        self.user_settings = user_settings
        self.screen = screen

        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect((0, 0), (user_settings.rect_width, user_settings.rect_height))

        self.rect.centery = self.screen_rect.centery
        self.rect.x = 50

        self.y = float(self.rect.y)
        self.move = self.user_settings.rect_move_speed

    def update(self):
        self.y += self.move
        self.rect.y = self.y
        self.check_edges()
        self.draw_rect()

    def change_direction(self):
        self.move *= -1

    def check_edges(self):
        if self.rect.bottom >= self.screen_rect.bottom:
            self.change_direction()
            self.rect.x += 40

        if self.rect.top <= 0:
            self.change_direction()
            self.rect.x -= 40

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.user_settings.rect_color, self.rect)