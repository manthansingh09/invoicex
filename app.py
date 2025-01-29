import os
import cv2
import pytesseract
import pandas as pd
import spacy
from flask import Flask, render_template, request, send_file
from pdf2image import convert_from_path
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

nlp = spacy.load("en_core_web_sm")  # Pretrained model for entity recognition

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Change for Linux/macOS

def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text


def map_invoice_fields(text):
    doc = nlp(text)
    extracted_data = {"Invoice Number": "", "Total Amount": "", "Base Amount": "", "Tax Amount": "", "Sender": "", "Recipient": ""}
    
    for line in text.split("\n"):
        line_lower = line.lower()
        if "invoice" in line_lower and "number" in line_lower:
            extracted_data["Invoice Number"] = line.split()[-1]
        elif "total" in line_lower or "grand total" in line_lower:
            extracted_data["Total Amount"] = "".join(filter(str.isdigit, line))
        elif "sub-total" in line_lower or "amount before tax" in line_lower:
            extracted_data["Base Amount"] = "".join(filter(str.isdigit, line))
        elif "tax" in line_lower or "gst" in line_lower or "vat" in line_lower:
            extracted_data["Tax Amount"] = "".join(filter(str.isdigit, line))
        elif "from" in line_lower or "seller" in line_lower:
            extracted_data["Sender"] = line
        elif "to" in line_lower or "buyer" in line_lower:
            extracted_data["Recipient"] = line

    return extracted_data

def save_to_excel(data, output_path):
    df = pd.DataFrame([data])
    df.to_excel(output_path, index=False)

@app.route("/")
def upload_page():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_invoice():
    if "invoice" not in request.files:
        return "No file uploaded", 400
    
    file = request.files["invoice"]
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    if filename.endswith(".pdf"):
        images = convert_from_path(file_path)
        image_path = os.path.join(UPLOAD_FOLDER, "converted.png")
        images[0].save(image_path, "PNG")
    else:
        image_path = file_path

    
    extracted_text = extract_text(image_path)
    invoice_data = map_invoice_fields(extracted_text)

    output_excel = os.path.join(UPLOAD_FOLDER, "output.xlsx")
    save_to_excel(invoice_data, output_excel)

    return send_file(output_excel, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
