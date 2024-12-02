"""
Fichier : command.py
Contient la classe Command pour gérer les commandes du jeu.
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""

class Command:

    def __init__(self, command_word, help_string, action, number_of_parameters):
        self.command_word = command_word  # Mot-clé de la commande
        self.help_string = help_string  # Texte d'aide pour expliquer la commande
        self.action = action  # Fonction à exécuter lorsque la commande est appelée
        self.number_of_parameters = number_of_parameters  # Nombre de paramètres requis

    def __str__(self):
        # Retourne une représentation lisible de la commande
        return f"{self.command_word} - {self.help_string}"

    def afficher_message_erreur():
        # Méthode statique pour afficher un message d'erreur générique
        print("Commande non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.")

    def executer(self, *params):
         # Exécute l'action associée à la commande avec les paramètres donnés.
         # Vérifie que le bon nombre de paramètres est fourni avant de l'exécuter.
        if len(params) != self.number_of_parameters:
            print("Nombre incorrect de paramètres pour cette commande.")
        else:
            return self.action(*params)

