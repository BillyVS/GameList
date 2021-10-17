import time
from datetime import date, datetime


class game:
    def __init__(self, title, release_year, developers, notes, date_added): 
        self.title = title 
        self.release_year = release_year
        self.developers = developers 
        self.notes = notes
        self.date_added = date_added


def addGame():
    title = input("What is the title of the game>\n")
    release_year = input("What year did the game come out?\n")
    developers = input("Who made the game?\n")
    notes = []
    today = date.today()
    Date = today.strftime("%d/%m/%Y")
    complete = 0
    
    
    while complete == 0:
        note = input("What did you like about the game?\n")
        if note == "x" or note == "X":
            complete = 1
        else:
            notes.append(note)

    game_dictionary[title] = game(title,release_year,developers,notes,Date)


def displayMenu():
    time.sleep(0.01)
    print("MENU".rjust(22," "))
    time.sleep(0.01)
    print("\n")
    print("1"+("ADD A GAME").rjust(40,"-"))
    time.sleep(0.01)
    print("2"+("REMOVE A GAME").rjust(40,"-"))
    time.sleep(0.01)
    print("3"+("VIEW YOUR LIST").rjust(40,"-"))
    time.sleep(0.01)
    print("3"+("Exit").rjust(40,"-"))
    time.sleep(0.01)
    valid_input = False
    while valid_input == False:
        choice = input()
        if choice == "1":
            valid_input = True
            print("\n")
            addGame()

            displayMenu()
        elif choice == "2":
            valid_input = True
            print("\n")
            print(game_dictionary["Portal"].release_year)
            
            displayMenu()

game_dictionary = {}
displayMenu()