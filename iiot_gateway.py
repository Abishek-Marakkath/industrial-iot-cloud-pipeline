import paho.mqtt.client as mqtt
import json
import sqlite3

# MQTT Broker Settings
BROKER = "localhost"
PORT = 1883
TOPIC = "iiot/telemetry"

# Setup Local Database Connection
db_connection = sqlite3.connect("sensor_data.db", check_same_thread=False)
cursor = db_connection.cursor()

# Create a table if it doesn't exist already
cursor.execute("""
    CREATE TABLE IF NOT EXISTS telemetry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id TEXT,
        timestamp TEXT,
        temperature REAL,
        pressure REAL
    )
""")
db_connection.commit()

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    try:
        data = json.loads(payload)
        
        device = data.get("device_id", "UNKNOWN")
        timestamp = data.get("timestamp", "")
        temp = data.get("measurements", {}).get("temperature", 0.0)
        pressure = data.get("measurements", {}).get("pressure", 0.0)
        
        # Insert the newly parsed data into the database
        cursor.execute(
            "INSERT INTO telemetry (device_id, timestamp, temperature, pressure) VALUES (?, ?, ?, ?)",
            (device, timestamp, temp, pressure)
        )
        db_connection.commit()
        
        print(f"[{device}] Saved to DB -> Temp: {temp}°C | Pressure: {pressure}")
        
    except json.JSONDecodeError:
        print(f"Error parsing JSON: {payload}")

gateway_client = mqtt.Client()
gateway_client.on_message = on_message

print("Gateway connecting to MQTT Broker...")
gateway_client.connect(BROKER, PORT, 60)
gateway_client.subscribe(TOPIC)

print(f"Gateway subscribed to: {TOPIC}")
print("Listening and saving to SQLite Database. Press Ctrl+C to exit.\n")

try:
    gateway_client.loop_forever()
except KeyboardInterrupt:
    print("\nShutting down Gateway and closing database connection...")
    db_connection.close()
    gateway_client.disconnect()
