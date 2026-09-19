import paho.mqtt.client as mqtt
import time
import json
from datetime import datetime
import random

# MQTT Broker Settings
BROKER = "localhost"
PORT = 1883
TOPIC = "iiot/telemetry"
DEVICE_ID = "SIMULATOR_01"

# Setup the MQTT Client (Using standard setup)
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print(f"[{DEVICE_ID}] Connected to local MQTT Broker. Starting telemetry stream...")

try:
    while True:
        # 1. Generate fake sensor data
        temperature = round(random.uniform(40.0, 60.0), 2)
        pressure = round(random.uniform(100.0, 120.0), 2)
        
        # 2. Package it into a Python dictionary
        data_payload = {
            "device_id": DEVICE_ID,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "measurements": {
                "temperature": temperature,
                "pressure": pressure
            },
            "status": "online"
        }
        
        # 3. Convert the dictionary to a JSON string
        json_message = json.dumps(data_payload)
        
        # 4. Publish the message to the broker
        client.publish(TOPIC, json_message)
        print(f"Published: {json_message}")
        
        # Wait 2 seconds before sending the next reading
        time.sleep(2)

except KeyboardInterrupt:
    print(f"\n[{DEVICE_ID}] Shutting down simulator...")
    client.disconnect()
