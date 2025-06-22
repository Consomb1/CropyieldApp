# 🌾 Real-Time Crop Yield Predictor

This is a Streamlit web application that predicts crop yield based on live weather data and farm input features. The model was trained using global crop production data and demonstrates how AI can support **SDG 2: Zero Hunger** by helping farmers and policymakers make smarter, data-driven decisions.

Click here: https://cropyieldpredict.streamlit.app/

---

## 🚀 Project Overview

- **Goal:** Predict crop yield in hectograms per hectare (hg/ha)
- **SDG Addressed:** [SDG 2: Zero Hunger](https://sdgs.un.org/goals/goal2)
- **ML Approach:** Supervised Learning using Random Forest Regressor
- **Live Inputs:** Weather data (temperature and rainfall) from OpenWeatherMap API

---

## 🧠 Features

- Real-time weather input via API
- User selects:
  - Country (e.g. Kenya, India)
  - Crop type (e.g. Maize, Rice)
  - Pesticide usage
  - Year of prediction
- Outputs predicted crop yield in hg/ha

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** [Streamlit](https://streamlit.io/)
- **Libraries:** scikit-learn, pandas, joblib, requests
- **Deployment:** [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📦 Requirements

Install dependencies before running:

```bash
pip install -r requirements.txt
