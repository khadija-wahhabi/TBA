"""
Description: Game class

Ce module définit la classe `Game` qui gère l'ensemble du jeu d'aventure.
Le jeu permet au joueur d'explorer différentes pièces, d'interagir avec des personnages,
de résoudre des énigmes et de collecter des objets. Ce jeu est basé sur des commandes textuelles
où le joueur se déplace, parle aux personnages, et interagit avec l'environnement.
"""

# Import modules
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character


class Game:
    """
    La classe `Game` représente le jeu d'aventure dans lequel le joueur doit explorer une maison,
    interagir avec des personnages, résoudre des mystères et trouver des indices.

    Attributs :
        - finished : booléen indiquant si le jeu est terminé.
        - rooms : liste des pièces du jeu.
        - commands : dictionnaire des commandes possibles dans le jeu.
        - player : instance du joueur, représentant le personnage principal.
        - level : niveau actuel du joueur dans l'aventure.
        - time_limit : limite de temps pour terminer le jeu.
        - difficulty : niveau de difficulté du jeu.
        - character_map : dictionnaire associant les personnages à leurs pièces.
        - possible_directions : dictionnaire des directions possibles pour le joueur.
    """

    def __init__(self):
        """
        Initialise un nouvel objet Game. Cette méthode configure les variables de l'état du jeu,
        y compris la liste des pièces, des commandes, et l'état du joueur.

        Les variables suivantes sont définies :
        - finished : False (le jeu n'est pas terminé).
        - rooms : liste vide.
        - commands : dictionnaire vide.
        - player : None (le joueur n'est pas encore défini).
        - level : 0 (niveau initial).
        - time_limit : 50 (limite de temps de jeu).
        - difficulty : 0 (difficulté par défaut).
        - character_map : dictionnaire vide pour les personnages.
        - possible_directions : dictionnaire des directions valides (N, S, E, O, U, D).
        """
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.level = 0
        self.time_limit = 50
        self.difficulty = 0
        self.character_map = {}
        self.possible_directions = {
            "N": "N",
            "n": "N",
            "S": "S",
            "s": "S",
            "E": "E",
            "e": "E",
            "O": "O",
            "o": "O",
            "D": "D",
            "d": "D",
            "U": "U",
            "u": "U",
        }

    # Setup the game
    def setup(self):
        """
        Configure toutes les parties du jeu, y compris les commandes, les pièces, les objets,
        les personnages, ainsi que l'exploration des différentes zones de la maison.

        Cette méthode prépare le jeu en instanciant les pièces (Room), les personnages (Character),
        les objets (Item) et les commandes (Command) qui seront utilisés par le joueur tout au long
        du jeu. Elle crée également les connexions entre les pièces pour que le joueur puisse naviguer.
        """

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command(
            "go",
            " <direction> : se déplacer dans une direction cardinale (N, E, S, O)",
            Actions.go,
            1,
        )
        self.commands["go"] = go
        history = Command(
            "history", " : afficher l'historique des lieux visités", Actions.history, 0
        )
        self.commands["history"] = history
        back = Command("back", " : revenir au dernier lieu visité", Actions.back, 0)
        self.commands["back"] = back
        check = Command("check", " : afficher l'inventaire du joueur", Actions.check, 0)
        self.commands["check"] = check
        look = Command(
            "look",
            " : afficher la liste des objets présents dans cette pièce",
            Actions.look,
            0,
        )
        self.commands["look"] = look
        take = Command(
            "take",
            " <nom d'item>: prendre un item présent dans la pièce",
            Actions.take,
            1,
        )
        self.commands["take"] = take
        drop = Command(
            "drop",
            " <nom d'item>: déposer un item dans la pièce où l'on se trouve",
            Actions.drop,
            1,
        )
        self.commands["drop"] = drop
        talk = Command("talk", " <nom de PNJ>: parler avec un PNJ", Actions.talk, 1)
        self.commands["talk"] = talk

        # Room and character setup

        items_jardin = [Item("os", "donne le au chien ça lui fera plaisir", 2)]
        characters_jardin = [
            Character(
                "chien",
                ["Wafwaf !!!", "Et nan je sais parler t'inquiètes"],
                "Terrifiant berger allemand qui aime bien dormir",
                "Je me souviens d'une ombre qui courait dans le jardin avant de s'enfuir.",
                items_jardin[0],
                None,
            )
        ]
        jardin = Room(
            "Jardin",
            "Un jardin bien entretenu. Un espace verdoyant où sommeille un énorme chien.",
            items_jardin,
            characters_jardin,
        )
        for character in characters_jardin:
            self.character_map[character] = jardin
        self.rooms.append(jardin)

        # Hall
        items_hall = [
            Item("clé", "Donne accès à quelque chose...", 1),
            Item("poignée", "Reste de la poignée cassée de la porte d'entrée", 2),
        ]
        characters_hall = [
            Character(
                "majordome fantôme",
                ["Bienvenue... ou pas.", "Faites attention où vous mettez les pieds."],
                "Un spectre en costume trois pièces, austère mais intriguant",
                "L'intrus a forcé cette porte. Je l'ai vu entrer avant qu'il ne disparaisse.",
                items_hall[0],
                items_hall[1],
            )
        ]
        hall = Room(
            "Hall d'entrée",
            "Une entrée de maison luxueuse. La pièce donne sur d'autres pièces et des escaliers.",
            items_hall,
            characters_hall,
        )
        for character in characters_hall:
            self.character_map[character] = hall
        self.rooms.append(hall)

        # Salon
        items_salon = [Item("marteau", "Utile pour casser", 3)]
        characters_salon = [
            Character(
                "chat",
                ["Miaou, laisse-moi dormir.", "Qu'est-ce que tu regardes ?"],
                "Un chat paresseux allongé sur le canapé",
                "J'ai vu quelqu'un fouiller les tiroirs... il a fait tomber quelque chose.",
                None,
                items_salon[0],
            ),
            Character(
                "fantôme pianiste",
                ["Vous aimez la musique ?", "Je joue souvent pour les étoiles."],
                "Un spectre qui semble lié au vieux piano",
                "Un bruit étrange venait de la baie vitrée... elle a été forcée.",
                items_salon[0],
                None,
            ),
        ]
        salon = Room(
            "Salon",
            "Un salon aux airs bourgeois. La baie vitrée semble cassée...",
            items_salon,
            characters_salon,
        )
        for character in characters_salon:
            self.character_map[character] = salon
        self.rooms.append(salon)

        # Garage
        items_garage = [
            Item("roue", "Pas sûr que ça serve mais on sait jamais", 4),
            Item("TN", "C'est du 43", 1),
        ]
        characters_garage = [
            Character(
                "mécano spectral",
                [
                    "Besoin d'un coup de clé ?",
                    "Cette place a vu de bien meilleures voitures...",
                ],
                "Un ancien mécanicien qui semble nostalgique de son garage",
                "Quelqu'un a laissé ses chaussures ici... des TN. Elles sont trop récentes"
                "pour être à moi.",
                items_garage[1],
                None,
            ),
            Character(
                "rat",
                ["Squeak !", "Toujours à fouiller dans les recoins !"],
                "Un rat curieux et vif qui explore les débris",
                "J'ai trouvé une feuille chiffonnée. Quelqu'un l'a sûrement perdue en fuyant.",
                None,
                items_garage[0],
            ),
        ]
        garage = Room(
            "Garage",
            "Un grand garage. Aucune voiture n'est visible et la pièce est dans le désordre total.",
            items_garage,
            characters_garage,
        )
        for character in characters_garage:
            self.character_map[character] = garage
        self.rooms.append(garage)

        # Cuisine
        items_cuisine = [Item("couteau", "Rien de plus normal dans une cuisine", 1)]
        characters_cuisine = [
            Character(
                "chef fantôme",
                [
                    "Ah, un peu d'aide serait appréciée !",
                    "Mon dernier plat... un désastre !",
                ],
                "Un cuisinier spectral qui semble hanté par son dernier repas",
                "J'ai entendu quelqu'un fouiller dans les tiroirs, "
                "il cherchait quelque chose en panique.",
                items_cuisine[0],
                None,
            )
        ]
        cuisine = Room(
            "Cuisine",
            "Une cuisine totalement équipée. Un des tiroirs est grand ouvert.",
            items_cuisine,
            characters_cuisine,
        )
        for character in characters_cuisine:
            self.character_map[character] = cuisine
        self.rooms.append(cuisine)

        # Escalier
        items_escalier = []
        characters_escalier = [
            Character(
                "tableau vivant",
                [
                    "Tu montes ? Fais attention à ne pas trébucher.",
                    "Ces marches ont vu beaucoup d'histoires.",
                ],
                "Une peinture murale animée représentant une famille ancienne",
                "J'ai vu une ombre monter les escaliers en courant avant de "
                "redescendre précipitamment.",
                None,
                None,
            )
        ]
        escaliers = Room(
            "Escaliers",
            "Des escaliers qui donnent accès à l'étage supérieur. "
            "Sur les murs on peut voir des photos de famille.",
            items_escalier,
            characters_escalier,
        )
        for character in characters_escalier:
            self.character_map[character] = escaliers
        self.rooms.append(escaliers)

        # Chambre 1
        items_chambre1 = [
            Item("casquette", "Aux couleurs du PSG", 0.5),
            Item("console", "Une PlayStation 5 allumée", 5),
        ]
        characters_chambre1 = [
            Character(
                "enfant fantôme",
                ["Chut, je joue !", "T'as une manette ?"],
                "Un jeune garçon spectral concentré sur sa console de jeux",
                "J'ai vu quelqu'un ! Il est entré ici mais quand il m'a vu, "
                "il a laissé tomber quelque chose et s'est enfui.",
                items_chambre1[0],
                None,
            )
        ]
        chambre1 = Room(
            "Chambre d'enfant",
            "Une chambre d'enfant décorée aux couleurs de l'OM. "
            "Du bruit semble provenir du placard.",
            items_chambre1,
            characters_chambre1,
        )
        for character in characters_chambre1:
            self.character_map[character] = chambre1
        self.rooms.append(chambre1)

        # Chambre 2
        items_chambre2 = [Item("collier", "Brisé en mille morceaux au sol", 0.5)]
        characters_chambre2 = [
            Character(
                "ombre mystérieuse",
                ["Pourquoi es-tu ici ?", "Ne touche pas à mes affaires."],
                "Une silhouette indistincte qui semble protéger la pièce",
                "L'intrus a tenté d'ouvrir mon coffre, mais je l'ai fait fuir.",
                items_chambre2[0],
                None,
            )
        ]
        chambre2 = Room(
            "Chambre des parents",
            "Une immense suite parentale. Du bruit semble provenir du placard.",
            items_chambre2,
            characters_chambre2,
        )
        for character in characters_chambre2:
            self.character_map[character] = chambre2
        self.rooms.append(chambre2)

        # Cave
        items_cave = [Item("papier", "Peut contenir un message très important", 0)]
        characters_cave = [
            Character(
                "gardien des secrets",
                [
                    "Tout ce que tu cherches est ici... peut-être.",
                    "L'obscurité révèle parfois la vérité.",
                ],
                "Une entité inquiétante qui semble liée aux mystères de la maison",
                "Sur cette feuille, l'intrus a griffonné : 'Trop de bruits. Je dois partir'.",
                items_cave[0],
                None,
            )
        ]
        cave = Room(
            "Cave",
            "Une cave toute poussiéreuse. La porte d'entrée est grande ouverte.",
            items_cave,
            characters_cave,
        )
        for character in characters_cave:
            self.character_map[character] = cave
        self.rooms.append(cave)

        # Create exits for rooms

        jardin.exits = {
            "N": hall,
            "E": garage,
            "S": None,
            "O": None,
            "U": None,
            "D": None,
        }
        hall.exits = {
            "N": None,
            "E": cuisine,
            "S": jardin,
            "O": salon,
            "U": escaliers,
            "D": None,
        }
        garage.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": jardin,
            "U": None,
            "D": cave,
        }
        cave.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "U": garage,
            "D": None,
        }
        cuisine.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": hall,
            "U": None,
            "D": None,
        }
        salon.exits = {
            "N": None,
            "E": hall,
            "S": jardin,
            "O": None,
            "U": None,
            "D": None,
        }
        escaliers.exits = {
            "N": None,
            "E": chambre1,
            "S": None,
            "O": chambre2,
            "U": None,
            "D": hall,
        }
        chambre1.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": escaliers,
            "U": None,
            "D": None,
        }
        chambre2.exits = {
            "N": None,
            "E": escaliers,
            "S": None,
            "O": None,
            "U": None,
            "D": None,
        }

        # Setup player and starting room
        starter_items = []
        # starter_items.append(Item("Mini potion", "permet de regagner de l'énergie", 0.5))
        # starter_items.append(Item("Machette", "ça peut toujours servir", 2))
        self.player = Player(input("\nEntrez votre nom: "), starter_items)
        self.player.current_room = jardin
        difficulty_selected = False
        while not difficulty_selected:
            difficulty_selected = True
            str_difficulty = input(
                "\nChoisis le niveau de difficulté parmi facile, moyen, difficile, extrême : "
            )
            if str_difficulty == "facile":
                self.difficulty = 0
            elif str_difficulty == "moyen":
                self.difficulty = 0.25
            elif str_difficulty == "difficile":
                self.difficulty = 0.5
            elif str_difficulty == "extrême":
                str_difficulty = 0.75
            else:
                print(
                    "Choisir uniquement parmi les choix proposés avec la bonne orthagraphe !"
                )
                difficulty_selected = False

    # Play the game
    def play(self):
        """
        Lance la boucle principale du jeu.

        Cette méthode exécute le jeu en continu tant que la partie n'est pas terminée. Elle attend
        les entrées du joueur, exécute les commandes correspondantes, et met à jour l'état du jeu
        en fonction des actions du joueur. Si le joueur termine l'aventure ou le temps est écoulé,
        le jeu se termine.
        """
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """
        Traite la commande entrée par l'utilisateur, en la décomposant en mots et en exécutant
        l'action correspondante.

        :param command_string: La chaîne de caractères représentant la commande à exécuter.
        :return: None
        """

        if command_string == "":
            return

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(
                f"\nCommande '{command_word}' non reconnue. Entrez 'aide'"
                "pour voir la liste des commandes disponibles.\n"
            )
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            action_bool = command.action(
                self, list_of_words, command.number_of_parameters
            )

            # Handle commands that affect the game state and characters
            if command_word in ["go", "back", "take", "drop"] and action_bool:
                for character in self.character_map:
                    if character.move(self):
                        self.character_map[character] = character.current_room

                self.time_limit -= 1

                # Check if time is over
                if self.time_limit == 0:
                    print(
                        "\nTemps écoulé, la partie est terminée... "
                        "Retente ta chance une autre fois.\n"
                    )
                    self.finished = True

                # Warn the player about the remaining time
                if self.time_limit % 10 == 0:
                    print(f"\nAttention : {self.time_limit} tours restants !\n")

                # Check if the player has solved the mystery
                if self.level == len(self.character_map):
                    print(
                        "\nBRAVO ! TU ES PARVENU A RESOUDRE LE MYSTERE DE CETTE MAISON !"
                    )
                    print("\nVoici ce qu'il s'est réellement passé : ")
                    print(
                        "\n Un homme habillé tout en noir s'est introduit par "
                        "effraction dans la maison par la baie vitrée avec un marteau."
                    )
                    print(
                        "\nIl est directement allé chercher les objets de "
                        "valeurs dans les chambres puis a entendu du bruit"
                        " et a essayé de se cacher dans le garage."
                    )
                    print(
                        "\nEn traversant les pièces il entendait de plus en plus"
                        " de bruit : le bruit des êtres de la maison"
                    )
                    print(
                        "\nIl a fini par fuir en laissant derrière lui tous"
                        " les indices que tu as trouvé et a reveillé tout le monde"
                    )
                    print("\nTu as maintenant en ta possession sa carte d'identité : ")
                    print(
                        "\nIl s'appelle Bilel Benaich né à Saint-Claude le 26 Mai 2003"
                    )
                    self.finished = True

    # Print the welcome message
    def print_welcome(self):
        """
        Affiche le message de bienvenue du jeu, expliquant l'objectif et la situation du joueur.

        :return: None
        """
        print(
            f"\nBienvenue {self.player.name} dans ce jeu d'aventure ! Il s'est "
            "passé quelque chose d'étrange dans cette maison, "
            "à toi de recoller les morceaux du puzzle."
        )
        print("Entrez 'aide' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())


def main():
    """
    Point d'entrée du jeu. Crée un objet Game et lance la méthode play() pour commencer l'aventure.

    :return: None
    """
    Game().play()


if __name__ == "__main__":
    """
    Lance l'exécution du jeu si le script est exécuté directement.

    :return: None
    """
    main()
