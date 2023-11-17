class Obstacle:
    def __init__(self):
        self.hp = 10
        self.type = 0

    def get_type(self):
        types = {
            0: "tree",
            1: "stone"
        }