from connect import *

# Create Subroutine
def read_films():
    
    # select all records
    filmCursor.execute("SELECT * FROM tblFilms")
    
    # fetch the selected records
    filmRecords = filmCursor.fetchall()
    
    # loop through filmRecords
    for eachRecord in filmRecords:
        print(eachRecord)
        
if __name__ == "__main__":
    read_films()
    
