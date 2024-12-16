"""
Fichier : room.py
Contient la classe Room pour gérer les pièces dans le jeu.
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""

class Room:

    # Dictionnaire des zones et leurs sorties
    zones = {
        "entrée": {"nord": "salon", "est": None, "sud": None, "ouest": None},
        "salon": {"nord": "chambre", "est": "cuisine", "sud": "entrée", "ouest": None},
        "cuisine": {"nord": None, "est": "jardin", "sud": None, "ouest": "salon"},
        "chambre": {"nord": "bureau", "est": None, "sud": "salon", "ouest": "grenier"},
        "grenier": {"nord": None, "est": "chambre", "sud": None, "ouest": None},
        "jardin": {"nord": None, "est": None, "sud": None, "ouest": "cuisine"},
        "bureau": {"nord": None, "est": None, "sud": "chambre", "ouest": None},
    }
    descriptions = {
        "entrée": " l ",
        "salon": " l",
        "cuisine":  " l",
        "chambre": "Vous êtes dans la chambre où vous vous êtes réveillé. Tout semble familier, mais un vide persiste en vous.",
        "grenier": "Un long couloir sombre avec des cadres de photos suspendus aux murs.",
        "jardin": "Vous êtes dans une bibliothèque ancienne. Les étagères sont remplies de livres poussiéreux et un journal attire votre attention.",
        "bureau": "Une cuisine déserte. Une odeur de nostalgie flotte dans l'air."
    }

    # Zones interdites
    zones_interdites = ["chambre", "grenier", "jardin"]

    # Sens unique
    sens_unique = {
        "jardin": {"sud": False},  # Ne peut pas revenir au jardin
        "grenier": {"ouest": False}  # Ne peut pas aller au grenier depuis la chambre
    }

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # Sorties supplémentaires
        self.inventory = {}  # Objets présents dans la pièce
        self.pnj = {}  # Personnages non joueurs présents dans la pièce
        self.indice = False  # Indique si un indice est présent
        self.cle = False  # Indique si une clé est présente

    def ajouter_sortie(self, direction, room):
        # Ajoute une sortie depuis cette pièce.
        self.exits[direction] = room

    def obtenir_sortie(self, direction):
        # Renvoie la destination correspondant à une direction donnée.
        return self.exits.get(direction)

    def afficher_description(self):
        # Affiche la description de la pièce et ses éléments interactifs.
        print(f"Vous êtes dans {self.name}.")
        print(self.description)

        if self.inventory:
            print("Vous voyez ici :")
            for objet in self.inventory.keys():
                print(f"- {objet}")

        if self.indice:
            print("Il y a quelque chose d'intéressant ici... Peut-être un indice.")

        if self.pnj:
            print("Vous remarquez quelqu'un dans la pièce :")
            for nom_pnj in self.pnj.keys():
                print(f"- {nom_pnj}")
