import streamlit as st
import numpy as np
import joblib

# Load the saved models
scaler_X = joblib.load('models/scaler_X.pkl')
scaler_y = joblib.load('models/scaler_y.pkl')
standard_scaler = joblib.load('models/standard_scaler.pkl')
pca = joblib.load('models/pca_transformer.pkl')
model = joblib.load('models/random_forest.pkl')

# Input form
st.title("Life Expectancy Predictor")

feature_names = [
    "Adult Mortality", "infant deaths", "Alcohol", "percentage expenditure",
    "Hepatitis B", "Measles", "under-five deaths", "Polio", "Total expenditure",
    "Diphtheria", "HIV/AIDS", "GDP", "Population", "thinness 1-19 years",
    "thinness 5-9 years", "Income composition of resources", "Schooling",
]

# Sample input values
sample_input = [
    263, 62, 0.01, 71.27962362, 65, 1154, 83, 6, 8.16,
    65, 0.1, 584.25921, 33736494, 17.2, 17.3, 0.479, 10.1
]

# # Add toggle
# use_sample = st.checkbox("Use sample input values")

user_inputs = []

# Create 3 columns
cols = st.columns(3)

# Autofill inputs with sample values, no checkbox
for idx, feature in enumerate(feature_names):
    col = cols[idx % 3]
    default_val = sample_input[idx]  # Always use sample_input as default
    value = col.number_input(f"{feature}", step=0.1, value=float(default_val))
    user_inputs.append(value)

if st.button("Predict"):
    # Convert to 2D array
    user_array = np.array(user_inputs).reshape(1, -1)

    # Scale, PCA, Predict
    scaledX = scaler_X.transform(user_array)
    scaled = standard_scaler.transform(scaledX)
    reduced = pca.transform(scaled)
    prediction = model.predict(reduced)
    inverseScaleY = scaler_y.inverse_transform(prediction.reshape(1, -1))

    # Get scalar from 2D array
    predicted_value = inverseScaleY[0, 0]

    st.success(f"Predicted Life Expectancy: {predicted_value:.2f}")