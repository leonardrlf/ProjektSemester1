########################################## Galgenmännchen ##########################
########## Autoren: Leonard Rolf, Levin Köppe, Younes Bareche, Noah Klug, Simon Kieslich####
###### Erstellt vom 05.03.2024 bis 21.03.2024 ###############

import random


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

            #display hangman on easy mode after 2 wrong inputs 
            trys = 6 - versuche
            if trys <= 0:
                trys = 0



            galgenmann(trys)                                                            #display of hangman
            guess = input("Rate einen Buchstaben oder gib das gesamte Wort ein: ").lower()      #input of guess

            
            #only one letter, is it really a letter and in word?
            if len(guess) == 1 and guess.isalpha():
                if guess in bisherige_Buchstaben:
                    print("Du hast diesen Buchstaben bereits geraten. Versuche es erneut.")
                    continue

                bisherige_Buchstaben.append(guess)  #put new letter in array

                #letter not in word, remove one attmept
                if guess not in Wort:
                    versuche -= 1
                    print(f"Falsch! Du hast noch {versuche} Versuche übrig.")
            
            #guess same leght as word and consists of characters 
            elif len(guess) == len(Wort) and guess.isalpha():
                if guess == Wort:                                                           #right guess 
                    print(f"Herzlichen Glückwunsch! Du hast das Wort '{Wort}' erraten.")
                    break
                else:
                    versuche -= 1
                    print(f"Falsch! Du hast noch {versuche} Versuche übrig.")
            
            #guess longer than one character but not the searched word 
            elif len(guess) != len(Wort) and guess.isalpha():
                versuche -= 1
                print(f"Falsches Wort! Du hast noch {versuche} Versuche übrig.")
            
            #every other input 
            else:
                print("Ungültige Eingabe. Bitte entweder einen Buchstaben raten oder das gesamte Wort eingeben.")
                continue

            #review if word is fully guessed 
            if "_" not in wort_Darstellung(Wort, bisherige_Buchstaben):
                print(f"Herzlichen Glückwunsch! Du hast das Wort '{Wort}' erraten.")
                break

        #losing condition 
        if versuche == 0:
            trys += 1
            print(f"Leider verloren! Das richtige Wort war '{Wort}'.")
            galgenmann(trys)    #display hangman
            
        #play angain or ending 
        play_again = input("Möchtest du noch einmal spielen? (ja/nein): ").lower()
        if play_again != 'ja':
            game = False



#####       THE GAME        #####

galgenmännchen()