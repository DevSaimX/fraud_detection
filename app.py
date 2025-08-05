# app.py

import streamlit as st
import numpy as np
import joblib

# Load saved model and scaler
model = joblib.load("logistic_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Fraud Detection App", layout="centered")
st.title("💳 Real-Time Credit Card Fraud Detection")
st.markdown("Enter transaction details to check if it's **fraudulent** or **legit**.")

# Input fields
amount = st.number_input("Transaction Amount", min_value=0.0, value=100.0)
time = st.number_input("Time (seconds since first transaction)", min_value=0.0, value=50000.0)

# PCA features (V1 to V28)
st.markdown("### Anonymized Transaction Features (V1 to V28)")
v_inputs = []
for i in range(1, 29):
    val = st.number_input(f"V{i}", value=0.0, key=f"v{i}")
    v_inputs.append(val)

# Combine input
if st.button("Predict"):
    # Scale Amount and Time
    scaled_vals = scaler.transform([[amount, time]])[0]
    amount_scaled = scaled_vals[0]
    time_scaled = scaled_vals[1]

    # Final input order: Time, V1..V28, Amount
    input_data = [time_scaled] + v_inputs + [amount_scaled]
    input_array = np.array(input_data).reshape(1, -1)

    prediction = model.predict(input_array)[0]
    probability = model.predict_proba(input_array)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Fraud Detected! (Probability: {probability:.2%})")
    else:
        st.success(f"✅ Legit Transaction (Probability of fraud: {probability:.2%})")
