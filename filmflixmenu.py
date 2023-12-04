import readfilms, addfilms, updatefilms, deletefilms, reportfilms

# create function 
def menuFile():
    with open('filmflix-py/filmMenu.txt') as flixMenuFile:

        flixFileData = flixMenuFile.read()
        return flixFileData
    
# print(menuFile())

def film_menu():
    option = 0 # initialise the option variable with an integer value 0
    optionsList = ["1","2","3","4","5","6"]

    # initialise the menu file function with the choiceMenu variable 
    choiceMenu = menuFile() 

    while option not in optionsList:
        print(choiceMenu)
        option = input("Enter an option from the FLIMFLIX main menu: ")
        
        if option not in optionsList:
            print(f"{option} is not a valid choice! ")
    return option

mainProgram = True

while mainProgram: 
    
    mainMenu = film_menu()
    
    if mainMenu == "1":
       readfilms.read_films()

    elif mainMenu == "2":
        addfilms.insert_films()

    elif mainMenu == "3":
        updatefilms.update_films()

    elif mainMenu == "4":
        deletefilms.delete_films()
    
    elif mainMenu == "5":
        reportfilms.film_reports()
    
    else:
        mainProgram = False
input("Press Enter to quit the FILMFLIX Application")


  