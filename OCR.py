from random import random

import numpy as np
import cv2
from PIL import Image
import pytesseract  # extract the text
import sys
from pdf2image import convert_from_path  # to convert pdf to images
import os
import random

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pages = convert_from_path('sample.pdf', 500)
# Counter to store images of each page of PDF to image
image_counter = 1
for page in pages:
    # Declaring filename for each page of pdf as jpg
    # For each page ,filename will be:
    # PDF page 1 -> page_1.jpg
    # PDF page 2 -> page_2.jpg
    # PDF page 3 -> page_3.jpg
    filename = "page_"+str(image_counter)+".jpg"
    # Save the image of the page in system
    page.save(filename, 'JPEG')
    image_counter = image_counter + 1

    # Variable to get count of total number of images
    filelimit = image_counter-1

    basepath = os.path.dirname(__file__)
    file_path2 = os.path.join(
        basepath, 'outputs', "output"+str(random.randint(1, 100000))
    )

    f = open(file_path2, "a")

    for i in range(1, filelimit + 1):
        filename = "page_"+str(i)+".jpg"
        text = str(((pytesseract.image_to_string(Image.open(filename)))))
        f.write(text)

    f.close()

