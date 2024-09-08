import requests
import sqlite3

# Στοιχεία API
BASE_URL = "https://api.meteomatics.com/"
USERNAME = "margera_makris_konstantinos"
PASSWORD = "N85N5oMhHd"

# Λίστα με τις τοποθεσίες που θέλουμε (Γεωγραφικό πλάτος και μήκος)
locations = {
    "Berlin": "52.520551,13.461804",
    "London": "51.5074,-0.1278",
    "Paris": "48.8566,2.3522",
    "New York": "40.7128,-74.0060"
}

# Δημιουργία ή σύνδεση στη βάση δεδομένων
def create_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    
    # Δημιουργία πίνακα αν δεν υπάρχει
    c.execute('''CREATE TABLE IF NOT EXISTS forecast (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    location TEXT,
                    date TEXT,
                    temperature REAL,
                    precipitation REAL,
                    wind_speed REAL
                )''')
    conn.commit()
    conn.close()

# Συνάρτηση για λήψη δεδομένων από το API
def get_weather_forecast(location, coords):
    url = f"{BASE_URL}2024-09-08T00:00:00Z/t_2m:C,precip_1h:mm,wind_speed_10m:ms/{coords}/json"
    response = requests.get(url, auth=(USERNAME, PASSWORD))
    
    if response.status_code == 200:
        print(f"Data fetched successfully for {location}!")
        print(f"Response JSON for {location}: {response.json()}")  # Εκτύπωση των δεδομένων που λαμβάνονται για debug
        return response.json()
    else:
        print(f"Error fetching data for {location}: {response.status_code}")
        return None

# Συνάρτηση για αποθήκευση δεδομένων στη βάση
def save_forecast(location, date, temperature, precipitation, wind_speed):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    
    # Εισαγωγή δεδομένων στον πίνακα
    c.execute("INSERT INTO forecast (location, date, temperature, precipitation, wind_speed) VALUES (?, ?, ?, ?, ?)",
              (location, date, temperature, precipitation, wind_speed))
    
    conn.commit()
    conn.close()

# Κύρια συνάρτηση για λήψη και αποθήκευση δεδομένων για πολλές τοποθεσίες
def main():
    for location, coords in locations.items():
        data = get_weather_forecast(location, coords)
        
        if data:
            temperature = None
            precipitation = None
            wind_speed = None
            
            for item in data['data']:
                for coord in item['coordinates']:
                    for date_info in coord['dates']:
                        date = date_info['date']
                        if item['parameter'] == 't_2m:C':
                            temperature = date_info['value']
                        elif item['parameter'] == 'precip_1h:mm':
                            precipitation = date_info['value']
                        elif item['parameter'] == 'wind_speed_10m:ms':
                            wind_speed = date_info['value']
                        
                        # Αποθήκευση στη βάση δεδομένων
                        save_forecast(location, date, temperature, precipitation, wind_speed)
                        print(f"Saved data for {location} on {date}. Temperature: {temperature}, Precipitation: {precipitation}, Wind Speed: {wind_speed}")

# Εκτέλεση
if __name__ == "__main__":
    create_db()  # Δημιουργία της βάσης αν δεν υπάρχει
    main()       # Εκτέλεση της κύριας συνάρτησης
