class GameBoard:
    """
    This class represents the board on which the game's battles take place.
    The board is rectangular and consists of square tiles.
    Each tile has a terrain type, such as grass or stone.
    Each tile can contain an entity, such as a character or an obstacle
    """
    def __init__(self, rows, columns) -> None:
        self.rows = rows
        self.columns = columns
        self.terrain = [[0 for _ in range(rows) for _ in range(columns)]]
        self.entities = [[0 for _ in range(rows)] for _ in range(columns)]

    def row_count(self):
        return self.rows
    
    def column_count(self):
        return self.columns

    def print_board_size(self):
        print(self.rows, self.columns)