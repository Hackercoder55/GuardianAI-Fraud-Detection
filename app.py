import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Load the saved model and column names
# We use try-except to handle errors in case files are missing
try:
    model = joblib.load('fraud_model.pkl')
    model_columns = joblib.load('model_columns.pkl')
except FileNotFoundError:
    st.error("Error: Model files not found. Please make sure 'fraud_model.pkl' is in the same folder.")
    st.stop()

# 2. Page Setup
st.set_page_config(page_title="Fraud Detection System", layout="centered")

st.title("🛡️ E-Commerce Fraud Detector")
st.write("Enter transaction details below to check for fraud risk.")

# 3. Create Input Fields for the User
# We will create a form so the user can enter data
with st.form("prediction_form"):
    
    # Numeric inputs
    tx_amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=100.0)
    tx_velocity = st.number_input("Transaction Velocity (tx/hr)", min_value=0.0, value=1.0)
    account_age = st.number_input("Account Age (Days)", min_value=0, value=30)
    time_since_last = st.number_input("Time Since Last Transaction (hrs)", min_value=0.0, value=5.0)
    
    # Categorical inputs (Dropdowns)
    # These match the text columns we saw earlier
    device = st.selectbox("Device Type", ["mobile", "tablet", "desktop"])
    browser = st.selectbox("Browser", ["chrome", "safari", "other"])
    
    # Submit button
    submit_val = st.form_submit_button("Predict Fraud Status")

# 4. Logic to handle the prediction when button is clicked
if submit_val:
    # Prepare the data dictionary with default values for missing columns
    # We fill everything with 0 first to match the model structure
    input_data = {col: 0 for col in model_columns}
    
    # Update with the user's actual inputs
    input_data['tx_amount'] = tx_amount
    input_data['tx_velocity'] = tx_velocity
    input_data['account_age_days'] = account_age
    input_data['time_since_last_tx'] = time_since_last
    
    # Handle the text columns (One-Hot Encoding manual mapping)
    # This sets the specific column (e.g., 'device_type_mobile') to 1 if selected
    if 'device_type_' + device in input_data:
        input_data['device_type_' + device] = 1
        
    if 'browser_' + browser in input_data:
        input_data['browser_' + browser] = 1

    # Convert to DataFrame (a single row)
    df_input = pd.DataFrame([input_data])
    
    # Make Prediction
    prediction = model.predict(df_input)[0]
    probability = model.predict_proba(df_input)[0][1] # Probability of being fraud
    
    # Show Results
    st.divider()
    if prediction == 1:
        st.error(f"⚠️ ALERT: This transaction is flagged as FRAUD!")
        st.write(f"**Risk Probability:** {probability * 100:.2f}%")
        st.write("Action: Transaction blocked for review.")
    else:
        st.success(f"✅ CLEAN: Transaction approved.")
        st.write(f"**Risk Probability:** {probability * 100:.2f}%")