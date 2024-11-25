"""
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""

# Fonction pour déplacer le joueur
def deplacer(joueur_position, direction):
    if direction not in zones[joueur_position]:
        afficher_message_erreur()
        return joueur_position

    prochaine_zone = zones[joueur_position][direction]

    # Gérer le passage interdit
    if prochaine_zone in zones_interdites:
        print(f"Le passage vers {prochaine_zone} est bloqué. Vous devez résoudre une énigme pour y accéder (fonctionnalité future).")
        return joueur_position

    # Gérer le sens unique
    if direction in sens_unique.get(joueur_position, {}) and not sens_unique[joueur_position][direction]:
        print("Vous ne pouvez pas aller dans cette direction.")
        return joueur_position

    if prochaine_zone:
        print(f"Vous avancez vers {prochaine_zone}.")
        return prochaine_zone
    else:
        afficher_message_erreur()
        return joueur_position

# Boucle principale
def jeu():
    print("Bienvenue dans le jeu ! Tapez 'help' pour voir les commandes disponibles.")
    joueur_position = "entrée"

    while True:
        commande = input(">>> ").strip()

        if commande == "help":
            print("Commandes : nord, est, sud, ouest, quitter")
        elif commande == "quitter":
            print("Merci d'avoir joué !")
            break
        elif commande == "":
            afficher_message_erreur()
        else:
            joueur_position = deplacer(joueur_position, commande)

jeu() 
