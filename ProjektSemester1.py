##################################### Galgenmännchen #####################################
##### Autoren: Leonard Rolf, Levin Köppe, Younes Bareche, Noah Klug, Simon Kieslich #####
######################### Erstellt vom 05.03.2024 bis 21.03.2024 #########################

# import modul random
import random   # import modul "random", so we have acces to random generator

# defining function random_word
def random_word():  # function, which brings back a random word from our collection
    words = ["karlsruhe","darmstadt","bremerhafen","hamburg","berlin","köln","kiel","nuernberg","chemnitz","cottbus","saarbruecken","trier","neubrandenburg"] # our word collection: citys of Germany
    return random.choice(words)  # end of function, return to main with random word

# defining function visualising_word
def visualising_word(word, guessed_letters):
 display = ""                                    ## creating a variable for displaiing the guessed letters
 for letter in word:                          ## if letter guessed store in display
    if letter in guessed_letters:
        display += letter
    else:                                        ## for every letter which isn't guessed write "_"
        display += "_"

 return display


# defining function visualising_hangman
def visualising_hangman(tries_tries):  # function, which visualizes the amount of trys by creating the hangman step by step
    rounds = [            # variable depends on trys left: variable n shows hangman graphic no. n
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
    print(rounds[tries_tries])  # the hangman is printed, depending on the amount of trys

# defining function tries_until_failure
def tries_until_failure():   # function, which returns tries until failure depending on level of difficulty
   difficulty = input("Wähle einen Schwierigkeitsgrad (leicht(1), mittel(2), schwer(3)): ").lower() # user should choose the level of difficulty
   if difficulty == "1":    # is it level "1"?
       return 8                # if it is, gives back "8" as tries until failure
   elif difficulty == "2":  # is it level "2"?
       return 6                # if it is, gives back "6" as tries until failure
   elif difficulty == "3":  # is it level "3"?
       return 4                # if it is, gives back "4" as tries until failure
   else:                       # did the user write something else instead of 1, 2 or 3?
       print("Ungültiger Schwierigkeitsgrad. Dieser wird standardmäßig auf mittel eingestellt.")   # it is printet, that the user wrote something wrong and now its set to level 2 
       return 6                # gives back "6" as tries until failure

# Game flow
# defining function hangman
def hangman():
 game = True
 while game == True:
        word_to_guess = random_word()                                                     # chose word 
        already_guessed_letters = []                                                # create array for already used letters 
        tries_left = tries_until_failure()                                       # recognize level of difficulty 

        print("Willkommen bei Galgenmännchen!")

        while tries_left > 0:
            letters_and_lines = visualising_word(word_to_guess, already_guessed_letters)  # display of word
            print(f"Aktueller Stand: {letters_and_lines}")

            # display hangman on easy mode after 2 wrong inputs 
            tries = 6 - tries_left
            if tries <= 0:
                tries = 0



            visualising_hangman(tries)  # display of hangman
            guess = input("Rate einen Buchstaben oder gib das gesamte Wort ein: ").lower()  #input of guess

            
            # only one letter, is it really a letter and in word?
            if len(guess) == 1 and guess.isalpha():
                if guess in already_guessed_letters:
                    print("Du hast diesen Buchstaben bereits geraten. Versuche es erneut.")
                    continue

                already_guessed_letters.append(guess)  # put new letter in array

                # letter not in word, remove one attmept
                if guess not in word_to_guess:
                    tries_left -= 1
                    print(f"Falsch! Du hast noch {tries_left} Versuche übrig.")
            
            # guess same leght as word and consists of characters 
            elif len(guess) == len(word_to_guess) and guess.isalpha():
                if guess == word_to_guess:  # right guess 
                    print(f"Herzlichen Glückwunsch! Du hast das Wort '{word_to_guess}' erraten.")
                    break
                else:
                    tries_left -= 1
                    print(f"Falsch! Du hast noch {tries_left} Versuche übrig.")
            
            #guess longer than one character but not the searched word 
            elif len(guess) != len(word_to_guess) and guess.isalpha():
                tries_left -= 1
                print(f"Falsches Wort! Du hast noch {tries_left} Versuche übrig.")
            
            #every other input 
            else:
                print("Ungültige Eingabe. Bitte entweder einen Buchstaben raten oder das gesamte Wort eingeben.")
                continue

            #review if word is fully guessed 
            if "_" not in visualising_word(word_to_guess, already_guessed_letters):
                print(f"Herzlichen Glückwunsch! Du hast das Wort '{word_to_guess}' erraten.")
                break

        #losing condition 
        if tries_left == 0:
            tries += 1
            print(f"Leider verloren! Das richtige Wort war '{word_to_guess}'.")
            visualising_hangman(tries)  #display hangman
            
        #play angain or ending 
        play_again = input("Möchtest du noch einmal spielen? (ja/nein): ").lower()
        if play_again != 'ja':
            game = False

#####       THE GAME        #####
## "main" function of program: invocation of the "galgenmännchen" function
hangman()
