#!/usr/bin/env python3

import random

def rollGame(player, opponent, cheat_code):

    def roll_4d6():
        wuerfel_1 = random.randint(1,6)
        wuerfel_2 = random.randint(1,6)
        wuerfel_3 = random.randint(1,6)
        wuerfel_4 = random.randint(1,6)
        result = wuerfel_1 + wuerfel_2 + wuerfel_3 + wuerfel_4
        return result

    # direkt gewonnen
    if player == cheat_code:
        print(opponent, "wird kreidebleich. Er rennt davon!")
        print("Du hast gewonnen!")
        return "win"

    else:
        print("Alles klar,", player, ", du spielst gegen", opponent,". Es geht um nicht weniger als dein Leben!\n")
        startplayer = random.choice([opponent, player])

        print(startplayer, "fängt in dieser Runde an.\n")
        print(startplayer, "würfelt mit vier Würfeln.\n")
        start_roll = roll_4d6()
        roll = roll_4d6()
        print("Ergebnis ist:", start_roll)

        if startplayer == player:
            # Der Spieler ist dran...
            answers = ['h','t']
            choice = ""
            while choice not in answers:

                choice = input("Hoch oder tief? h,t\n")
            print(opponent,"ist an der Reihe!\n")
            print("Ergebnis ist:", roll,"\n")
            if (start_roll > roll and choice == "h") or (start_roll < roll and choice == "t"):
                print("GEWONNEN! Puh, dein Leben ist gerettet und du erhälst genau nichts.\n")
                return "win"
            else:
                print("Oh no! Du hast verloren.")
                return "lose"

        else:
            # Der Gegner ist dran...
            if start_roll < 12:
                choice = ["t"]
            if start_roll >= 12:
                choice = ["h"]
            print(opponent, "tippt", choice, "!")
            print(player,"ist an der Reihe!\n")
            print("Ergebnis ist:", roll,"\n")

            answers = ['1','2','3']
            leave = ""
            while leave not in answers:
                leave = input("Willst du 1/weiterspielen 2/weg rennen 3/zum Fenster rausspringen\n")

            if leave == "1":
                if (start_roll > roll and choice == "h") or (start_roll < roll and choice == "t"):
                    print("Oh no! Du hast verloren.")
                    return "lose"
                else:
                    print("GEWONNEN! Puh, dein Leben ist geretet und du erhälst genau nichts.\n")
                    return "win"

            elif leave == "2":
                print('Du landest in der Zugtoilette\n')
                return "run"

            elif leave == "3":
                print('Du landest in einer trockenen Wüste und der Zug fährt davon!\n')
                return "jump"


if __name__ == "__main__":

    character_list = ["Joe","Jack","William","Averell"]
    name = input("Wie heisst du?\n")
    print("Grüß dich,", name,"\n")

    random_character = random.randint(0,3)
    character = character_list[random_character]

    rollGame(name, character, "Lucky Luke")
