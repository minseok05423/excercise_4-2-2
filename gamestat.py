class Gamestat():
    def __init__(self, ship, rect_obj):
        self.ship = ship
        self.rect_obj = rect_obj

        self.shots_hit = 0
        self.shots_left = 3

        self.win = False
        self.lose = False
        self.game_active = True

        self.scores = {}
        self.update_score()

    def update_score(self):
        self.scores["shots hit"] = self.shots_hit
        self.scores["shots left"] = self.shots_left

    def check_stats(self):
        if self.lose or self.win:
            self.game_active = False

    def reset_stats(self):
        self.shots_hit = 0
        self.shots_left = 3
        self.win = False
        self.lose = False
        self.game_active = True