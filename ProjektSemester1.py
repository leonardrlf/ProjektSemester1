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

def versuche_bis_verloren():


def galgenmännchen():