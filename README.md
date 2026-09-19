# Industrial IoT (IIoT) Data Pipeline

A practical industrial telemetry pipeline that simulates edge device data, routes it through an MQTT broker, processes it via a custom Python gateway, and visualizes it in real-time. 

This project demonstrates core Industrial Automation and IIoT concepts, including MQTT publish/subscribe architecture, time-series telemetry routing, and local data storage.

## 🏗️ Architecture Diagram

`text
[ Simulator ] --->JSON / MQTT ---> [ Mosquitto Broker ]
(device_simulator.py) (Local: Port 1883)
                                              |
                                              v
[ Dashboard ] <--- SQLite 3 <------ [ Python Gateway ]
(dashboard.py)    (sensor_data.db)    (iiot_gateway.py)

⚙️ Technology Stack
Language: Python 3.11
Message Broker: Eclipse Mosquitto (MQTT)
Edge Communication: paho-mqtt
Data Manipulation: pandas
Visualization: streamlit
Storage: SQLite3 (Local edge storage)

🚀 Key Features
Asynchronous Message Routing: Utilizes MQTT publish/subscribe architecture for lightweight, high-throughput device communication.
JSON Payload Structuring: Packages telemetry data (temperature, pressure, timestamps, device IDs) into standardized JSON formats common in modern PLCs.
Automated Persistence: A custom gateway script continuously listens to the broker and automatically parses and inserts new readings into a relational database.
Real-Time Visualization: A web dashboard that automatically refreshes to display the latest edge readings and historical time-series trends.
