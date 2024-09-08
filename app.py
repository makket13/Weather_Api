from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Συνάρτηση για σύνδεση με τη βάση δεδομένων
def connect_db():
    conn = sqlite3.connect('weather.db')
    return conn

# 1. Λίστα τελευταίων προβλέψεων για κάθε τοποθεσία
@app.route('/latest', methods=['GET'])
def get_latest_forecast():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT location, date, temperature, precipitation, wind_speed FROM forecast ORDER BY date DESC LIMIT 3")
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

# 2. Λίστα του μέσου όρου θερμοκρασίας για τις τελευταίες 3 προβλέψεις
@app.route('/average_temp', methods=['GET'])
def get_average_temp():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
        SELECT location, AVG(temperature) as avg_temp
        FROM forecast
        GROUP BY location
        ORDER BY date DESC
        LIMIT 3
    """)
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

# 3. Τοποθεσίες με βάση την υψηλότερη θερμοκρασία
@app.route('/top_locations', methods=['GET'])
def get_top_locations():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
        SELECT location, MAX(temperature) as max_temp
        FROM forecast
        GROUP BY location
        ORDER BY max_temp DESC
        LIMIT 5
    """)
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

# Εκκίνηση του Flask app
if __name__ == '__main__':
    app.run(debug=True)
