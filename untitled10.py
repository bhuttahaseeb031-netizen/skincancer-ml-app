import os
import pickle
import streamlit as st
import gdown

FILE_ID = "APNI_GOOGLE_DRIVE_FILE_ID_YAHAN_LIKHEIN"
MODEL_PATH = "model.pkl"


def download_model(file_id: str, model_path: str) -> None:
    """Google Drive se model file download karta hai agar pehle se mojood na ho."""
    if os.path.exists(model_path) and os.path.getsize(model_path) > 1024:
        return

    if os.path.exists(model_path):
        os.remove(model_path)

    url = f"https://drive.google.com/uc?id={file_id}"
    downloaded = gdown.download(url=url, output=model_path, quiet=True, fuzzy=True)

    if not downloaded or not os.path.exists(model_path) or os.path.getsize(model_path) < 1024:
        raise RuntimeError(
            "Model file Google Drive se download nahi ho saki. "
            "Check karein ke FILE_ID sahi hai aur file ki sharing 'Anyone with the link' par set hai."
        )


@st.cache_resource(show_spinner="Model load ho raha hai...")
def load_model():
    download_model(FILE_ID, MODEL_PATH)
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


model = load_model()
