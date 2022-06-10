class Settings():
    def __init__(self):
        # set screen settings
        self.screen_width, self.screen_height = 800, 600
        self.bg_color = 230, 230, 230

        # set ship settings
        self.ship_speed = 1.5

        # set rectangle settings
        self.rect_width = 50
        self.rect_height = 50
        self.rect_color = (1, 1, 1)
        self.rect_move_speed = 0.1

        # set bullet settings
        self.bullet_width = 30
        self.bullet_height = 5
        self.bullet_color = (1, 1, 1)
        self.bullet_speed = 1

