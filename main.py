"""
Fichier : main.py
Point d'entrée du jeu. Contient la boucle principale et les interactions avec le joueur.
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""

from command import Command
from room import Room

# Fonction pour déplacer le joueur d'une pièce à une autre
def deplacer(joueur_position, direction):
    # Gère les déplacements entre les pièces en fonction des directions données par le joueur.
    if direction not in Room.zones[joueur_position]:
        Command.afficher_message_erreur()  # Utilise la méthode statique de la classe Command
        return joueur_position

    prochaine_zone = Room.zones[joueur_position][direction]

    # Gérer le passage interdit
    if prochaine_zone in Room.zones_interdites:
        print(f"Le passage vers {prochaine_zone} est bloqué. Résolvez une énigme pour y accéder.")
        return joueur_position

    # Gérer les sens uniques
    if direction in Room.sens_unique.get(joueur_position, {}) and not Room.sens_unique[joueur_position][direction]:
        print("Vous ne pouvez pas aller dans cette direction.")
        return joueur_position

    # Si le déplacement est valide
    if prochaine_zone:
        print(f"Vous avancez vers {prochaine_zone}.")
        return prochaine_zone
    else:
        Command.afficher_message_erreur()
        return joueur_position

# Boucle principale du jeu
def jeu():
    """
    Initialise et lance la boucle principale du jeu.
    """
    print("Bienvenue dans le jeu ! Tapez 'help' pour voir les commandes disponibles.")
    joueur_position = "entrée"  # Position initiale du joueur

    while True:
        commande = input(">>> ").strip().lower()  # Normalise l'entrée utilisateur

        if commande == "help":
            print("Commandes disponibles : nord, est, sud, ouest, quitter")
        elif commande == "quitter":
            print("Merci d'avoir joué ! À bientôt.")
            break
        elif commande == "":
            Command.afficher_message_erreur()
        else:
            joueur_position = deplacer(joueur_position, commande)

# Démarrage du jeu
if __name__ == "__main__":
    jeu()

