import sqlite3

db = sqlite3.connect('Week14/14-1.db')
cursor = db.cursor()
cursor.execute('drop table if exists Ages')

command = """CREATE TABLE Ages(
    name VARCHAR(128), 
  age INTEGER
  )"""
cursor.execute(command)

cursor.execute("""INSERT INTO Ages (name, age) VALUES ('Caelan', 15);""")
cursor.execute("""INSERT INTO Ages (name, age) VALUES ('Oluwabukunmi', 21);""")
cursor.execute("""INSERT INTO Ages (name, age) VALUES ('Oonagh', 18);""")
cursor.execute("""INSERT INTO Ages (name, age) VALUES ('Loui', 38);""")
cursor.execute("""INSERT INTO Ages (name, age) VALUES ('Katelyne', 25);""")


print(cursor.execute("""SELECT hex(name || age) AS X FROM Ages ORDER BY X"""))