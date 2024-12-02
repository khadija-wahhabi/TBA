"""
Fichier : room.py
Contient la classe Room pour gérer les pièces et leurs propriétés dans le jeu.
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""

class Room:

    zones = {
        "entrée": {"nord": "salon", "est": None, "sud": None, "ouest": None},
        "salon": {"nord": "chambre", "est": "cuisine", "sud": "entrée", "ouest": None},
        "cuisine": {"nord": "jardin", "est": None, "sud": None, "ouest": "salon"},
        "chambre": {"nord": None, "est": None, "sud": "salon", "ouest": "grenier"},
        "grenier": {"nord": None, "est": "chambre", "sud": None, "ouest": None},
        "jardin": {"nord": None, "est": None, "sud": "cuisine", "ouest": None}
    }

    zones_interdites = ["chambre", "grenier", "jardin"]  # Liste des zones initialement bloquées
    
    sens_unique = {
        "entrée": {"nord": True},
        "salon": {"nord": True, "sud": True},
        "cuisine": {"sud": False},
        "chambre": {"ouest": False}
    }

    def __init__(self, name, description):
        self.name = name  # Nom de la pièce
        self.description = description  # Description de la pièce
        self.exits = {}  # Sorties possibles
        self.inventory = {}  # Objets présents dans la pièce
        self.indice = False  # Indique si la pièce contient un indice
        self.pnj = {}  # Personnages non-joueurs présents
        self.cle = False  # Indique si la pièce contient une clé

    def afficher_description(self):
        # Affiche les informations de la pièce, y compris les sorties disponibles.
        print(f"Vous êtes dans {self.name}. {self.description}")
        if self.exits:
            print("Sorties disponibles : " + ", ".join(self.exits.keys()))

