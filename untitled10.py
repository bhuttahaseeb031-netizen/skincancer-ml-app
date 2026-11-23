import os
import gdown
import pickle

# Agar model.pkl mojood nahi hai toh Google Drive se download karein
if not os.path.exists("model.pkl"):
    file_id = "APNI_GOOGLE_DRIVE_FILE_ID_YAHAN_LIKHEIN"
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, "model.pkl", quiet=False)

# Ab model load karein
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
