import pickle as p
import json
from easygui import *

key = 1
code_entered = 0
seen_code = 1

def firststart():
    try:
        f = open("config.save","rb")
        config = p.load(f)

    except:
        msgbox("Dateiveränderung erkannt! \n")
        msgbox("Erzeuge neue Dateien... \n")
        f = open("config.save","wb")
        options = {'firststart': 'true'}
        p.dump(options, f)
        f.close()
        msgbox("Bitte starte das Spiel neu!")
        quit()


    else:
        global firststart
        firststart = config['firststart']
        start()



def savegame(location, comefrom):
    slot = inputbox("Welcher Speicherstand soll genutzt werden ? 1,2,3\n")
    f = open("saves/" + slot + ".save","wb")
    global name
    global key
    global code_entered
    save = {1: name,2: location,3: key,4: code_entered,5: seen_code,6: comefrom}
    p.dump(save, f)
    f.close()
    quit()

def loadgame():
    slot = inputbox("Welcher Speicherstand soll genutzt werden ? 1,2,3\n")
    location = "saves/" + slot + ".save"

    try:
        f = open(location,"rb")
    except IOError:
        msgbox("Dieser Speicherstand existiert nicht!")
        loadgame()


    else:
        try:

            save = p.load(f)
            global name
            name = save[1]
            global number
            number = save[2]
            global key
            key = save[3]
            global code_entered
            code_entered = save[4]
            global seen_code
            seen_code = save[5]

            f.close()
            msgbox("Wilkommen zurück, " + name + "\n")
            #print(location)

            loop(save[6], save[2])

        except p.UnpicklingError:

            msgbox("Der Speicherstand ist fehlerhaft!\n")


def inputbox(message):
    fieldValues = []
    input = multenterbox(message,"Lost in the Forest (c) by jms-diys", ["Auswahl"])[0]
    return input

def start():
    global firststart
    global name


    if firststart =='false':

        load = inputbox("Willst du einen Spielstand laden? 1/Ja 2/Nein\n")
        #load = load[0]
        if load == '1':
            loadgame()


        elif load == '2':
            name = inputbox("Wie ist dein Name?")

            msgbox("Hallo, " + name + '\n')
            msgbox("Wilkommen im Spiel Lost in the Forest. Du musst aus dem Wald entkommen. Viel Glück!\n")
            loop('start','wald')
            #loop('labyrinth3', 'door')

        else:
            msgbox("Eingabe nicht erkannt!")
            start()

    elif firststart == 'true':
        f = open("config.save","wb")
        options = {'firststart': 'false'}
        p.dump(options, f)
        f.close()
        name = inputbox("Wie ist dein Name?\n")
        msgbox("Hallo, " + name )
        msgbox("Wilkommen im Spiel Lost in the Forest. Du musst aus dem Wald entkommen. Viel Glück!\n")
        loop('start','wald')




def labyrinth_stop(comefrom, answer):

    global key
    key = 1


def labyrinth2_r(comefrom, answer):

    global seen_code
    seen_code = 1




class door:

    def __init__(self, comefrom, answer):
        self.comefrom = comefrom
        self.answer = answer

    def open(comefrom, answer):

        global key
        global code_entered
        print('test')

        if key == 1 & code_entered == 1:
            msgbox("Die Tür ist offen!")
            loop('door','end')
        elif key == 1:
            msgbox("GAME OVER!")
            firststart()

        else:
            msgbox("Du hast keinen Schlüssel im Inventar!")
            loop('labyrinth3','door')



    def enterkey(comefrom, answer):

        global code_entered
        code_entered = 1
        msgbox('Code erfolgreich eingegeben!')
        loop('labyrinth3','door')




def end(comefrom, position):
    quit()



def directions(comefrom, position):

    print('comefrom' + comefrom)
    print('pos'+position)
    mytuple = (position, comefrom)
    string = '_'.join(mytuple)
    print(string)
    string = str(string)
    try:
        string = string.replace(".", "_")

    except:
        print("")

    print(string)
    #comefrom = eval(comefrom)

    wald_start = {'1': 'labyrinth', '2': 'quit','5': 'savegame', '6': 'loadgame'}

    labyrinth_labyrinth_l = {'1': 'wald', '2': 'labyrinth_f', '3': comefrom,'4': 'labyrinth_r', '5': 'savegame', '6': 'loadgame'}
    labyrinth_labyrinth_r = {'1': 'labyrinth_f', '2': 'wald', '3': comefrom,'4': 'labyrinth_l', '5': 'savegame', '6': 'loadgame'}
    labyrinth_labyrinth_f = {'1': 'labyrinth_l', '2': 'labyrinth_r', '3': comefrom,'4': 'wald', '5': 'savegame', '6': 'loadgame'}
    labyrinth_wald = {'1': 'labyrinth_r', '2': 'labyrinth_l', '3': comefrom,'4': 'labyrinth_f', '5': 'savegame', '6': 'loadgame'}

    labyrinth_r_labyrinth2 = {'1': 'labyrinth', '3': comefrom, '5': 'savegame', '6': 'loadgame'}
    labyrinth_r_labyrinth = {'2': 'labyrinth2', '3': comefrom, '5': 'savegame', '6': 'loadgame'}

    labyrinth_l_labyrinth = {'1': 'labyrinth_trap', '2': 'labyrinth_trap', '3': comefrom,'5': 'savegame', '6': 'loadgame'}

    labyrinth_f_labyrinth_stop = {'1': 'labyrinth_trap', '2': 'labyrinth2', '3': comefrom,'4': 'labyrinth', '5': 'savegame', '6': 'loadgame'}
    labyrinth_f_labyrinth2 = {'1': 'labyrinth_stop', '2': 'labyrinth', '3': comefrom,'4': 'labyrinth_trap', '5': 'savegame', '6': 'loadgame'}
    labyrinth_f_labyrinth = {'1': 'labyrinth2', '2': 'labyrinth_trap', '3': comefrom,'4': 'labyrinth_stop', '5': 'savegame', '6': 'loadgame'}

    labyrinth_stop_labyrinth_f = {'3': comefrom,'5': 'savegame', '6': 'loadgame'}

    labyrinth_trap_labyrinth_l = {'6': 'loadgame', '7': 'firststart'}

    labyrinth2_labyrinth2_r = {'1': 'labyrinth2_f', '2': 'labyrinth_r', '3': comefrom,'4': 'labyrinth_f', '5': 'savegame', '6': 'loadgame'}
    labyrinth2_labyrinth2_f = {'1': 'labyrinth_f', '2': 'labyrinth2_r', '3': comefrom,'4': 'labyrinth_r', '5': 'savegame', '6': 'loadgame'}
    labyrinth2_labyrinth_f = {'1': 'labyrinth_r', '2': 'labyrinth2_f', '3': comefrom,'4': 'labyrinth2_r', '5': 'savegame', '6': 'loadgame'}
    labyrinth2_labyrinth_r = {'1': 'labyrinth2_r', '2': 'labyrinth_f', '3': comefrom,'4': 'labyrinth2_f', '5': 'savegame', '6': 'loadgame'}

    labyrinth2_r_labyrinth2 = {'1': 'labyrinth_trap', '2': 'labyrinth_trap', '3': comefrom,'5': 'savegame', '6': 'loadgame'}


    labyrinth2_f_labyrinth2_stop = {'1': 'labyrinth2', '2': 'labyrinth3', '3': comefrom, '5': 'savegame', '6': 'loadgame'}
    labyrinth2_f_labyrinth3 = {'1': 'labyrinth_stop', '3': comefrom,'4':' labyrinth2', '5': 'savegame', '6': 'loadgame'}
    labyrinth2_f_labyrinth2 = {'2': 'labyrinth_stop', '3': comefrom, '4':'labyrinth3', '5': 'savegame', '6': 'loadgame'}

    labyrinth3_door = {'1': 'labyrinth2_f', '2': 'labyrinth_trap', '3': comefrom,'4': 'labyrinth_trap', '5': 'savegame', '6': 'loadgame'}
    labyrinth3_labyrinth2_f = {'1': 'labyrinth_trap', '2':'door', '3': comefrom,'4': 'labyrinth_trap', '5': 'savegame', '6': 'loadgame'}
    labyrinth3_closed_labyrinth2_f = {'1': 'labyrinth_trap', '3': comefrom,'4': 'labyrinth_trap', '5': 'savegame', '6': 'loadgame'}

    door_labyrinth3 = {'1': 'door.open', '2': 'door.enterkey', '3': comefrom,'5': 'savegame', '6': 'loadgame'}

    door_enterkey_door = {'4598': 'door.bomb', '2': 'bomb', '3': comefrom,'5': 'savegame', '6': 'loadgame'}

    door_open_door = {'1': 'door.bomb', '2': 'bomb', '3': comefrom,'5': 'savegame', '6': 'loadgame'}

    end_door = {'3': 'end'}


    return locals()[string]


def rooms(room):
    global key
    global seen_code
    global code_entered
    goto = str(room)
    loc = {



    'wald': {
    'message': 'Willst du in den Wald gehen? 1/Ja 2/Nein \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'

    },

    'labyrinth':{
    'message': 'Du landest in einem Labyrinth!\n Willst du nach 1/rechts, 2/links, 3/zurück oder 4/vorwärts gehen? 5/Speichern 6/Laden \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'
    },

    'labyrinth_r':{
    'message': 'Du landest bei einer Kreuzung mit vielen Fußabdrücken! \n Willst du nach 2/links oder 4/zurück gehen? 5/Speichern 6/Laden \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'
    },

    'labyrinth_l':{
    'message': 'Du landest an einer Kreuzung mit einem Wegweiser, der in die Richtung vorwärts zeigt!\n Willst du nach 1/rechts, 2/links oder 3/zurück gehen? 5/Speichern 6/Laden \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'
    },

    'labyrinth_f':{
    'message': 'Du landest an einer Kreuzung mit Wandmalerei! \nWillst du nach 1/rechts, 2/links, 3/rückwärts, oder 4/vorwärts gehen? 5/Speichern 6/Laden \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'
    },

    'labyrinth_stop':{
    'message': 'Du landest in einer Sackgasse und findest einen mysteriösen Schlüssel!\nWillst du 3/rückwärts gehen? 5/Speichern 6/Laden \n',
    'req': 'true',
    'req_special': 'false',
    'input':'true'
    },

    'labyrinth_trap':{
    'message': '#########\nDu bist in einer Falle gelandet! 6/Laden 7/Neustart \n#########\n',
    'req': 'false',
    'req_special': 'true',
    'input':'true'
    },

    'labyrinth2':{
    'message': 'Du landest auf einer weiteren Kreuzung!\nWillst du nach 1/rechts, 2/links, 3/rückwärts, oder 4/vorwärts gehen? 5/Speichern 6/Laden \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'
    },

    'labyrinth2_r':{
    'message': 'Auf dem Boden stehen Zahlen: 4598!\n Willst du nach 2/links, 3/rückwärts oder 4/vorwärts gehen? 5/Speichern 6/Laden \n',
    'req': 'true',
    'req_special': 'false',
    'input':'true'
    },

    'labyrinth2_f':{
    'message': 'Du landest an einer anderen Kreuzung!\nWillst du nach 2/links, 3/rückwärts, oder 4/vorwärts gehen? 5/Speichern 6/Laden \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'
    },

    'labyrinth2_stop':{
    'message': 'Du landest in einer Sackgasse! \n Willst du nach 3/zurück gehen? 5/Speichern 6/Laden \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'
    },

    'labyrinth3':{
    'message': 'Du landest an einer großen Kreuzung, die Tür ist verschwunden! Willst du nach 1/rechts, 2/links, 3/rückwärts, oder 4/vorwärts gehen? 5/Speichern 6/Laden \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'
    },

    'labyrinth3_closed':{
    'message': 'Du landest an einer großen Kreuzung, es sieht so aus als ob links neben dir eine geschlossene Tür ist!Willst du nach 1/rechts, 3/rückwärts oder 4/vorwärts gehen? 5/Speichern 6/Laden \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'
    },

    'door':{
    'message': '"Du siehst eine Tür, welche einen Schlüssel benötigt, aber es ist auch eine Zeitbombe versteckt.\n 1/Die Tür trotzdem aufschließen 2/Die Zeitbombe entschärfen 3/zurückgehen? 5/Speichern 6/Laden \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'
    },

    'door_code_entered':{
    'message': '"Du siehst eine Tür, welche einen Schlüssel benötigt.\n 1/Die Tür aufschließen oder 3/zurückgehen? 5/Speichern 6/Laden \n',
    'req': 'false',
    'req_special': 'false',
    'input':'true'
    },

    'door.enterkey':{
    'message': '#### Bitte Code eingeben! #### 3/Abbrechen ',
    'req': 'true',
    'req_special': 'false',
    'input':'true'
    },

    'door.open':{
    'message': '',
    'req': 'true',
    'req_special': 'false',
    'input':'false'
    },

    'end':{
    'message': 'Du hast es geschafft! Herzlichen Glükwunsch! \n Willst du das Spiel 3/beenden?\n',
    'req': 'true',
    'req_special': 'false',
    'input':'true'
    },

           }
    print(goto)

    if goto == 'labyrinth3':
        if seen_code == 1:
            return loc['labyrinth3']['message'], loc[goto]['req'], loc[goto]['req_special'], loc[goto]['input']
        else:
            return loc['labyrinth3_closed']['message'], loc[goto]['req'], loc[goto]['req_special'], loc[goto]['input']
    elif goto == 'door':
        if code_entered == 1:
            return loc['door_code_entered']['message'], loc[goto]['req'], loc[goto]['req_special'], loc[goto]['input']
        else:
            return loc['door']['message'], loc[goto]['req'], loc[goto]['req_special'], loc[goto]['input']

    else:

        return loc[goto]['message'], loc[goto]['req'], loc[goto]['req_special'], loc[goto]['input']




def loop(comefrom, position):



    while True:

        room_data = rooms(position)
        input_text = room_data[0]
        goto_function = room_data[1]
        goto_function_special = room_data[2]
        #if input_text == 'savegame':
            #savegame(position, comefrom)
        if room_data[3] == 'true':
            #choices = ["1", "2","3","4","5","6"]
            #msg = input_text
            #title = "Ice Cream Survey"
            #answer = choicebox(msg, title, choices)

            msg = input_text
            title = "Lost in the Forest (c) by jms-diys"
            fieldNames = ["Auswahl"]
            fieldValues = []  # we start with blanks for the values
            answer = multenterbox(msg,title, fieldNames)
            answer = answer[0]


            #answer = input(input_text)
            answers = directions(comefrom, position)
            #answers = room_data[2]
            #answers = {'3': eval(comefrom),'4': labyrinth, '5': savegame, '6': loadgame}
            print(answers)
            print(answer)


        if goto_function == 'true':
            try:
                func = eval(position)
                func(comefrom, answers[answer])

            except:
                print('')

        elif goto_function_special == 'true':
            eval(answers[answer])()



        if answer in answers:
            if answers[answer] == 'savegame':

                savegame(position, comefrom)


            if goto_function_special == 'false':

                #answers[answer]()
                print('test')
                comefrom = position
                position = answers[answer]#.__name__
                #print(position)

        else:
            msgbox("Eingabe nicht erkannt!\n")





firststart()
