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
        self.player = None
        self.rooms = Room.zones  # Dictionnaire pour stocker les pièces
        self.commands = self.initialiser_commandes()  # Commandes disponibles

    def initialiser_jeu(self):
        nom = input("Entrez votre nom: ").strip()
        self.player = Player("chambre", nom)
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.\n")
        self.regarder_autour()

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
        print("\nCommandes disponibles :")
        for cmd in self.commands.values():
            print(f"- {cmd}")
        print()

    def quitter(self):
        # Quitte le jeu.
        print("Merci d'avoir joué ! À bientôt.")
        exit()

    def deplacer(self, direction=None):
        # Gère le déplacement du joueur en fonction de la direction donnée.
        # - direction : Direction souhaitée (nord, sud, est, ou ouest)
        if direction is None:
            # Si aucune direction n'est passée, demander à l'utilisateur
            direction = input("Entrez une direction (nord, est, sud, ouest) : ").strip().lower()

        lieu_actuel = self.player.position
        directions_possibles = Room.zones.get(lieu_actuel, {})

        if direction in directions_possibles and directions_possibles[direction]:
            prochaine_zone = directions_possibles[direction]

            # Vérification des zones interdites
            if prochaine_zone in Room.zones_interdites:
                print(f"Cette zone ({prochaine_zone}) est interdite d'accès.")
                return

            # Vérification du sens unique
            if lieu_actuel in Room.sens_unique:
                if direction in Room.sens_unique[lieu_actuel]:
                    print(f"Le sens vers {prochaine_zone} est bloqué (sens unique).")
                    return

            # Ajouter à l'historique si ce n'est pas un doublon
            if not self.player.historique or self.player.historique[-1] != self.player.position:
                self.player.historique.append(self.player.position)

            # Changer la position du joueur
            self.player.changer_position(prochaine_zone)
            print(f"Vous êtes maintenant dans {self.player.position}.")
        else:
            print("Cette direction est inconnue ou inaccessible depuis cet endroit.")

            
    def jouer(self):
        self.initialiser_jeu()
        while True:
            commande = input("> ").strip().lower()
            if commande == "quit":
                print("Merci d'avoir joué ! À bientôt.")
                break
            elif commande == "help":
                self.afficher_aide()
            elif commande in ["nord", "sud", "est", "ouest"]:
                self.deplacer(commande)
            elif commande == "regarder":
                self.regarder_autour()
            elif commande == "historique":
                self.afficher_historique()
            else:
                print("Commande inconnue. Tapez 'help' pour voir les commandes disponibles.")

    def regarder_autour(self):
        lieu = self.player.position
        description = Room.descriptions.get(lieu, "Lieu inconnu.")
        sorties = Room.obtenir_sortie(lieu)
        print(f"\n{description}\n")
        print(f"Sorties: {sorties}")
        
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


