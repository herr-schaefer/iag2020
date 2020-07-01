#!/usr/bin/env python3
#
# Authors: Peter Schäfer, Felix Schulthess
#
# - 2020-06-02: Add code to cryptpad
# - 2020-06-03: Add code for gambling with your money
# - 2020-06-04: Add description and location ++ some possibilities to interact with
#

import random

inventory = ["Colt", "Geisterstein", "Kleingeld"]
current_location = "Wagen 3"


locations = {
    "Lokomotive": {
        "description": "Ja heiliges Blechle! Eine Pennsylvania D6 treibt diesen Zug an. Ein gewaltiges Dampfross aus dem Jahr 1882. Beeindruckend, das muss man schon sagen. Eine Sache fehlt allerdings, der Lokomotivführer! Wo kann der sein?",
        "items": [
            "Kohlebriketts",
            "Schaufel"
        ],
        "exits": {
            "zurück": "Wagen 1",
            "hoch": "Dach Lokomotive"
        }
    },
    "Wagen 1": {
        "description": "In diesem Wagen riecht es nach Zigarrenrauch. Im schummrigem Licht sitzen drei lumpige Gestalten an einem Spieltisch. An der Wand hinter dem Croupier hängt ein Portrait von George Washington. Der Wagon besitzt ausnahmsweise drei Türen. Eine führt in die Zugtoilette.",
        "items": [
            "Geldkassette"
        ],
        "exits": {
            "vor": "Lokomotive",
            "zurück": "Wagen 2",
            "hoch": "Dach Wagen 1",
            "toilette": "Zugtoilette"
        }
    },
    "Wagen 2": {
        "description": "Bei diesem Wagen handelt es sich um einen alten Postwagen. Dieser Wagen ist vollgestopft mit großen Paketen. Der Beschriftung nach zu urteilen sind die meisten davon von Tante Marta, die ihre Schmiede von Colorado nach Wyoming umzieht.",
        "items": [
            "Seil",
            "Packpapier"
        ],
        "exits": {
            "vor": "Wagen 1",
            "zurück": "Wagen 3",
            "hoch": "Dach Wagen 2"
        }
    },
    "Wagen 3": {
        "description": "Der Wagen hier ist ein alter, verratzter Speisewagen. Es sind keine anderen Passagiere da. In der Ecke steht ein einarmiger Bandit. Draußen vor dem Fenster brennt die Sonne nieder auf die Prärie.",
        "items": [
        ],
        "exits": {
            "vor": "Wagen 2",
            "hoch": "Dach Wagen 3"
        }
    },
    "Dach Lokomotive": {
        "description": "Der heiße und rußhaltige Rauch der Lokomotive macht das Dach zu einem ungemütlichen Ort. Allerdings lässt sich hier der Stoff, aus dem Diamanten sind, auflesen. Und um Diamanten geht es hier ja schließlich.",
        "items": [
            "Ruß"
        ],
        "exits": {
            "zurück": "Dach Wagen 1",
            "runter": "Lokomotive"
        }
    },
    "Dach Wagen 1": {
        "description": "Du betritst das Blechdach von Wagen 1. In der vorderen, linken Ecke befindet sich der Abluftschacht der Zugtoilette.",
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
        "description": "Das Holzdach knarzt verdächtig unter deinen Füßen. Alles was man sich hier holen kann sind Spreißel. Aber zum Glück trägst du ja Cowboystiefel aus veganem Kunstleder.",
        "items": [
        ],
        "exits": {
            "vor": "Dach Wagen 1",
            "zurück": "Dach Wagen 3",
            "runter": "Wagen 2"
        }
    },
    "Dach Wagen 3": {
        "description": "Ein rostiges Blechdach schmückt den letzen Wagen. In der Mitte ist das Blech blauschwarz gefärbt.",
        "items": [
        ],
        "exits": {
            "vor": "Dach Wagen 2",
            "runter": "Wagen 3"
        }
    },
    "Zugtoilette": {
        "description": "Wie zu erwarten riecht es hier wie auf dem Schulklo! Hast du etwas anderes erwartet? An einer Wand hängt ein Portrait von dir mit der Überschwift: 'WANTED DEAD OR ALIVE'. Offensichtlich ein Fahndungsplakat.",
        "items": [
            "Klobürste",
            "Plakat",
        ],
        "exits": {
            "raus": "Wagen 1",
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
    # Print the avialable exits
    print("Hier geht es weiter:")
    for direction, location in locations[current_location]["exits"].items():
        print("  ", location, "({})".format(direction))
    # Print inventory
    print("Du hast:")
    for item in inventory:
        print("  ", item)


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
        # ... otherwise, there is exit no in that direction.
        else:
            print('Da geht es nicht weiter!')

    if command[0] == 'nimm' :
        item = command[1].capitalize()
        # If the location has that item...
        if item in locations[current_location]['items']:
            # Add the item to their inventory
            inventory += [item]
            # Print a helpful message
            print("Du hast jetzt:", item)
            # Remove the item from the location
            locations[current_location]["items"].remove(item)
        else:
            # Tell player, there is no such item
            print("Hier gibt es kein:", command[1])

    if command[0] == "betrachte":
        print("Das geht (noch) nicht.")

    if command[0] == 'benutze':
        if current_location == "Wagen 3":
            if command[1] == "bandit":
                if "Kleingeld" in inventory:
                    print("Du wirfst einige Münzen in den Automaten und versucht dein Glück.")
                    inventory.remove("Kleingeld")
                    if random.randint(0,1) == 1:
                        print("Du hast Glück und gewinnst einen silbernen Dollar!")
                        inventory.append("Silberdollar")
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
