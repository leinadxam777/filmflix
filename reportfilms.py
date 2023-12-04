from connect import *
import filmflixmenu


def filmReportFile():
    with open('filmflix-py/report_films.txt') as filmMenuFile:

        # read from the menu file and assign it to a variable
        filmFileData = filmMenuFile.read()

        return filmFileData
    
# print(filmReportFile())

# Create a subroutine
def film_reports():
    option = 0 
    optionsList = ["1","2","3","4","5"]

    # initialise the menu file function with the choiceMenu variable 
    choiceMenu = filmReportFile() 

    while option not in optionsList:
        print(choiceMenu) 
        option = input("Enter an option from the report menu: ")
        
        if option not in optionsList:
            print(f"{option} is not a valid choice! ")
    return option

reportProgram = True

while reportProgram:
    
    reportMenu = film_reports()

    if reportMenu == "1":
        filmCursor.execute("SELECT * FROM tblFilms")

    elif reportMenu == "2":
        filmGenre = input("Choose a genre: ").title()
        filmCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{filmGenre}'")

    elif reportMenu == "3":
        filmYear = int(input("Enter a year: "))
        filmCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {filmYear}")

    elif reportMenu == "4":
        filmRating = input("Enter a rating: ")
        filmCursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{filmRating}'")
        
    else:
        print("Closing program.......")
        mainProgram = False
        filmflixmenu.film_menu()
        
   
    filmData = filmCursor.fetchall()
    
    for records in filmData:
        print(records)
        
if __name__ == "__main__":
    film_reports()