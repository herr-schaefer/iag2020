#!/usr/bin/env python3
#
# Authors: Peter Schäfer, Felix Schulthess
#
# - 2020-06-02: Add code to cryptpad
# - 2020-06-03: Add code for gambling with your money
# - 2020-06-04: Add description and location ++ some possibilities to interact with
#

import random

inventory = ["colt", "geisterstein", "kleingeld"]
current_location = "Wagen 3"


locations = {
    "Lokomotive": {
        "description": "Ja heiliges blechle!! Eine preußische P8 treibt diesen Zuga an. Ein gewaltiges Dampfross aus dem Jahr 1913. Beeindrucken, muss man schon sagen. Eine Sache fehtl allerdings, der Lokomotivführer!?",
        "items": [
            "kohlebriketts",
            "schaufel"
        ],
        "exits": {
            "zurück": "Wagen 1",
            "hoch": "Dach Lokomotive"
        }
    },
    "Wagen 1": {
        "description": "In diesem Wagen riecht es nach Zigarrenrauch. Im schumrigem Licht sitzen drei lumpige Gestalten an einem Black-Jack Tisch. An der Wand hinter dem Croupier hängt ein Portrait von Georg Washinton. Der Wagon besitzt ausnahmsweise drei Türen. Eine führt in die Zugtoilette.",
        "items": [
            "geldkassette"
        ],
        "exits": {
            "vor": "Lokomotive",
            "zurück": "Wagen 2",
            "hoch": "Dach Wagen 1",
            "toilette": "Zugtoilette"
        }
    },
    "Wagen 2": {
        "description": "Bei diesem Wagen handelt es sich um einen alten Postwagen. Dieser Wagen ist volgestopft mit Paketen von Tante Marta, die ihre Schmiede nach Wyoming umzieht.",
        "items": [
            "seil",
            "packpapier"
        ],
        "exits": {
            "vor": "Wagen 1",
            "zurück": "Wagen 3",
            "hoch": "Dach Wagen 2"
        }
    },
    "Wagen 3": {
        "description": "Der Wagen hier ist ein alter, verratzter Speisewagen. Es sind keine anderen Passagiere da. In der Ecke steht ein einarmiger Bandit.",
        "items": [
        ],
        "exits": {
            "vor": "Wagen 2",
            "hoch": "Dach Wagen 3"
        }
    },
    "Dach Lokomotive": {
        "description": "Der heiße und rußhaltige Rauch der Lokomotive macht diesen Ort zu einem ungemütlichen Ort. Allerdings läßt sich hier der Stoff aus dem Diamanten sind auflesen. Und um Diamanten geht es hier ja schließlich.",
        "items": [
            "Ruß"
        ],
        "exits": {
            "zurück": "Dach Wagen 1",
            "runter": "Lokomotive"
        }
    },
    "Dach Wagen 1": {
        "description": "Du betritst ein Blechdach. In der vorderen Linken Ecke befindet sich der Abluftschacht der Zugtoilette.",
        "items": [
            "Stecknadel"
        ],
        "exits": {
            "vor": "Dach Lokomotive",
            "zurück": "Dach Wagen 2",
            "runter": "Wagen 1",
        }
    },
    "Dach Wagen 2": {
        "description": "Das Holzdach knarzt verdächtig unter deinen Füßen. Alles was man sich hier holen kann sind Spreißel. Aber zum glück trägst du ja Cowboystifel aus veganem Kunstleder.",
        "items": [
        ],
        "exits": {
            "vor": "Dach Wagen 1",
            "zurück": "Dach Wagen 3",
            "runter": "Wagen 2"
        }
    },
    "Dach Wagen 3": {
        "description": "Ein rostiges Blechdach schmückt diesen Wagen. In der Mitte ist das Blech blauschwarz gefärbt.",
        "items": [
        ],
        "exits": {
            "vor": "Dach Wagen 2",
            "runter": "Wagen 3"
        }
    },
    "Zugtoilette": {
        "description": "Wie zu erwarten riecht es hier wie auf dem Schulklo! Hast du etwas anderes erwartet? An einer Wand hängt ein Portrait von dir mit der Überschwift: 'WANTED DEAD OR ALIVE'",
        "items": [
            "Klobürste"
        ],
        "exits": {
            "vor": "Wagen 1",
        }
    }
}


def welcome():
    print("    Wilkommmen zu...")
    print(r"""
            .-.____________________.-.
     ___ _.' .-----.    _____________|======+-----------+
    /_._/   (      |   /____________|       |   COLT    |
      /      `  _ ____/                     |  EXPRESS  |
     |_      .\( \\                         |___________|
    .'  `-._/__`_//
  .'       |-----/
 /        /
/        |
|        '
|         \
`-._____.-'""")
    print("")
    print("... dem spannenden Text Adventure!")
    print("")


def help():
    print("Verfügbare Kommandos:")
    print("  gehe [ RICHTUNG ]")
    print("  nimm [ GEGENSTAND ]")
    print("  benutze [ GEGENSTAND ]")
    print("  hilfe")
    print("  ende")


def status():
    print("Du befindest dich hier:", current_location)
    # If there is a description, show that to the player
    if "description" in locations[current_location]:
        print(locations[current_location]["description"])
    # If there are items at this location, tell the player about it
    if locations[current_location]["items"]:
        print("Hier liegt auch was rum:", locations[current_location]["items"])
    print("Du hast:", inventory)


welcome()


# Loop forever
while True:

    status()

    # Get the player's next command
    command = ''
    while command == '':
        command = input('> ')

    # Use .split() to break it up into an list, e.g. typing 'gehe vor'
    # would give the list: ['gehe','vor']
    command = command.lower().split()

    if command[0] == 'gehe':
        # Check if we can go there...
        if command[1] in locations[current_location]["exits"]:
            # Set the current location to the new location
            current_location = locations[current_location]["exits"][command[1]]
        # ... otherwise, there is exit in that direction.
        else:
            print('Da geht es nicht weiter!')

    if command[0] == 'nimm' :
        # If the location has that item...
        if command[1] in locations[current_location]['items']:
            # Add the item to their inventory
            inventory += [command[1]]
            # Print a helpful message
            print("Du hast jetzt:", command[1])
            # Remove the item from the location
            locations[current_location]["items"].remove(command[1])
        else:
            # Tell player, there is no such item
            print("Hier gibt es kein:", command[1])

    if command[0] == 'benutze':
        if current_location == "Wagen 3":
            if command[1] == "bandit":
                if "kleingeld" in inventory:
                    print("Du wirfst einige Münzen in den Automaten und versucht dein Glück.")
                    inventory.remove("kleingeld")
                    if random.randint(0,1) == 1:
                        print("Du hast Glück und gewinnst einen silbernen Dollar!")
                        inventory.append("silberdollar")
                    else:
                        print("Pech gehabt. Dein Geld ist futsch.")
                else:
                    print("Dafür fehlt dir wohl das nötige Kleingeld.")
        else:
            print("So etwas gibt es hier nicht!")

    if command[0] == 'hilfe':
        help()

    if command[0] == 'ende':
        print("Bis zum nächsten Mal!")
        break

    print("")
