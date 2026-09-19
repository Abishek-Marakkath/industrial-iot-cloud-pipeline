# Industrial IoT (IIoT) Data Pipeline

A practical industrial telemetry pipeline that simulates edge device data, routes it through an MQTT broker, processes it via a custom Python gateway, and visualizes it in real-time. 

This project demonstrates core Industrial Automation and IIoT concepts, including MQTT publish/subscribe architecture, time-series telemetry routing, and local data storage.

## 🏗️ Architecture Diagram


graph TD
    A[Edge Simulator<br/>device_simulator.py] -- JSON via MQTT --> B((Mosquitto Broker<br/>Port 1883))
    B -- Telemetry Stream --> C[Python Gateway<br/>iiot_gateway.py]
    C -- SQL INSERT --> D[(SQLite Database<br/>sensor_data.db)]
    D -- Live Queries --> E[Streamlit Dashboard<br/>dashboard.py]
    
    style A fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style B fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style C fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    style D fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style E fill:#ffebee,stroke:#d32f2f,stroke-width:2px
