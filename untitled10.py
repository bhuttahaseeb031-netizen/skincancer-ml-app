import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Page title and layout
st.set_page_config(page_title="ML Prediction App", layout="centered")
st.title("Machine Learning Prediction App")
st.write("Neeche diye gaye features enter karein aur prediction hasil karein:")

# Load saved features list and trained model
@st.cache_resource
def load_files():
    with open("features.pkl", "rb") as f:
        features = pickle.load(f)
    # Note: Apni model file ka sahi naam yahan likhein (e.g., model.pkl)
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return features, model

try:
    features, model = load_files()

    # Create input fields dynamically based on features.pkl
    input_data = {}
    st.subheader("Input Features")
    
    for feature in features:
        input_data[feature] = st.number_input(f"Enter {feature}", value=0.0, format="%.4f")

    # Predict button
    if st.button("Predict"):
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)
        st.success(f"Predicted Result: {prediction[0]:,.2f}")

except FileNotFoundError as e:
    st.error(f"File nahi mili: {e}. Yaqeeni banayein ke 'features.pkl' aur 'model.pkl' GitHub repository mein maujood hain.")
except Exception as e:
    st.error(f"Error: {e}")
