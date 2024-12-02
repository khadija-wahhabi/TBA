"""
Fichier : game.py
Contient la classe Game pour gérer la logique principale du jeu.
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""

from player import Player
from room import Room
from command import Command

class Game:
    
    def __init__(self):
        # Initialise le jeu :
        # - Création du joueur.
        # - Chargement des commandes.
        self.player = Player("entrée")  # Position initiale
        self.commands = self.initialiser_commandes()  # Commandes disponibles

    def initialiser_commandes(self):
        # Initialise les commandes disponibles dans le jeu.
        return {
            "nord": Command("nord", "Aller vers le nord.", self.deplacer, 0),
            "est": Command("est", "Aller vers l'est.", self.deplacer, 0),
            "sud": Command("sud", "Aller vers le sud.", self.deplacer, 0),
            "ouest": Command("ouest", "Aller vers l'ouest.", self.deplacer, 0),
            "help": Command("help", "Afficher l'aide.", self.afficher_aide, 0),
            "quitter": Command("quitter", "Quitter le jeu.", self.quitter, 0),
        }

    def afficher_aide(self):
        # Affiche les commandes disponibles pour le joueur.
        print("Commandes disponibles :")
        for cmd in self.commands.values():
            print(f"- {cmd}")

    def quitter(self):
        # Quitte le jeu.
        print("Merci d'avoir joué ! À bientôt.")
        exit()

    def deplacer(self, direction=None):
    # Gère le déplacement du joueur en fonction de la direction donnée.
    # - direction : Direction souhaitée (nord, sud, est, ouest).
    if direction is None:
        # Si aucune direction n'est passée, demander à l'utilisateur
        direction = input("Entrez une direction (nord, est, sud, ouest) : ").strip().lower()

    lieu_actuel = self.player.position
    directions_possibles = Room.zones.get(lieu_actuel, {})

    if direction in directions_possibles and directions_possibles[direction]:
        # Si la direction est valide et mène à un lieu existant
        prochaine_zone = directions_possibles[direction]
        self.player.changer_position(prochaine_zone)
        print(f"Vous êtes maintenant dans {self.player.position}.")
    else:
        # Si la direction est invalide ou non disponible
        print("Cette direction est inconnue ou inaccessible depuis cet endroit.")

    def jouer(self):
        # Démarre la boucle principale du jeu.
        print("Bienvenue dans le jeu ! Tapez 'help' pour voir les commandes disponibles.")

        while True:
            commande = input(">>> ").strip().lower()
            if commande in self.commands:
                self.commands[commande].action()
            else:
                Command.afficher_message_erreur()
