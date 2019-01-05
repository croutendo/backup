#databases
#create a new SQLite database
import sqlite3
db = sqlite3.connect("new_database.db")

#create a new table
db.execute("""
    DROP TABLE IF EXISTS new_database
    """)
db.execute("""
    CREATE TABLE new_database (
        firstname VARCHAR(35), lastname VARCHAR(35), address VARCHAR(50),
        city VARCHAR(50), state VARCHAR(2), zipcode VARCHAR(10),
        phonenumber VARCHAR(11))
    """)

#populate the database
db.execute("""
    INSERT INTO new_database (
        firstname, lastname, address, city, state, zipcode, phonenumber)
        VALUES
        ("Bruce", "Wayne", "142 Derp Lane", "Gotham City", "NY", 10017, 13475551234)
    """)
db.execute("""
    INSERT INTO new_database (
        firstname, lastname, address, city, state, zipcode, phonenumber)
        VALUES
        ("Joe", "Hugivszadam", "646 IDK Street", "Minas Tirith", "WY", 98765, 19095554321)
    """)
db.execute("""
    INSERT INTO new_database (
        firstname, lastname, address, city, state, zipcode, phonenumber)
        VALUES
        ("Brucius", "Wayne", "142 Derp Lane", "Gotham City", "NY", 10017, 13475551234)
    """)
db.execute("""
    INSERT INTO new_database (
        firstname, lastname, address, city, state, zipcode, phonenumber)
        VALUES
        ("Josephine", "Hugivszadam", "646 IDK Street", "Minas Tirith", "WY", 98765, 19095554321)        
    """)

#retrieve and display the data
cursor = db.execute("""
    SELECT * FROM new_database
    """)
for row in cursor:
    print(row)
    print()
print()

#delete a row
db.execute("""
    DELETE FROM new_database WHERE firstname = "Joe"
    """)

#retrieve and display the data
cursor = db.execute("""
    SELECT * FROM new_database
    """)
for row in cursor:
    print(row)
    print()
print()

db.close()
                    
