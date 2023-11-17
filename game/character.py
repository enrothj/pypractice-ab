class Character:
    def __init__(self, name) -> None:
        self.name = name
        self.stats = {
            "hp": 10,
            "mp": 10,
            "sp": 10,
        }

    def get_stat(self, name: str):
        return self.stats[name]
    
    