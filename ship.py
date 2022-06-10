import pygame

import load_image as l

class Ship():
    def __init__(self, screen):
        self.screen = screen

        b_image = l.loadify("images/ship.bmp")
        self.image = pygame.transform.rotate(b_image, 90)
        self.image_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.image_rect.centery = self.screen_rect.centery
        self.image_rect.right = self.screen_rect.right

        self.moving_up = False
        self.moving_down = False

        self.rect = float(self.image_rect.y)

        self.startRectY = self.rect

    def check_flags(self, user_settings):
        if self.moving_up and self.image_rect.top >= 0:
            self.rect -= user_settings.ship_speed
        elif self.moving_down and self.image_rect.bottom <= self.screen_rect.bottom:
            self.rect += user_settings.ship_speed
        self.image_rect.y = self.rect

    def blit_me(self):
        self.screen.blit(self.image, self.image_rect)

