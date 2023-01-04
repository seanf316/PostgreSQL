import psycopg2


# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database (Like a list/array)
cursor = connection.cursor()

# Query1 - select all records from "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# # Query2 - select only the "Name" column records from "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track"
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["TEST"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
