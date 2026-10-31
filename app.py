
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("intrusion_detection_model.pkl")
features = joblib.load("feature_columns.pkl")

st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Network Intrusion Detection System")
st.write("Machine Learning Based Cybersecurity Dashboard")

st.subheader("Project Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Dataset Records", "123,117")

with col2:
    st.metric("ML Algorithm", "Random Forest")

st.divider()

st.subheader("Network Traffic Prediction")

st.write("Enter the numerical values for the network traffic features.")

input_values = {}

for feature in features:
    input_values[feature] = st.number_input(
        feature,
        value=0.0
    )

if st.button("Detect Network Traffic"):
    input_df = pd.DataFrame([input_values])

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Category: {prediction}")

    if prediction in ["MQTT", "Thing_speak",
                      "Wipro_bulb_Dataset", "Amazon-Alexa"]:
        st.info("This record belongs to a normal traffic category.")
    else:
        st.error("Potential malicious traffic detected!")
