import tkinter as tk
from battle import Battle
from battle_gui import BattleGUI


root = tk.Tk()
battle = Battle()
app = BattleGUI(root, battle)
root.mainloop()