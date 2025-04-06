from flask import Flask, render_template, request
import os
import pytesseract
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = ""
    image_filename = None
    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename != '':
            image_filename = file.filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
            file.save(image_path)
            img = Image.open(image_path)
            extracted_text = pytesseract.image_to_string(img)
    return render_template('index.html', text=extracted_text, image=image_filename)

if __name__ == '__main__':
    app.run(debug=True)
