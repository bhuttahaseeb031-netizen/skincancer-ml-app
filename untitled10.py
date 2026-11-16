import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Skin Cancer Prediction App", page_icon="🩺", layout="centered"
)

st.title("🩺 Skin Cancer Prediction App")
st.write(
    "Apni details darj karein taake model predict kar sakay ke skin condition"
    " kaisi hai."
)

# Load the trained model directly from GitHub repository folder
@st.cache_resource
def load_model():
  with open("model.pkl", "rb") as f:
    model = pickle.load(f)
  return model


try:
  model = load_model()
  st.success("Model kamyabi ke sath load ho gaya hai! 🎉")
except Exception as e:
  st.error(
    f"Model load karne mein error aya hai: {e}. Baraye meharbani check karein"
    " ke 'model.pkl' file GitHub par mojood hai."
  )

# Yahan se aap apna input form aur prediction logic shuru kar sakte hain
# Masalan:
# age = st.number_input("Age", min_value=1, max_value=100, value=30)
# if st.button("Predict"):
#     # prediction code...
