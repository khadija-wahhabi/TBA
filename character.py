# character.py

"""
Ce module définit la classe Character, qui représente un personnage dans le jeu.
La classe gère les interactions entre le personnage et le joueur, ainsi que la gestion
de son déplacement et des objets associés.
"""

import random


class Character:
    """
    La classe Character représente un personnage dans le jeu d'aventure.
    Elle permet de gérer le nom, la description, les messages et les objets nécessaires
    pour interagir avec le joueur.
    """

    def __init__(self, name, msgs, description, hidden_msg, needed_item, hated_item):
        """
        Initialise un nouveau personnage avec ses attributs.

        :param name: Le nom du personnage.
        :param msgs: Une liste de messages que le personnage peut dire.
        :param description: Une description du personnage.
        :param hidden_msg: Un message caché que le personnage peut révéler.
        :param needed_item: Un objet que le personnage souhaite que le joueur lui donne.
        :param hated_item: Un objet que le personnage déteste.
        """
        self.name = name
        self.current_room = None
        self.msgs = msgs
        self.hidden_msg = hidden_msg
        self.needed_item = needed_item
        self.description = description
        self.print_index = 0
        self.hated_item = hated_item

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant le personnage.

        :return: Une chaîne décrivant le nom et la description du personnage.
        """
        return f"{self.name} : {self.description} "

    def move(self, game):
        """
        Permet au personnage de se déplacer dans une pièce en fonction de la difficulté du jeu.

        :param game: L'objet du jeu qui contient la difficulté et d'autres informations.
        :return: True si le déplacement a réussi, sinon False.
        """
        if random.random() < game.difficulty:
            possible_exits = [
                exit for exit in self.current_room.exits.values() if exit is not None
            ]
            if not possible_exits:
                return False
            old_room = self.current_room
            characters = old_room.inventory.characters
            self.current_room = random.choice(possible_exits)
            self.current_room.inventory.characters.append(self)
            characters.remove(self)
            return True
        return False

    def get_msg(self):
        """
        Récupère le prochain message du personnage à afficher.

        :return: Le message actuel du personnage.
        """
        if not self.msgs:
            return "\n...\n"

        msg = self.msgs[self.print_index]
        self.print_index = (self.print_index + 1) % len(self.msgs)
        return f"\n{self.name} :  {msg}\n"

    def interact(self, game):
        """
        Permet au personnage d'interagir avec le joueur en fonction des objets qu'il possède.

        :param game: L'objet du jeu qui contient les informations sur le joueur et l'inventaire.
        :return: True si l'interaction a réussi, sinon False.
        """
        if self.hated_item:
            for item in game.player.inventory.items:
                if item.name == self.hated_item.name:
                    print(
                        f"\n{self.name} : Ah je déteste ça ({self.hated_item})! "
                        "Ne reviens plus me parler\n"
                    )
                    return False

        if self.needed_item:
            for item in game.player.inventory.items:
                if item.name == self.needed_item.name:
                    print(
                        f"\nPourrais-tu me passer cet item : {self.needed_item.name}? "
                        "En échange je peux te donner des infos.\n"
                    )
                    print(
                        f"Répondre 'yes' si tu veux donner ton item ({self.needed_item.name})\n"
                    )
                    if input("> ") == "yes":
                        self.msgs.append(self.hidden_msg)
                        self.print_index = len(self.msgs) - 1
                        print(f"\nTu as donné ton item ({self.needed_item.name}).")
                        game.player.inventory.items.remove(item)
                        game.level += 1
                        self.needed_item = None
                    return True
            print(
                f"\nSi tu me ramènes ça : {self.needed_item.name}, je peux peut-être t'aider.\n"
            )
            return False

        return True
