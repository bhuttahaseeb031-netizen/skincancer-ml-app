import os
import pickle
import urllib.request
import streamlit as st

MODEL_PATH = "model.pkl"
FILE_ID = "YOUR_ACTUAL_GOOGLE_DRIVE_FILE_ID"  # Replace with your real Google Drive file ID


def download_model(file_id: str, dest_path: str) -> None:
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with urllib.request.urlopen(req) as response:
        content_type = response.headers.get("Content-Type", "")
        data = response.read()

    # Google Drive sometimes returns an HTML warning/confirmation page for large files
    if "text/html" in content_type or data.lstrip().startswith(b"<!DOCTYPE html"):
        raise RuntimeError(
            "Google Drive returned an HTML page instead of the model file. "
            "Check that link sharing is set to 'Anyone with the link', or host the file "
            "on Hugging Face / GitHub Releases for reliable direct downloads."
        )

    with open(dest_path, "wb") as f:
        f.write(data)


@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        download_model(FILE_ID, MODEL_PATH)

    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


model = load_model()
