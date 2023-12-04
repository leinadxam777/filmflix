from connect import *

# Create a subroutine
def insert_films():
    # Ask user for input for Title, Artist, Genre
    filmTitle = input("What is the film title: ")
    filmYear = int(input("Which year it was released: "))
    filmRating = input("Enter the rating: ")
    filmDuration = int(input("How long is the duration: "))
    filmGenre = input("Enter the genre: ")
    
    
    # Insert data into our songs table
    filmCursor.execute("INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)", (filmTitle, filmYear, filmRating, filmDuration, filmGenre))
    
    # Commit the change
    connection.commit()
    
    # Testing
    print(f"The {filmTitle} has been succesfully inserted into the films table")

if __name__ == "__main__":
    insert_films()