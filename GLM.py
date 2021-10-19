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


def printAllLists():
    print(game_list)
    print(release_years)
    print(developers)
    print(notes)
    print(dates)
    print(ranked_list)

def getListOfLists(list_name):
    n= 0
    checked = 0
    the_list = []
    while checked == 0:
        if lines[n].find(list_name) != -1:
            checked = 1
        else:
            n += 1
    x = n + 1
    checked = 0
    while checked == 0:
        if lines[x] == "\n":
            checked =1
        else:
            line = lines[x].rstrip("\n")
            split_list = [x.strip() for x in line.split(',')]
            the_list.append(split_list)
            x = x+1
        
    return the_list


def getList(list_name):
    n= 0
    checked = 0
    the_list = []
    while checked == 0:
        if lines[n].find(list_name) != -1:
            checked = 1
        else:
            n += 1
    x = n + 1
    checked = 0
    while checked == 0:
        if lines[x] == "\n":
            checked =1
        else:
            the_list.append(lines[x].rstrip("\n"))
            x = x+1
        
    return the_list


def addGame():
    game_title = input("What is the title of the game>\n")
    game_release_year = input("What year did the game come out?\n")
    game_developer = input("Who made the game?\n")
    game_notes = []
    today = date.today()
    game_date_added = today.strftime("%d/%m/%Y")
    complete = 0
    at_least_one = False
    while complete == 0:
        note = input("Notes about the game:   (X to skip)\n")
        if note == "x" or note == "X":
            if at_least_one == True:
                complete = 1
            else:
                game_notes.append("none")
        else:
            at_least_one = True
        
        game_notes.append(note)
    game_dictionary[game_title] = game(game_title,game_release_year,game_developer,game_notes,game_date_added)
    game_list.append(game_title)
    release_years.append(game_release_year)
    developers.append(game_developer)
    notes.append(game_notes)
    dates.append(game_date_added)
    if len(game_list) == 1:
        ranked_list.append(game_title)
    else:
        filmRankedInsertion((game_dictionary[game_title]))


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
    output_lines = []
    output_lines.append("    GAMES LIST:")
    for game in game_list:
        output_lines.append(game)
    for i in range (0,2):
        output_lines.append("\n")
    output_lines.append("    RANKED LIST:")
    for game in ranked_list:
        output_lines.append(game)
    for i in range (0,2):
        output_lines.append("\n")
    output_lines.append("    RELEASE YEARS:")
    for year in release_years:
        output_lines.append(year)
    for i in range (0,2):
        output_lines.append("\n")
    output_lines.append("    DEVELOPERS:")
    for developer in developers:
        output_lines.append(developer)
    for i in range (0,2):
        output_lines.append("\n")
    output_lines.append("    NOTES:")
    for note in notes:
        string = ""
        for further_notes in note:
            string = string + further_notes + ","
        output_lines.append(string)
    for i in range (0,2):
        output_lines.append("\n")
    output_lines.append("    DATES ADDED:")
    for date in dates:
        output_lines.append(date)
    for i in range (0,2):
        output_lines.append("\n")


    file_to_write = open("GAMELIST.txt","w")
    for line in output_lines:
        file_to_write.write(str(line))
        file_to_write.write("\n")
    file_to_write.close()


def filmRankedInsertion(game):
    
    ranked_list_sub = list(ranked_list)
    list_length = len(ranked_list_sub)
    rankings = list(range(1,list_length + 1))
    game_reference = ""
    rating_reference = 0
    games_asked = []
    position_found = False
    while position_found == False:
        if list_length > 0:
            if ranked_list_sub[int(list_length/2)] not in games_asked:
                if game_reference != ranked_list_sub[int(list_length/2)]:
                    if list_length % 2 == 0:
                        print("Is",game.title,"better than: ",ranked_list_sub[int(list_length/2)])
                        game_reference = ranked_list_sub[int(list_length/2)]
                    else:
                        print("Is",game.title,"better than: ",ranked_list_sub[int((list_length/2)-0.5)])
                        game_reference = ranked_list_sub[int(list_length/2)]
                    print("Y or N")
                    valid_input = False
                    while valid_input == False:
                        choice = input()
                        if choice == "y" or choice == "Y" or choice == "n" or choice == "N":
                            valid_input = True
                        else:
                            print("Y or N")
                    games_asked.append(game_reference)

                    if choice == "y" or choice == "Y":
                        if list_length % 2 == 0:
                            list_length = list_length/2
                            print(ranked_list)
                            print(ranked_list_sub)
                            del ranked_list_sub[int(list_length):int(len(ranked_list_sub))]
                            print(ranked_list)
                            print(ranked_list_sub)
                            rating_reference = 1
                        else:
                            if len(ranked_list_sub) == 1:
                                rating_reference = 1
                                list_length = 0
                            else:
                                rating_reference = 1
                                list_length = (list_length / 2) - 0.5
                                del ranked_list_sub[int(list_length):int(len(ranked_list_sub))]
                    
                    elif choice == "n" or choice == "N":
                        if list_length % 2 == 0:
                            list_length = int(len(ranked_list_sub)/2)
                            del ranked_list_sub[0:list_length]
                            list_length = len(ranked_list_sub)
                            RatingReference = - 1
                        else:
                            if len(ranked_list_sub) == 1:
                                RatingReference = - 1
                                list_length = 0
                            else:
                                RatingReference = - 1
                                list_length = len(ranked_list_sub)
                                del ranked_list_sub[0:int((int(list_length)/2)-0.5)]
                                list_length = len(ranked_list_sub)
                else:
                    list_length = 0
            else:
                list_length = 0
        else:
            position_found = True
    if rating_reference == 1:
        print(ranked_list.index(game_reference))
        ranked_list.insert((ranked_list.index(game_reference)), game.title)
        print(ranked_list)
    if rating_reference == -1:
        ranked_list.insert((ranked_list.index(game_reference)), game.title)
  



game_dictionary = {}
##Collect all saved data
game_list = getList("GAMES LIST:")
print(game_list)
ranked_list = getList("RANKED LIST:")
release_years = getList("RELEASE YEARS:")
developers = getList("DEVELOPERS:")
notes = getListOfLists("NOTES:")
dates = getList("DATES ADDED:")
if len(game_list) != 0:
    for i in range(0,len(game_list)):
        game_dictionary[game_list[i]] = game(game_list[i],ranked_list[i],release_years[i],developers[i],notes[i])
displayMenu()
editTextFile()