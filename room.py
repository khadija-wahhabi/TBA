# room.py

"""
Ce module définit la classe Room, qui représente une pièce dans le jeu.
La classe gère les objets et personnages présents dans la pièce, ainsi que les sorties.
"""

from inventory import Inventory


class Room:
    """
    La classe Room représente une pièce dans un jeu d'aventure.
    Elle permet de gérer les objets, les personnages et les sorties associées à la pièce.
    """

    def __init__(self, name, description, items, characters):
        """
        Le constructeur initialise une nouvelle pièce avec un nom, une description,
        des objets et des personnages.

        :param name: Le nom de la pièce.
        :param description: La description de la pièce.
        :param items: Les objets présents dans la pièce.
        :param characters: Les personnages présents dans la pièce.
        """
        self.name = name
        self.description = description
        self.exits = {}
        for character in characters:
            character.current_room = self
        self.inventory = Inventory("room", items, characters)

    def get_exit(self, direction):
        """
        Récupère la pièce dans la direction spécifiée si elle existe.

        :param direction: La direction vers laquelle le joueur veut se déplacer.
        :return: La pièce dans cette direction si elle existe, sinon None.
        """
        if direction in self.exits:
            return self.exits[direction]
        return None

    def get_exit_string(self):
        """
        Retourne une chaîne décrivant les sorties de la pièce.

        :return: Une chaîne contenant toutes les directions possibles.
        """
        exit_string = "Sorties: "
        for direction in self.exits:
            if self.exits.get(direction) is not None:
                exit_string += direction + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_long_description(self):
        """
        Retourne une description détaillée de la pièce, y compris les sorties.

        :return: Une chaîne de caractères décrivant la pièce et ses sorties.
        """
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
