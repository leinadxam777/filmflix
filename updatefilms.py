from connect import *

def update_films():
    # Use primary key to update a record
    idField = int(input("Enter the identification number of the film you want to update: "))
    
    # field to update 
    fieldName = input("Choose the field to update: (title, yearReleased, rating, duration or genre)")
    
    fieldValue = input(f"Enter the value for {fieldName} field: ")
    
    filmCursor.execute(f"UPDATE tblFilms SET {fieldName} = '{fieldValue}' WHERE filmID = {idField}")

    # filmCursor.execute("UPDATE tblFilms SET genre = ? WHERE filmID = ?", (fieldValue, idField))
    
   
    connection.commit()
    print(f"The filmID {idField} has been updated")
    
if __name__ == "__main__":
    update_films()
    