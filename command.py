# This file contains the Command class.
"""
Authors = WAHHABI Khadija & BOUASSRIA Lamyae
"""

class Command:

    # The constructor.
    def __init__(self, command_word, help_string, action, number_of_parameters):
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    # The string representation of the command.
    def __str__(self):
        return  self.command_word \
                + self.help_string

    def afficher_message_erreur():
        print("Commande non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.")
