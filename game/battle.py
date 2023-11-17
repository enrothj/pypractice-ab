from game_board import GameBoard
from entities.character import Character

class Battle:
    """This class represents a single battle.
    It has a game board and monitors the game state.
    Eventually, it will have parameters on what kind
    of a battle to create."""

    def characters(self):
        return [Character("Sam"), Character("Tom")]
    
    def terrain(self):
        return [_ % 3 for _ in range(25)]
    
    def obstacles(self):
        obst = [0 for _ in range(25)]
        obst[1] = 0
        return obst

    def __init__(self):
        self.board = GameBoard(5, 5)
        self.board.init_terrain(self.terrain())
        self.board.init_obstacles(self.obstacles())
        self.board.init_characters(self.characters())

    def get_board(self):
        return self.board