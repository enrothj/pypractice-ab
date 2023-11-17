from game_board import GameBoard
from entities import Character

class Battle:
    """This class represents a single battle.
    It has a game board and monitors the game state.
    Eventually, it will have parameters on what kind
    of a battle to create."""

    def characters():
        return [Character("Sam"), Character("Tom")]

    def __init__(self):
        self.board = GameBoard(5, 5)
        self.board.init_characters(self.characters)