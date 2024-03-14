########################################## Galgenmännchen ##########################
########## Autoren: Leonard Rolf, Levin Köppe, Younes Bareche, Noah Klug, Simon Kieslich####
###### Erstellt vom 05.03.2024 bis 21.03.2024 ###############

# import modul random
import random   # import modul "random", so we have acces to random generator

# defining function random_Wort
def random_Wort():  # function, which brings back a random word from our collection
    woerter = ["karlsruhe","darmstadt","bremerhafen","hamburg","berlin","köln","kiel","nuernberg","chemnitz","cottbus","saarbruecken","trier","neubrandenburg"] # our word collection: citys of Germany
    return random.choice(woerter) # end of function, return to main with random word

def wort_Darstellung(wort,erratene_Buchstaben):
 display = ""                                    ##creating a variable for displaiing the guessed letters
 for buchstabe in wort:                          ## if letter guessed store in display
    if buchstabe in erratene_buchstabe:
        display += buchstabe
    else:                                           ## for every letter which isn't guessed write "_"
        display += "_"

 return display


# defining function galgenmann
def galgenmann(versuche): # function, which visualizes the amount of trys by creating the hangman step by step
    ettapen = [           # variable depends on trys left: variable n shows hangman graphic no. n
                          # figure 1 to 7
        """
        +---+
        |   |
            |
            |
            |
            |
        =========
        """,
       
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
       
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
       
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
       
        """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        """,
       
        """
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        """,
       
        """
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        """
        ]
    print(ettapen[versuche]) # the hangman is printed, depending on the amount of trys

def versuche_bis_verloren():  # Funktion "versuche_bis_verloren" definiert, um die Anzahl der Versuche basierend auf dem Schwierigkeitsgrad zurückzugeben
   schwierigkeit = input("Wähle einen Schwierigkeitsgrad (leicht(1), mittel(2), schwer(3)): ").lower() # Benutzer wird aufgefordert, einen Schwierigkeitsgrad zu wählen
   if schwierigkeit == "1": # Überprüfung, ob der Schwierigkeitsgrad "1" ist
       return 8  # Wenn der Schwierigkeitsgrad "1" ist, wird die Anzahl der Versuche auf 8 festgelegt und zurückgegeben
   elif schwierigkeit == "2": # Überprüfung, ob der Schwierigkeitsgrad "1" ist
       return 6 # Wenn der Schwierigkeitsgrad "2" ist, wird die Anzahl der Versuche auf 6 festgelegt und zurückgegeben
   elif schwierigkeit == "3": # Überprüfung, ob der Schwierigkeitsgrad "3" ist
       return 4 # Wenn der Schwierigkeitsgrad "3" ist, wird die Anzahl der Versuche auf 4 festgelegt und zurückgegeben
   else: # Wenn der eingegebene Schwierigkeitsgrad weder "1", "2" noch "3" ist
       print("Ungültiger Schwierigkeitsgrad. Dieser wird standardmäßig auf mittel eingestellt.")   # Es wird ausgegeben, dass der eingegebene Schwierigkeitsgrad ungültig ist und standardmäßig auf "mittel" eingestellt wird
       return 6  # Die Anzahl der Versuche wird auf 6 (mittel) festgelegt und zurückgegeben

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
