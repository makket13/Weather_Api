import sqlite3

# Σύνδεση στη βάση δεδομένων
conn = sqlite3.connect('weather.db')
c = conn.cursor()

# Δημιουργία πίνακα για τις προβλέψεις καιρού
c.execute('''
    CREATE TABLE IF NOT EXISTS forecast (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT NOT NULL,
        date TEXT NOT NULL,
        temperature REAL NOT NULL
    )
''')

# Κλείσιμο σύνδεσης
conn.commit()
conn.close()
