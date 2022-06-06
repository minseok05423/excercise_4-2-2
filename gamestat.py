class Gamestat():
    def __init__(self, ship, rect_obj):
        self.ship = ship
        self.rect_obj = rect_obj

        self.shots_hit = 0
        self.shots_left = 3
        self.win = False
        self.lose = False
        self.game_active = True

    def check_stats(self):
        if self.lose or self.win:
            self.game_active = False

    def reset_stats(self):
        self.shots_hit = 0
        self.shots_left = 3
        self.win = False
        self.lose = False
        self.game_active = True