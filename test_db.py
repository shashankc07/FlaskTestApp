import sqlite3 as sql

# Connection to database
conn = sql.connect('test.db')

# Create a cursor
c = conn.cursor()

# Creating a table
c.execute("""
        CREATE TABLE IF NOT EXISTS test (
        pid INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        dob TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL
        )""")

# commit our i.e push the execute command's info into the DB
conn.commit()

# close the connection   --> Always do this
conn.close()
