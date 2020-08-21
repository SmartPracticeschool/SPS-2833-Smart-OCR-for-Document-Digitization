from __future__ import division, print_function

import os
import random

import pytesseract
from PIL import Image
from flask import Flask, request, render_template
from pdf2image import convert_from_path
from werkzeug.utils import secure_filename

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


app = Flask(__name__, static_url_path='')

@app.route('/predict' , methods=['GET', 'POST'])
def upload():
    global file_path2
    if request.method == 'POST':
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads',  secure_filename(f.filename))
        f.save(file_path)
        PDF_file = file_path
        pages = convert_from_path(PDF_file, 500)
        image_counter = 1
        for page in pages:
            filename = "page_"+str(image_counter)+".jpg"
            page.save(filename, "JPEG")
            image_counter = image_counter + 1
        file_limit = image_counter -1
        # Create a text file to write the output
        basepath = os.path.dirname(__file__)
        file_path2 = os.path.join(
            basepath, 'outputs', "output"+str(random.randint(1, 100000))+".txt")
        f = open(file_path2, "a")
        for i in range(1, file_limit +1):
            filename = "page_"+str(i)+".jpg"
            text = str(((pytesseract.image_to_string(Image.open(filename)))))
            text = text.replace('-\n', '')
            f.write(text)
        f.close()
    return file_path2

@app.route('/')
def index():
    return render_template('base.html')
