# Define the Room class.
"""
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""
class Room:
    """
     Classe pour l'implémentation des rooms
    """

    # Dictionnaire des zones et des chemins
    zones = {
        "entrée": {"nord": "salon", "est": None, "sud": None, "ouest": None},
        "salon": {"nord": "chambre", "est": "cuisine", "sud": "entrée", "ouest": None},
        "cuisine": {"nord": "jardin", "est": None, "sud": None, "ouest": "salon"},
        "chambre": {"nord": None, "est": None, "sud": "salon", "ouest": "grenier"},
        "grenier": {"nord": None, "est": "chambre", "sud": None, "ouest": None},
        "jardin": {"nord": None, "est": None, "sud": "cuisine", "ouest": None}
    }

    # Zones interdites
    zones_interdites = ["chambre", "grenier", "jardin"]  

    # Sens unique
    sens_unique = {
        "entrée": {"nord": True},  # Peut aller vers le salon uniquement
        "salon": {"nord": True, "sud": True},  # Ne peut pas revenir directement à l'entrée
        "cuisine": {"sud": False},  # Ne peut pas revenir au jardin
        "chambre": {"ouest": False}  # Ne peut pas aller au grenier depuis la chambre
    }

    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.indice = False
        self.pnj = {}
        self.cle = False


