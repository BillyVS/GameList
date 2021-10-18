import time
from datetime import date, datetime

file = open("GAMELIST.txt","r")
lines = file.readlines()


class game:
    def __init__(self, title, release_year, developers, notes, date_added): 
        self.title = title 
        self.release_year = release_year
        self.developers = developers 
        self.notes = notes
        self.date_added = date_added


def getList(list_name):
    print(lines)
    n= 0
    checked = 0
    the_list = []
    print(list_name)
    while checked == 0:
        if lines[n].find(list_name) != -1:
            checked = 1
        else:
            n += 1
    print(n)
    item = lines[n+1].rstrip("\n")
    the_list.append(item)
    return the_list


def addGame():
    title = input("What is the title of the game>\n")
    release_year = input("What year did the game come out?\n")
    developers = input("Who made the game?\n")
    notes = []
    today = date.today()
    date_added = today.strftime("%d/%m/%Y")
    complete = 0
    
    
    while complete == 0:
        note = input("What did you like about the game?\n")
        if note == "x" or note == "X":
            complete = 1
        else:
            notes.append(note)

    game_dictionary[title] = game(title,release_year,developers,notes,date_added)


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
        elif choice == "3":
            valid_input = True


def editTextFile():
    keys_list = list(game_dictionary)
    output_lines = []
    output_lines.append("    GAMES LIST:")
    for key in keys_list:
        output_lines.append(game_dictionary[key].title)
    for i in range (0,2):
        output_lines.append("\n")
    output_lines.append("    RANKED LIST:")
    for game in ranked_list:
        output_lines.append("TEST")
    for i in range (0,2):
        output_lines.append("\n")
    output_lines.append("    RELEASE YEARS:")
    for key in keys_list:
        output_lines.append(game_dictionary[key].release_year)
    for i in range (0,2):
        output_lines.append("\n")
    output_lines.append("    DEVELOPERS:")
    for key in keys_list:
        output_lines.append(game_dictionary[key].developers)
    for i in range (0,2):
        output_lines.append("\n")
    output_lines.append("    NOTES:")
    for key in keys_list:
        output_lines.append(game_dictionary[key].notes)
    for i in range (0,2):
        output_lines.append("\n")
    output_lines.append("    DATES ADDED:")
    for key in keys_list:
        output_lines.append(game_dictionary[key].date_added)
    for i in range (0,2):
        output_lines.append("\n")


    file_to_write = open("GAMELIST.txt","w")
    for line in output_lines:
        file_to_write.write(str(line))
        file_to_write.write("\n")
    file_to_write.close()


def FilmRankedInsertion(game,ranked_games):
    position_found = False
    ranked_games = list(ranked_games)
    games_left = len(ranked_games)
    game_reference = "PlaceHolder"
    rating_reference = 0
    games_asked = []
    while position_found == False:
        if games_left > 0:
            if ranked_games[int(games_left/2)] not in games_asked:
                       
                if game_reference != ranked_games[int(games_left/2)]:
                    if games_left % 2 == 0:
                        print("Is",game,"better than: ",ranked_games[int(games_left/2)])
                        game_reference = ranked_games[int(games_left/2)]
                    else:
                        print("Is",game,"better than: ",ranked_games[int((games_left/2)-0.5)])
                        game_reference = ranked_games[int(games_left/2)]
                    print("Y or N")
                    ValidInput = False
                    while ValidInput == False:
                        Choice = input()
                        if Choice == "y" or Choice == "Y" or Choice == "n" or Choice == "N":
                            ValidInput = True
                        else:
                            print("Y or N")
                    games_asked.append(game_reference)
                    if Choice == "y" or Choice == "Y":
                        if games_left % 2 == 0:
                            games_left = games_left/2
                            del ranked_games[int(games_left):int(len(ranked_games))]
                            rating_reference = 1
                        else:
                            if len(ranked_games) == 1:
                                rating_reference = 1
                                games_left = 0
                            else:
                                rating_reference = 1
                                games_left = (games_left / 2) - 0.5
                                del ranked_games[int(games_left):int(len(ranked_games))]
                    elif Choice == "n" or Choice == "N":
                        if games_left % 2 == 0:
                            games_left = int(len(ranked_games)/2)
                            del ranked_games[0:games_left]
                            games_left = len(ranked_games)
                            rating_reference = - 1
                        else:
                            if len(ranked_games) == 1:
                                rating_reference = - 1
                                games_left = 0
                            else:
                                rating_reference = - 1
                                games_left = len(ranked_games)
                                del ranked_games[0:int((int(games_left)/2)-0.5)]
                                games_left = len(ranked_games)
                else:
                    games_left = 0
            else:
                games_left = 0
        else:
            position_found = True
    

    print(rating_reference)
  



game_dictionary = {}
##Collect all saved data
game_list = getList("GAMES LIST:")
ranked_list = getList("RANKED LIST:")
release_years = getList("RELEASE YEARS:")
developers = getList("DEVELOPERS:")
notes = getList("NOTES:")
if len(game_list) != 0:
    for i in range(0,len(game_list)):
        
        game_dictionary[game_list[i]] = game(game_list[i],ranked_list[i],release_years[i],developers[i],notes[i])
displayMenu()
editTextFile()