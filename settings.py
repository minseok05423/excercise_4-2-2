class Settings():
    def __init__(self):
        self.screen_width, self.screen_height = 800, 600
        self.bg_color = 230, 230, 230

        self.ship_speed = 1.5

        self.rect_width = 50
        self.rect_height = 50
        self.rect_color = (1, 1, 1)
        self.rect_move_speed = 1

        self.bullet_width = 30
        self.bullet_height = 5
        self.bullet_color = (1, 1, 1)
        self.bullet_speed = 1

        self.obj_speed = 20