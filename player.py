"""
Fichier : player.py
Contient la classe Player pour gérer le joueur.
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""

class Player:
    def __init__(self, start_position):
        # Initialisation du joueur.
        self.position = start_position  # Position actuelle
        self.inventory = []  # Inventaire du joueur
        self.historique = [start_position]  # Historique des déplacements
        
    def changer_position(self, nouvelle_position):
        # Change la position actuelle du joueur.
        self.position = nouvelle_position
        self.historique.append(nouvelle_position)  # Enregistre la nouvelle position dans l'historique

    def ajouter_objet(self, objet):
        # Ajoute un objet à l'inventaire du joueur.
        self.inventory.append(objet)

    def afficher_inventaire(self):
        # Affiche le contenu de l'inventaire du joueur.
        if self.inventory:
            print("Votre inventaire : " + ", ".join(self.inventory))
        else:
            print("Votre inventaire est vide.")

