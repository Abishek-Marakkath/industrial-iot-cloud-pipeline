# Industrial IoT (IIoT) Data Pipeline

A practical industrial telemetry pipeline that simulates edge device data, routes it through an MQTT broker, processes it via a custom Python gateway, and visualizes it in real-time. 

This project demonstrates core Industrial Automation and IIoT concepts, including MQTT publish/subscribe architecture, time-series telemetry routing, and local data storage.

## 🏗️ Architecture Diagram

`text
[ Simulator ] ---> JSON / MQTT ---> [ Mosquitto Broker ]
(device_simulator.py)                  (Local: Port 1883)
                                              |
                                              v
[ Dashboard ] <--- SQLite 3 <------ [ Python Gateway ]
(dashboard.py)    (sensor_data.db)    (iiot_gateway.py)
