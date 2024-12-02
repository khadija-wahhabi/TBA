"""
Fichier : main.py
Point d'entrée principal du jeu.
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""

from game import Game

def main():
    print("=== Bienvenue dans notre jeu texte ! ===")
    print("Vous vous réveillez dans la maison de vos grands-parents, sans souvenirs de votre passé.")
    print("Votre mission : explorer la maison, résoudre des énigmes, et retrouver votre mémoire.")
    print("Tapez 'help' à tout moment pour afficher les commandes disponibles.")
    
    # Créer une instance de Game et démarrer le jeu
    game = Game()
    game.jouer()

if __name__ == "__main__":
    main()


# Démarrage du jeu
if __name__ == "__main__":
    jeu()

