"""
Fichier : room.py
Contient la classe Room pour gérer les pièces dans le jeu.
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""

class Room:

    # Dictionnaire des zones et leurs sorties
    zones = {
        "entrée": {"nord": "salon", "est": None, "sud": None, "ouest": None, "U": "grenier", "D": "cave"},  
        "salon": {"nord": "chambre", "est": "cuisine", "sud": "entrée", "ouest": None, "U": None, "D": "cave"}, 
        "cuisine": {"nord": None, "est": "jardin", "sud": None, "ouest": "salon", "U": None, "D": None},
        "chambre": {"nord": "bureau", "est": None, "sud": "salon", "ouest": None, "U": "grenier", "D": None},  
        "bureau": {"nord": None, "est": None, "sud": "chambre", "ouest": None, "U": None, "D": None},
        "jardin": {"nord": None, "est": None, "sud": None, "ouest": "cuisine", "U": None, "D": None},
        "grenier": {"nord": None, "est": None, "sud": None, "ouest": None, "U": None, "D": "chambre"},  
        "cave": {"nord": None, "est": None, "sud": None, "ouest": None, "U": "salon", "D": None},  
    }
    
    descriptions = {
        "entrée": " l ",
        "salon": " l",
        "cuisine":  " l",
        "chambre": "Vous êtes dans la chambre où vous vous êtes réveillé. Tout semble familier, mais un vide persiste en vous.",
        "bureau": "Une cuisine déserte. Une odeur de nostalgie flotte dans l'air.",
        "jardin": "Vous êtes dans une bibliothèque ancienne. Les étagères sont remplies de livres poussiéreux et un journal attire votre attention.",
        "grenier": "Un long couloir sombre avec des cadres de photos suspendus aux murs.",
        "cave": " Description",
    }

    # Zones interdites
    zones_interdites = ["grenier", "jardin"]

    # Sens unique
    sens_unique = {
        "entrée": {"D": "cave"},  # Ne peut pas revenir au jardin
        "chambre": {"U": "grenier"}  # Ne peut pas aller au grenier depuis la chambre
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
