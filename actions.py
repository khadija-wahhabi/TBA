# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the
# command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"
# Message if the direction is not possible
MSG2 = "\nLa direction '{direction}' n'existe pas. Essaye plutôt parmi : N, S, E, O, U, D .\n"
# Message if the object has no inventory
MSG3 = "\nCet objet n'a pas d'inventaire. Essaye plutôt 'inventory room' ou 'inventory player'."


class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """

        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]

        if len(direction) == 0:
            print("\nAjouter une direction après le go\n")
            return False

        first_character = direction[0]

        # If the direction is totally wrong
        if first_character not in game.possible_directions:
            print(MSG2.format(direction=direction))
            return False

        # Move the player in the direction specified by the parameter.
        player.move(game.possible_directions[first_character])
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def history(game, list_of_words, number_of_parameters):

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        history_bool = player.get_history()

        for str_char in history_bool:
            print(str_char)

        return True

    def back(game, list_of_words, number_of_parameters):

        player = game.player
        l = len(list_of_words)

        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player.move_back()
        return True

    def check(game, list_of_words, number_of_parameters):

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        inventory = player.inventory
        str_inventory = inventory.get_inventory()

        for str_char in str_inventory:
            print(str_char)

        return True

    def look(game, list_of_words, number_of_parameters):

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        current_room = game.player.current_room
        inventory = current_room.inventory
        str_inventory = inventory.get_inventory()

        for str_char in str_inventory:
            print(str_char)

        return True

    def take(game, list_of_words, number_of_parameters):

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        current_room = player.current_room
        items = current_room.inventory.items
        item_name = list_of_words[1]
        item = None

        for item_ in items:
            if item_name == item_.name:
                item = item_
                break

        if item is None:
            print(
                "\nCet item n'est pas disponible. Utilisez look pour voir "
                "les différents objets disponibles\n"
            )
            return False

        if player.take(item):
            items.remove(item_)
            print(f"\n{item.name} dans le sac\n")
            return True

        print("\nSac trop rempli hésite pas à faire le tri\n")

    def drop(game, list_of_words, number_of_parameters):

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        current_room = player.current_room
        items = player.inventory.items
        item_name = list_of_words[1]
        item = None

        for item_ in items:
            if item_name == item_.name:
                item = item_
                break

        if item is None:
            print(
                "\nCet item n'est pas disponible. Utilisez check pour voir les "
                "différents objets disponibles\n"
            )
            return False

        if player.drop(item):
            current_room.inventory.items.append(item_)
            print(
                f"\n{item.name} déposé dans la pièce suivante : {current_room.name}\n"
            )
            return True

        print("\nImpossible de déposer cet item ici\n")

    def talk(game, list_of_words, number_of_parameters):

        l = len(list_of_words)

        if l < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        current_room = player.current_room
        character_name = ""
        for i in range(len(list_of_words[1:])):
            character_name += list_of_words[i + 1]
            if i < len(list_of_words[1:]) - 1:
                character_name += " "

        talk_character = None

        for character in current_room.inventory.characters:
            if character.name == character_name:
                talk_character = character

        if talk_character is None:
            print(
                f"\nAucun personnage nommé {character_name} dans cette pièce. "
                "Utilise look pour analyser la pièce\n"
            )
            return False

        if talk_character.interact(game):
            print(talk_character.get_msg())
        return True
