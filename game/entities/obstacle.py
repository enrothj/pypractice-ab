class Obstacle:
    def __init__(self, type: int) -> None:
        self.type = type

    def type_name(self):
        types = {
            0: 'stone',
            1: 'grass',
            2: 'water'
        }

        return types[self.type]