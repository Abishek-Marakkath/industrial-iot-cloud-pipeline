import streamlit as st
import pandas as pd
import sqlite3
import time

st.set_page_config(page_title="IIoT Dashboard", layout="wide")
st.title("🏭 Real-Time IIoT Telemetry Dashboard")

def load_data():
    # Connect to the SQLite database
    conn = sqlite3.connect("sensor_data.db")
    # Grab the 50 most recent readings
    df = pd.read_sql_query("SELECT * FROM telemetry ORDER BY id DESC LIMIT 50", conn)
    conn.close()
    return df

# Load the data
df = load_data()

if not df.empty:
    # Display the absolute latest reading as big metrics
    latest_reading = df.iloc[0]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Device ID", latest_reading['device_id'])
    col2.metric("Latest Temperature", f"{latest_reading['temperature']} °C")
    col3.metric("Latest Pressure", f"{latest_reading['pressure']} units")

    st.subheader("Live Telemetry Trends")
    # Sort data chronologically so the chart reads left-to-right
    chart_data = df.sort_values('id').set_index('timestamp')[['temperature', 'pressure']]
    st.line_chart(chart_data)

    st.subheader("Raw Database Records")
    st.dataframe(df)
else:
    st.write("Waiting for data... Make sure your simulator and gateway are running!")

# Tell the web page to automatically refresh every 2 seconds
time.sleep(2)
st.rerun()
