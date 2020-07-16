#!/usr/bin/env python3
import random

class Athlete():

    def __init__(self, firstname, lastname, club, prio=0):
        self.firstname = firstname
        self.lastname = lastname
        self.club = club
        self.prio = prio

    def __repr__(self):
        return self.firstname + " " + self.lastname \
            + " (" + self.club + ", " + str(self.prio) + ")"


clubs = [
    "Stadtwache",
    "Hexen",
    "Kobolde",
    "Assassinen"
    ]


athletes = [
    Athlete("Zlorf", "Flanellfuß", "Assassinen"),
    Athlete("Samuel", "Mumm", "Stadtwache"),
    Athlete("Karotte", "Eisengießersohn", "Stadtwache"),
    Athlete("Kelda", "Aggie", "Kobolde"),
    Athlete("Esmeralda", "Wetterwachs", "Hexen"),
    Athlete("Delphine Angua", "von Überwald", "Stadtwache"),
    Athlete("Rob", "Irgendwer", "Kobolde"),
    Athlete("Sally", "Humpeding", "Stadtwache", 1),
    Athlete("Gytha", "Ogg", "Hexen"),
    Athlete("Mustrum", "Ridcully", "Hexen"),
    Athlete("Robert", "Selachii", "Assassinen"),
    Athlete("Großer", "Yan", "Kobolde"),
    Athlete("Billy", "Breitkinn", "Kobolde"),
    Athlete("Mittelgroßer", "Jock", "Kobolde"),
    Athlete("Leckerschmeck", "Nivor", "Assassinen"),
    Athlete("Kompt", "de Yoyo", "Assassinen")
    ]


def print_athlete_list(athletes):
    for number, athlete in enumerate(athletes):
        print("{}: {}".format(number, athlete))


if __name__ == "__main__":

    print("\nListe am Anfang:")
    print_athlete_list(athletes)
    sortedByClubsList = []
    random.shuffle(clubs)

    for clubname in clubs:
        clublist = [ a for a in athletes if a.club == clubname ]
        sortedByClubsList = sortedByClubsList + clublist

    print("\nListe nach Vereinen sortiert:")
    print_athlete_list(sortedByClubsList)
    sortedList = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
    sortedAthletes = []

    print("\nAthleten in 16er-Liste sortiert:")
    for i in sortedList:
        sortedAthletes.append(sortedByClubsList[i])
    print_athlete_list(sortedAthletes)

#0: Zlorf Flanellfuß (Assassinen, 0)
#1: Mittelgroßer Jock (Kobolde, 0)
#2: Kelda Aggie (Kobolde, 0)
#3: Samuel Mumm (Stadtwache, 0)

#    1. ____
#            \  _____
#    2. ____ /        \
#                      \ _______
#    3. ____           /        \
#            \  _____ /          \
#    4. ____ /                    \
#                                  \ _______
#    6. ____                       /
#            \  _____             /
#    7. ____ /        \          /
#                      \ _______/
#    8. ____           /
#            \  _____ /
#    9. ____ /





# Todoliste:
# 1. Freilose einbauen
# 2. Vereine sollen ihren Athleten Prioritäten geben. Aber wie werden die behandelt
# 3. Am Ende muss etwas Druckbares dabei rauskommen (evtl. Ascii-Art für den Anfang)
# 4. Soll man den Ablauf skripten (also eingeben, wer welchen Kampf gewonnen hat)?
# $. Es sollten auch 4er, 8er und 32er Listen unterstützt werden
