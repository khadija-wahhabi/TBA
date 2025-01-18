# player.py

"""
Ce module définit la classe Player, qui représente un joueur dans un jeu d'aventure.
La classe gère les actions du joueur telles que se déplacer, 
prendre des objets, et gérer un inventaire.
"""

from inventory import Inventory


class Player:
    """
    La classe Player représente un joueur dans le jeu.
    Elle permet de gérer les informations du joueur comme l'inventaire,
    l'historique des pièces visitées, et les actions du joueur (se déplacer,
    prendre des objets, etc.).
    """

    def __init__(self, name, items):
        """
        Le constructeur initialise un joueur avec un nom, une pièce de départ,
        un historique des pièces visitées, et un inventaire avec un poids limité.

        :param name: Le nom du joueur.
        :param items: Les objets à initialiser dans l'inventaire du joueur.
        """
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = Inventory("player", items, [])
        self.inventory_size = 5

    def move(self, direction):
        """
        Permet au joueur de se déplacer vers une autre pièce.

        :param direction: La direction (par exemple, "nord", "sud") vers laquelle
        le joueur souhaite se déplacer.
        :return: True si le déplacement a réussi, False sinon.
        """
        # Récupère la pièce suivante à partir du dictionnaire des sorties de la pièce actuelle.
        next_room = self.current_room.exits.get(direction)

        # Si la pièce suivante est None, afficher un message d'erreur et retourner False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        self.history.append(self.current_room)
        # Définit la pièce actuelle sur la pièce suivante.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def get_history(self):
        """
        Récupère l'historique des pièces visitées par le joueur.

        :return: Une liste de chaînes de caractères décrivant l'historique des pièces.
        """
        str_history = []

        if len(self.history) == 0:
            str_history.append(
                "\nPas d'historique disponible : vous êtes au point de départ.\n"
            )
            return str_history

        str_history.append("\nVous avez déjà visité les lieux suivants : ")
        for room in self.history:
            description = room.description.split(".")
            str_history.append("     - " + description[0])

        str_history.append("")
        return str_history

    def move_back(self):
        """
        Permet au joueur de revenir à la pièce précédente dans l'historique.

        :return: True si le retour en arrière a réussi, False sinon.
        """
        if len(self.history) == 0:
            print("\nRetour en arrière impossible : vous êtes au point de départ.\n")
            return False
        next_room = self.history.pop()
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def bag_weight(self):
        """
        Calcule le poids total des objets dans l'inventaire du joueur.

        :return: Le poids total des objets dans l'inventaire.
        """
        total_weight = 0
        for item in self.inventory.items:
            total_weight += item.weight

        return total_weight

    def take(self, item):
        """
        Permet au joueur de prendre un objet si cela ne dépasse pas la capacité
        de l'inventaire.

        :param item: L'objet que le joueur souhaite prendre.
        :return: True si l'objet a été ajouté à l'inventaire, False si l'inventaire est trop lourd.
        """
        if item.weight + self.bag_weight() > self.inventory_size:
            return False

        self.inventory.items.append(item)
        return True

    def drop(self, item):
        """
        Permet au joueur de poser un objet de son inventaire.

        :param item: L'objet que le joueur souhaite poser.
        :return: Toujours True après avoir retiré l'objet de l'inventaire.
        """
        self.inventory.items.remove(item)
        return True
