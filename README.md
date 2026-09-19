# Industrial IoT (IIoT) Data Pipeline

A practical industrial telemetry pipeline that simulates edge device data, routes it through an MQTT broker, processes it via a custom Python gateway, and visualizes it in real-time. 

This project demonstrates core Industrial Automation and IIoT concepts, including MQTT publish/subscribe architecture, time-series telemetry routing, and local data storage.

## 🏗️ System Architecture

```mermaid
graph TD
    A[Edge Simulator<br/>device_simulator.py] -- JSON via MQTT --> B((Mosquitto Broker<br/>Port 1883))
    B -- Telemetry Stream --> C[Python Gateway<br/>iiot_gateway.py]
    C -- SQL INSERT --> D[(SQLite Database<br/>sensor_data.db)]
    D -- Live Queries --> E[Streamlit Dashboard<br/>dashboard.py]
    
    style A fill:#2C3E50,stroke:#1A252F,stroke-width:2px,color:#fff
    style B fill:#D35400,stroke:#A04000,stroke-width:2px,color:#fff
    style C fill:#27AE60,stroke:#1E8449,stroke-width:2px,color:#fff
    style D fill:#2980B9,stroke:#1F618D,stroke-width:2px,color:#fff
    style E fill:#8E44AD,stroke:#6C3483,stroke-width:2px,color:#fff
