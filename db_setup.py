import sqlite3

conn = sqlite3.connect('weather.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS forecast (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT NOT NULL,
        date TEXT NOT NULL,
        temperature REAL NOT NULL
    )
''')

conn.commit()
conn.close()
