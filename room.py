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
        "cuisine": {"nord": "jardin", "est": "bureau", "sud": None, "ouest": "salon"},
        "chambre": {"nord": None, "est": None, "sud": "salon", "ouest": "grenier"},
        "grenier": {"nord": None, "est": "chambre", "sud": None, "ouest": None},
        "jardin": {"nord": None, "est": None, "sud": "cuisine", "ouest": None},
        "bureau": {"nord": None, "est": None, "sud": None, "ouest": "cuisine"},
    }

    # Zones interdites
    zones_interdites = ["chambre", "grenier", "jardin"]

    # Sens unique
    sens_unique = {
        "entrée": {"nord": True},  # Peut aller vers le salon uniquement
        "cuisine": {"sud": False},  # Ne peut pas revenir au jardin
        "chambre": {"ouest": False}  # Ne peut pas aller au grenier depuis la chambre
    }

    def __init__(self, name, description):
        # Initialisation d'une pièce.
        # - name : Nom de la pièce.
        # - description : Description de la pièce.
        self.name = name
        self.description = description
        self.exits = {}  # Sorties supplémentaires
        self.inventory = {}  # Objets présents dans la pièce
        self.pnj = {}  # Personnages non joueurs présents dans la pièce
        self.indice = False  # Indique si un indice est présent
        self.cle = False  # Indique si une clé est présente

    def ajouter_sortie(self, direction, room):
        # Ajoute une sortie depuis cette pièce.
        # - direction : La direction de la sortie.
        # - room : La pièce cible.
        self.exits[direction] = room
