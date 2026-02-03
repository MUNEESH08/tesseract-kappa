from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image
import os

app = FastAPI()

# Tell Tesseract where traineddata is
os.environ["TESSDATA_PREFIX"] = "/app/tessdata"

@app.post("/tesseract-kappa/mytrained")
async def ocr_mytrained(file: UploadFile = File(...)):
    image = Image.open(file.file)

    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(
        image,
        lang="mytrained",
        config=custom_config
    )

    return {
        "model": "mytrained",
        "extracted_text": text.strip()
    }