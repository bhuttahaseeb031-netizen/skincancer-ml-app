import os
import urllib.request
import pickle

if not os.path.exists("model.pkl"):
    file_id = "APNI_GOOGLE_DRIVE_FILE_ID_YAHAN_LIKHEIN"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    urllib.request.urlretrieve(url, "model.pkl")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
