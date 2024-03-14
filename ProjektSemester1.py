########################################## Galgenmännchen ##########################
########## Autoren: Leonard Rolf, Levin Köppe, Younes Bareche, Noah Klug, Simon Kieslich####
###### Erstellt vom 05.03.2024 bis 21.03.2024 ###############

bereit =True
input
test

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
