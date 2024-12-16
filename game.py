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
        self.commands = self.initialiser_commandes()  # Position initiale
        self.history = []  # Historique des déplacements
        self.player = self.demander_nom_utilisateur()  # Commandes disponibles

    def initialiser_commandes(self):
        return {
        "nord": Command("nord", "Aller vers le nord.", lambda: self.deplacer("nord"), 0),
        "est": Command("est", "Aller vers l'est.", lambda: self.deplacer("est"), 0),
        "sud": Command("sud", "Aller vers le sud.", lambda: self.deplacer("sud"), 0),
        "ouest": Command("ouest", "Aller vers l'ouest.", lambda: self.deplacer("ouest"), 0),
        "u": Command("u", "Aller vers le haut (grenier).", lambda: self.deplacer("u"), 0),  
        "d": Command("d", "Aller vers le bas (cave).", lambda: self.deplacer("d"), 0),  
        "help": Command("help", "Afficher l'aide.", self.afficher_aide, 0),
        "quitter": Command("quitter", "Quitter le jeu.", self.quitter, 0),
        "back": Command("back", "Revenir à la dernière position.", self.revenir, 0),
        "journal": Command("journal", "Voir le journal et résoudre des énigmes.", self.voir_journal, 0),
        "historique": Command("historique", "Afficher l'historique des déplacements.", self.afficher_historique, 0),
        }

    def afficher_aide(self):
        print("Commandes disponibles :")
        for cmd in self.commands.values():
            print(f"- {cmd}")

    def quitter(self):
        print("Merci d'avoir joué ! À bientôt.")
        exit()

    def demander_nom_utilisateur(self):
        nom = input("Entrez votre nom : ").strip()
        if not nom:
            print("Nom invalide. Par défaut, vous serez appelé 'Aventurier'.")
            nom = "Aventurier"
        print(f"Bienvenue, {nom} ! Préparez-vous à explorer.")
        return Player(start_position="chambre", name=nom)  # Retourne un joueur avec le nom

    def deplacer(self, direction=None):
        
        if direction is None:  # Si aucune direction n'est spécifiée, demander à l'utilisateur
            direction = input("Entrez une direction (nord, est, sud, ouest, U, D) : ").strip().lower()

        lieu_actuel = self.player.position
        directions_possibles = Room.zones.get(lieu_actuel, {})

        # Ajout de la gestion pour "U" (vers le grenier) et "D" (vers la cave)
        if direction == "u":  # Si la commande est "U", on va vers le grenier
            prochaine_zone = "grenier"
        elif direction == "d":  # Si la commande est "D", on va vers la cave
            prochaine_zone = "cave"
        elif direction in directions_possibles:  # Pour les directions normales
            prochaine_zone = directions_possibles.get(direction)
        else:
            print("Cette direction est inconnue ou inaccessible depuis cet endroit.")
            return

            # Vérification des zones interdites
        if prochaine_zone in Room.zones_interdites:
            print(f"Cette zone ({prochaine_zone}) est interdite d'accès.")
            return

            # Vérification du sens unique
        if lieu_actuel in Room.sens_unique:
             if direction in Room.sens_unique[lieu_actuel]:
                 print(f"Le sens vers {prochaine_zone} est bloqué (sens unique).")
                 return

        # Changer la position du joueur
        self.player.changer_position(prochaine_zone)
        self.history.append(lieu_actuel)
        print(f"Vous êtes maintenant dans {self.player.position}.")
        
    def revenir(self):
        if self.history:
            last_position = self.history.pop()
            self.player.changer_position(last_position)
            print(f"Vous êtes revenu à votre position précédente : {self.player.position}.")
        else:
            print("Vous n'avez pas d'historique de déplacement pour revenir en arrière.")

    def voir_journal(self):
        print("Voici votre journal :")
        print("Vous avez trouvé un journal caché dans une étagère poussiéreuse.")
        print("Il contient des lettres, des photos et des dessins.")
        print("Chaque page semble contenir un indice pour résoudre des énigmes et retrouver votre mémoire.")

    def afficher_historique(self):
        if self.history:
            print("Historique des déplacements :")
            for index, location in enumerate(self.history, 1):
                print(f"{index}. {location}")
        else:
            print("Aucun historique de déplacement disponible.")

    def jouer(self):
        print("Bienvenue dans le jeu ! Tapez 'help' pour voir les commandes disponibles.")
        while True:
            commande = input(">>> ").strip().upper()  # Convertir en majuscules ici
            if commande in self.commands:
                self.commands[commande].action()
            else:
                Command.afficher_message_erreur()

