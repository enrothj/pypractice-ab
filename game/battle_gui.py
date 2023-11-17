import tkinter as tk

from battle import Battle

class BattleGUI:
    def __init__(self, root, battle) -> None:
        self.root = root
        self.root.title("Battle")

        self.battle: Battle = battle
        self.board = battle.board
        self.create_gameboard()

    def create_gameboard(self):
        for row in range(self.board.rows):
            for col in range(self.board.columns):
                colors = {
                    0: "white",
                    1: "green",
                    2: "blue"
                }
                terrain_type = self.board.get_terrain(row, col)
                color = colors[terrain_type]
                square = tk.Canvas(self.root, width=50, height=50, background=color)
                square.grid(row=row, column=col)

