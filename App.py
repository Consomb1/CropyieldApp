import joblib
import requests
import pandas as pd
import streamlit as st

# trained model loading
model = joblib.load("yield_model.pkl")

#  OpenWeatherMap API key
API_KEY ="96392bad9b5c7b7b523958aa0b8e2560"
 

st.title("🌾 Real-Time Crop Yield Predictor")
st.markdown("Predicts crop yield based on weather and farm inputs.")

# Inputs
country = st.selectbox("Select Country", ["Kenya", "India", "Uganda", "Nigeria"])
crop = st.selectbox("Select Crop", ["Maize", "Wheat", "Rice, paddy", "Potatoes"])
pesticides = st.number_input("Pesticide Usage (tonnes)", 0.0, 500.0, 100.0)
year = st.slider("Prediction Year", 2000, 2030, 2025)
city = st.text_input("City for Weather Lookup", "Nairobi")

# Function to get weather data
def get_weather(city, country_code):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()
    if 'main' in res:
        return res['main']['temp'], res.get('rain', {}).get('1h', 0)
    return None, None

# Country code mapping (simplified)
country_codes = {
    "Kenya": "KE",
    "India": "IN",
    "Uganda": "UG",
    "Nigeria": "NG"
}

# Predict button
if st.button("Predict Crop Yield"):
    code = country_codes.get(country, "KE")
    temp, rain = get_weather(city, code)

    if temp is None:
        st.error("⚠️ Could not fetch weather. Check city or API key.")
    else:
        # Prepare input
        input_data = {
            'year': year,
            'rainfall_mm': rain,
            'pesticides_tonnes': pesticides,
            'avg_temp': temp,
            f'country_{country}': 1,
            f'crop_{crop}': 1
        }

        # Fill missing columns
        for col in model.feature_names_in_:
            if col not in input_data:
                input_data[col] = 0

        input_df = pd.DataFrame([input_data])
        input_df = input_df[model.feature_names_in_]

        # Predict
        result = model.predict(input_df)[0]
        st.success(f"🌽 Predicted Yield for {crop} in {country} ({year}): {result:.2f} hg/ha")
        st.write(f"🌡️ Temp: {temp}°C, 🌧️ Rainfall: {rain} mm")
