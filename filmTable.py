from connect import * # import the connect.py module 


filmCursor.execute(""" 
CREATE TABLE IF NOT EXISTS "tblfilms" (
    "filmID" INTEGER NOT NULL UNIQUE,
    "title" TEXT NOT NULL,
    "yearReleased" INTEGER NOT NULL,
    "rating" TEXT NOT NULL,
    "duration" INTEGER NOT NULL,
    "genre" TEXT NOT NULL,
    PRIMARY KEY("filmID" AUTOINCREMENT))
""")