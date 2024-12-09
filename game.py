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
        self.rooms = {}  # Dictionnaire pour stocker les pièces
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
            "ajouter": Command("ajouter", "Ajouter une nouvelle pièce.", self.creer_piece, 0),
            "historique": Command("historique", "Afficher l'historique des déplacements.", self.afficher_historique, 0),
            "retour": Command("retour", "Revenir à la position précédente.", self.revenir_en_arriere, 0),
        }

    def creer_piece(self):
        # Permet au joueur de créer une nouvelle pièce.
        name = input("Entrez le nom de la nouvelle pièce : ").strip().lower()
        description = input("Entrez la description de la pièce : ").strip()
        
        if name in self.rooms:
            print(f"La pièce '{name}' existe déjà.")
            return

        # Ajouter la nouvelle pièce
        self.rooms[name] = {"description": description, "exits": {}}

        # Demander à l'utilisateur s'il veut connecter cette pièce à d'autres
        while True:
            connecter = input("Voulez-vous connecter cette pièce à une autre ? (oui/non) : ").strip().lower()
            if connecter == "oui":
                direction = input("Entrez une direction (nord, est, sud, ouest) : ").strip().lower()
                destination = input("Entrez le nom de la pièce à laquelle se connecter : ").strip()

                if destination in self.rooms:
                    self.rooms[name]["exits"][direction] = destination
                    print(f"La pièce '{name}' est maintenant connectée à '{destination}' vers {direction}.")
                else:
                    print(f"La pièce '{destination}' n'existe pas.")
            elif connecter == "non":
                break
            else:
                print("Réponse non reconnue, réessayez.")

        print(f"La pièce '{name}' a été ajoutée avec succès.")
    
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
            prochaine_zone = directions_possibles[direction]
            self.player.historique.append(self.player.position)
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

    def afficher_historique(self):
        if self.player.historique:
            print("Historique des déplacements :")
            for index, lieu in enumerate(self.player.historique, start=1):
                print(f"{index}. {lieu}")
        else:
            print("Aucun déplacement enregistré.")

    def revenir_en_arriere(self):
    # Vérifier si l'historique contient des déplacements
        if len(self.player.historique) > 1:
            # Retirer la position actuelle de l'historique, et récupérer la précédente
            self.player.historique.pop()  # Supprime la dernière pièce (actuelle)
            derniere_position = self.player.historique[-1]  # La dernière pièce dans l'historique
            self.player.changer_position(derniere_position)
            print(f"Vous êtes revenu(e) à {self.player.position}.")
        else:
            print("Aucun déplacement précédent disponible.")


