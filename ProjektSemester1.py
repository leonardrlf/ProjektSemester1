########################################## Galgenmännchen ##########################
########## Autoren: Leonard Rolf, Levin Köppe, Younes Bareche, Noah Klug, Simon Kieslich####
###### Erstellt vom 05.03.2024 bis 21.03.2024 ###############

<<<<<<< HEAD
import
 random


def random_Wort():






def wort_Darstellung(wort, erratene_Buchstaben):






def galgenmann(versuche):






def versuche_bis_verloren():




# Game flow

def galgenmännchen():
 game = True
 while game == True:
        Wort = random_Wort()    #chose word 
        bisherige_Buchstaben = []       #create array for already used letters 
        versuche = versuche_bis_verloren()      #recognize level of difficulty 

        print("Willkommen bei Galgenmännchen!")

        while versuche > 0:
            mischung_wort_strich = wort_Darstellung(Wort, bisherige_Buchstaben)  #display of word
            print(f"Aktueller Stand: {mischung_wort_strich}")
            galgenmann(6 - versuche)                                                            #display of hangman
            guess = input("Rate einen Buchstaben oder gib das gesamte Wort ein: ").lower()      #input of guess

