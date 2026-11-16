import streamlit as st
import pandas as pd
import pickle
import gdown
import os

# Google Drive se model download karne ke liye (apni File ID yahan dalein)
file_id = "APNI_GOOGLE_DRIVE_FILE_ID_YAHAN_DALEIN"
if not os.path.exists("model.pkl"):
    gdown.download(f"https://drive.google.com/uc?id={file_id}", "model.pkl", quiet=False)

# Baqi purana code
@st.cache_resource
def load_files():
    with open("features.pkl", "rb") as f:
        features = pickle.load(f)
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return features, model
