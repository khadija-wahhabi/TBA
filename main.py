"""
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""

import tkinter as tk
from gameinterface import GameInterface
from game import Game

def launch_game():
    """
    Fonction pour relancer le jeu
    """
    root = tk.Tk()
    game_instance = Game()
    my_game_interface = GameInterface(root, game_instance)
    root.mainloop()
    return my_game_interface.should_restart

def main():
    """
    Fonction Main
    """
    should_restart = True
    while should_restart:
        should_restart = launch_game()

if __name__ == "__main__":
    main()
