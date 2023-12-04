import sqlite3 as sql

connection = sql.connect('filmflix-py/filmflix.db')


# Create a cursor variable and assigned it to the cursor method to excute sql statements
filmCursor = connection.cursor()
