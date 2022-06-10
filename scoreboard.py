import pygame.font

class Scoreboard():
    def __init__(self, user_settings, screen, stat):
        self.screen = screen
        self.user_settings = user_settings
        self.stat = stat

        self.screen_rect = self.screen.get_rect()
        self.n = len(self.stat.scores)
        self.line_num = 0
        self.score_image_hash = {}
        self.image_update = {}
        self.num = 0

        self.bg_width = 180
        self.bg_height = 90
        self.bg = pygame.Rect((0, 0), (self.bg_width, self.bg_height))
        self.bg_color = (100, 100, 100)
        self.bg.topright = self.screen_rect.topright

        self.bg_line_height = self.bg_height / (2 * self.n - 1)

        self.font = pygame.font.SysFont(None, 30)
        self.font_color = (1, 1, 1)

        self.set_score()

    def set_score(self):
        self.stat.update_score()
        for score_name, score in self.stat.scores.items():
            line_loc = self.get_line_loc()
            self.prep_score(score_name, score, line_loc)
        self.line_num = 0

    def get_line_loc(self):
        self.line_num += 1
        line_loc = self.bg.top + self.bg_line_height + (self.line_num - 1) * self.bg_line_height
        return line_loc

    def prep_score(self, score_name, score, line_loc):
        full_score = score_name + " = " + str(score)
        self.score_image = self.font.render(full_score, True, self.font_color, self.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.centerx = self.bg.centerx
        self.score_image_rect.centery = line_loc
        self.score_image_hash[self.score_image] = self.score_image_rect

    def update_board(self):
        self.stat.update_score()
        self.set_score()

    def draw_board(self):
        self.screen.fill(self.bg_color, self.bg)
        for score_image, score_image_rect in self.score_image_hash.items():
            self.screen.blit(score_image, score_image_rect)