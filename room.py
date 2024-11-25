# Define the Room class.
"""
author = Eman Moussa & Hana Bouabdellah
"""
class Room:
    """
     Classe pour l'implémentation des rooms

    """

    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.indice = False
        self.pnj = {}
        self.cle = False

    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Permet d'obtenir les sorties.

        """
        # Return the room in the given direction if it exists.
        if direction in self.exits:
            return self.exits[direction]
        return None

    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        Affiche les sorties.

        """
        exit_string = "Sorties: "
        for ex in self.exits:
            if self.exits.get(ex) is not None:
                exit_string += ex + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Retourne une longue description de la room.

        """
        self.get_indices()
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_name(self):
        """
        Retourne le nom de la room.

        """
        return self.name

    def get_inventory(self):
        """
        Affiche l'inventaire de la pièce.

        """
        if len(self.inventory)==0 and len(self.pnj)==0:
            print("Il n'y a rien ici.")
        else:
            print("On voit :")
            for i in self.inventory.values():
                print("\t- ",end="")
                print(i)
            for i in self.pnj.values():
                print("\t- ",end="")
                print(i)


    def get_indices(self):
        """
        Préviens le joueur qu'un jeu un disponible dans la room.

        """
        if self.indice is True:
            print("\nUn jeu est disponible, entrez \"jouer\" pour tenter votre chance")

    def get_exlist(self):
        """
        Affiche un tableau contenant les directions vers lesquelles une pièce est présente.

        """
        exlist = []
        for ex in self.exits:
            if self.exits.get(ex) is not None:
                exlist.append(ex)
        return exlist
