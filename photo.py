from io import BytesIO
from tkinter import Image

import PIL
import requests


def download_photo(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            img = Image.open(BytesIO(response.content))
            img.save(file_path)
            print("Photo downloaded successfully!")
        except PIL.UnidentifiedImageError:
            print("Failed to identify the image file.")
    else:
        print("Failed to download photo.")