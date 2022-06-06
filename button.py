import pygame.font

class Button():
    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.button_width, self.button_height = 150, 75
        self.button_color = (100, 100, 100)
        self.txt_color = (1, 1, 1)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect((0, 0), (self.button_width, self.button_height))
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.txt_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)