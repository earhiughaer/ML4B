import streamlit as st
import pandas as pd
import altair as alt
import json

# Laden Sie die Sensordaten aus der JSON-Datei
with open('test.json') as f:
    data = json.load(f)

# Konvertieren Sie die Daten in ein Pandas DataFrame
df = pd.json_normalize(data)

# Erstellen Sie ein Liniendiagramm der Beschleunigungsdaten
accel_chart = alt.Chart(df).mark_line().encode(
    x="Timestamp",
    y="Acceleration",
    color="Axis"
).properties(
    title="Beschleunigungsdaten des Smartphones"
)

# Erstellen Sie ein Streudiagramm der Position des Smartphones
position_chart = alt.Chart(df).mark_circle().encode(
    x="Longitude",
    y="Latitude",
    color=alt.Color("Timestamp", scale=alt.Scale(scheme="reds")),
    size="Accuracy"
).properties(
    title="Flugbahn des Smartphones"
)

# Zeigen Sie die Diagramme in der Streamlit-Anwendung an
st.title("Flugbahn des Smartphones")
st.altair_chart(accel_chart, use_container_width=True)
st.altair_chart(position_chart, use_container_width=True)
