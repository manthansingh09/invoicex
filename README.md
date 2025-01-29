# InvoiceX
## 📌 Overview
This project is a **Flask-based web application** that extracts data from invoices using **OCR and NLP**, maps the extracted text to structured fields, and exports the results into an **Excel file**.

## 🚀 Features
✔ **Upload Invoice (PDF/Image)**  
✔ **Extract Key Fields Automatically**  
✔ **Save Data in Structured Excel Format**  
✔ **OCR-Based Text Extraction**  
✔ **Supports Different Invoice Formats**  

## 🛠️ Tech Stack
- **Python** (Flask, Pandas, OpenCV, spaCy)
- **Tesseract OCR** (Text Extraction)
- **PDF2Image** (PDF to Image Conversion)
- **Excel Processing** (OpenPyXL)

## 🔧 Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/invoice-extraction.git
cd invoice-extraction
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Install Tesseract OCR
- **Windows:** Download from [here](https://github.com/UB-Mannheim/tesseract/wiki).
- **Linux/macOS:** Install using:
  ```bash
  sudo apt install tesseract-ocr  # Ubuntu/Debian
  brew install tesseract  # macOS
  ```

### 4️⃣ Run the App
```bash
python app.py
```
Visit **`http://127.0.0.1:5000/`** in your browser.

## 📂 Project Structure
```
invoice-extraction/
│── templates/           # HTML files
│   ├── index.html
│── app.py               # Main Flask app
│── requirements.txt      # Dependencies
│── README.md            # Project Documentation
```

## 📊 How It Works
1. **Upload an Invoice (PDF or Image)**  
2. **OCR extracts text from the document**  
3. **NLP detects key invoice fields (Total, Tax, etc.)**  
4. **Data is mapped & exported to an Excel file**  

## 🎯 Next Steps
🔹 **Improve Field Detection with AI Models**  
🔹 **Enhance Multi-Language Support**  
🔹 **Deploy on Cloud (AWS, GCP, etc.)**  

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

## 📜 License
This project is licensed under the **MIT License**.
