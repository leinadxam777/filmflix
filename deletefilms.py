from connect import *

def delete_films():
    # use primary key to update a record
    idField = input("Enter the identification number of the film you want to delete: ")
    
    filmCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
    connection.commit()
    
    print(f"The {idField} film ID has been deleted from films table")
    
if __name__ == "__main__":
    delete_films()