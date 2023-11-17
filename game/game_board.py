from character import Character

class GameBoard:
    """
    This class represents the board on which the game's battles take place.
    The board is rectangular and consists of square tiles.
    Each tile has a terrain type, such as grass or stone.
    Each tile can contain an entity, such as a character or an obstacle
    """
    def __init__(self, rows:int,
                 columns:int,
                 terrain, 
                 entities) -> None:
        self.rows = rows
        self.columns = columns
        self.terrain = terrain
        self.entities = entities

    def row_count(self):
        return self.rows
    
    def column_count(self):
        return self.columns

    def print_board_size(self):
        print(self.rows, self.columns)