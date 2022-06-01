import sys

class Gamestat():
    def __init__(self):
        self.shots_hit = 0
        self.shots_left = 3

    def check_shots(self):
        if self.shots_left == 0 and self.shots_hit < 3:
            sys.exit()