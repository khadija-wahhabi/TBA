# inventory.py

"""
Ce module définit la classe Inventory, qui représente un inventaire dans le jeu.
L'inventaire peut être associé à un joueur ou à une pièce et contient des objets et des personnages.
"""


class Inventory:
    """
    La classe Inventory représente l'inventaire d'un objet dans le jeu.
    Un inventaire peut contenir des objets et des personnages.
    """

    def __init__(self, object_name, items, characters):
        """
        Initialise un nouvel inventaire pour un objet donné.

        :param object_name: Le nom de l'objet auquel appartient cet inventaire
        (par exemple, "room" ou "player").
        :param items: Une liste d'objets (exemples : objets dans la pièce ou
        dans l'inventaire du joueur).
        :param characters: Une liste de personnages associés à cet inventaire.
        """
        self.object_name = object_name
        self.items = items
        self.characters = characters

    def get_inventory(self):
        """
        Retourne une représentation sous forme de liste de l'inventaire, incluant
        les objets et les personnages.

        :return: Une liste de chaînes de caractères représentant l'inventaire.
                 Si l'inventaire est vide, un message spécifique est renvoyé.
        """
        str_inventory = []

        if len(self.items) + len(self.characters) == 0:
            if self.object_name == "room":
                str_inventory.append("\nPièce vide\n")
            elif self.object_name == "player":
                str_inventory.append("\nInventaire du joueur vide\n")
            else:
                return None
            return str_inventory

        if self.object_name == "room":
            str_inventory.append("\nDans cette pièce il y a :")
        elif self.object_name == "player":
            str_inventory.append("\nVous avez en votre possession suivants : ")
        else:
            return None

        for item in self.items:
            str_inventory.append(f"     - {item}")
        for character in self.characters:
            str_inventory.append(f"     - {character}")

        str_inventory.append("")
        return str_inventory
