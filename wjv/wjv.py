#!/usr/bin/env python3
import random
import csv

ATHLETES_FILE_PATH = "wjv-input.csv"

class Athlete():

    def __init__(self, firstname, lastname, club, prio=0):
        self.firstname = firstname
        self.lastname = lastname
        self.club = club
        self.prio = prio

    def __repr__(self):
        return self.firstname + " " + self.lastname \
            + " (" + self.club + ", " + str(self.prio) + ")"


def load_athletes_from_file(athlethesFilePath):
    athletes = []
    with open(athlethesFilePath) as athlethesFile:
        athlethesCSVObj = csv.reader(athlethesFile) # read the file; if there's an error FileNotFoundError is raised
        for athleteRow in athlethesCSVObj:
            # todo: prio management; checking if csv file is valid, better handling rows: maybe loop through colums?
            athlete = Athlete(athleteRow[0],athleteRow[1],athleteRow[2])
            athletes.append(athlete)
    return athletes


def get_clubs_form_athlete_list(athletes): # get all the clubs of athlethes list
    clubs = []
    for player in athletes: # loop through all athletes
        club = player.club # get the club of this player
        if club not in clubs: # add the club if it isn't already in the list
            clubs.append(club)
    return clubs


def print_athlete_list(athletes):
    for number, athlete in enumerate(athletes):
        print("{}: {}".format(number, athlete))


if __name__ == "__main__":

    # Load from file
    athletes = load_athletes_from_file(ATHLETES_FILE_PATH)

    print("\nListe am Anfang:")
    print_athlete_list(athletes)
    sortedByClubsList = []
    clubs = get_clubs_form_athlete_list(athletes)
    random.shuffle(clubs) #randomize the clubs

    # Sort by clubs
    for clubname in clubs:
        clublist = [ a for a in athletes if a.club == clubname ]
        sortedByClubsList = sortedByClubsList + clublist

    print("\nListe nach Vereinen sortiert:")
    print_athlete_list(sortedByClubsList)

    # Sort by list
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
