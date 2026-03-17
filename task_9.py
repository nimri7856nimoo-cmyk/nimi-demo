import sqlite3

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")

cursor.execute("INSERT INTO users VALUES (1, 'Ali')")
cursor.execute("INSERT INTO users VALUES (2, 'Sara')")

conn.commit()

for row in cursor.execute("SELECT * FROM users ORDER BY name"):
    print(row)

conn.close()