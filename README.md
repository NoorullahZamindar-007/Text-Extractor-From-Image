# Text-Extractor-From-Image
Text Extractor using Flask, OpenCV, Numpy, PIL, pytesseract, re 

---

### ✅ `README.md`

markdown
# 🧠 OCR Flask App

A simple and modern web application built with **Flask** that performs **Optical Character Recognition (OCR)** on uploaded images using **Tesseract OCR**. Upload an image, extract text, and display the results — all from your browser.

---
 
## 🚀 Features

- 📸 Upload any image with text
- 🔍 Extract readable text using Tesseract OCR
- 🌐 Built with Flask and Python
- 💡 Clean, responsive web UI
- 📦 Lightweight and easy to set up

---

## 📸 Demo

![OCR Flask App Screenshot](/static/uploads/2.png) <!-- Optional: replace with your own screenshot -->

--- 

## 📁 Project Structure


ocr-flask-app/

├── app.py

├── templates/

│   └── index.html

├── static/

│   └── uploads/

├── requirements.txt

└── README.md



---

## ⚙️ Installation & Setup

### 1. Clone the repo

bash
git clone https://github.com/NoorullahZamindar-007/Text-Extractor-From-Image
cd ocr-flask-app


### 2. Create a virtual environment (optional but recommended)

bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux


### 3. Install dependencies

bash
pip install -r requirements.txt


### 4. Install Tesseract OCR

- Download from: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- Recommended for Windows: [UB Mannheim Build](https://github.com/UB-Mannheim/tesseract/wiki)
- After installation, update the Tesseract path in `app.py` if needed:
python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


---

## 🧪 Run the App

bash
python app.py


Visit: `http://127.0.0.1:5000` in your browser.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Norullah Zamindar**  
Data Scientest | Developer | AI Enthusiast  
[LinkedIn](https://www.linkedin.com/in/noorullah-zamindar-4975a328a/) • [GitHub](https://github.com/NoorullahZamindar-007)

---

## ⭐️ Show Your Support

If you like this project, please ⭐️ the repo to support the author and share with others!



---

### 📝 Notes

- If you face with any issues please contact us using uper info 
