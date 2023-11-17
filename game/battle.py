from game_board import GameBoard
from entities import Character

class Battle:
    """This class represents a single battle.
    It has a game board and monitors the game state.
    Eventually, it will have parameters on what kind
    of a battle to create."""

    def characters():
        return [Character("Sam"), Character("Tom")]
    
    def terrain():
        return [0 for _ in range(25)]
    
    def obstacles():
        obst = [0 for _ in range(25)]
        obst[1] = 0
        return obst

    def __init__(self):
        self.board = GameBoard(5, 5)
        self.board.init_terrain(self.terrain)
        self.board.init_obstacles(self.obstacles)
        self.board.init_characters(self.characters)

