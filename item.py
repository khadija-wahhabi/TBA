# item.py

"""
Ce module définit la classe Item, qui représente un objet dans le jeu.
Chaque objet possède un nom, une description et un poids.
"""


class Item:
    """
    La classe Item représente un objet dans le jeu avec un nom, une description et un poids.
    """

    def __init__(self, name, description, weight):
        """
        Initialise un nouvel objet avec ses caractéristiques.

        :param name: Le nom de l'objet.
        :param description: Une description de l'objet.
        :param weight: Le poids de l'objet en kilogrammes.
        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant l'objet avec son nom,
        sa description et son poids.

        :return: Une chaîne décrivant l'objet.
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"
