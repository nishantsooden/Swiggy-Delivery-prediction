import streamlit as st
import pandas as pd
import joblib
import os
import pickle
# Page config
st.set_page_config(
    page_title="Swiggy Delivery Time Prediction",
    page_icon="🍔",
    layout="centered"
)

# Load model
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)

MODEL_PATH = os.path.join(BASE_DIR, "model", "swiggy.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))

model = pickle.load(open(MODEL_PATH, "rb"))

# Title
st.title("🍔 Swiggy Delivery Time Prediction")
st.markdown("Predict delivery time using Machine Learning")

st.divider()

# Sidebar inputs
st.sidebar.header("📌 Enter Order Details")

distance = st.sidebar.slider("Distance (km)", 0.5, 20.0, 5.0)
prep_time = st.sidebar.slider("Preparation Time (minutes)", 5, 60, 20)
experience = st.sidebar.slider("Courier Experience (years)", 0, 10, 2)

weather = st.sidebar.selectbox(
    "Weather",
    ["Clear", "Rainy", "Foggy", "Stormy"]
)

traffic = st.sidebar.selectbox(
    "Traffic Level",
    ["Low", "Medium", "High", "Jam"]
)

time_of_day = st.sidebar.selectbox(
    "Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

vehicle = st.sidebar.selectbox(
    "Vehicle Type",
    ["Bike", "Scooter", "Car"]
)

# Create input DataFrame
input_data = pd.DataFrame({
    "Distance_km": [distance],
    "Weather": [weather],
    "Traffic_Level": [traffic],
    "Time_of_Day": [time_of_day],
    "Vehicle_Type": [vehicle],
    "Preparation_Time_min": [prep_time],
    "Courier_Experience_yrs": [experience]
})

st.subheader("📊 Input Data")
st.dataframe(input_data, use_container_width=True)

# Prediction
if st.button("🚀 Predict Delivery Time"):
    prediction = model.predict(input_data)[0]

    st.success(f"🕒 Estimated Delivery Time: *{prediction:.2f} minutes*")

    if prediction <= 30:
        st.balloons()
        st.info("🔥 Fast Delivery Expected!")
    elif prediction <= 45:
        st.warning("⏳ Moderate Delivery Time")
    else:
        st.error("🚨 Delivery might take longer")

st.divider()

st.caption("📌 Built by Nishant | Swiggy ML Project")