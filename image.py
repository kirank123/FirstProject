import numpy as np
import pytesseract
import cv2
import time
from PIL import ImageGrab


def imToString():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    while True:
        cap = ImageGrab.grab(bbox=(100, 200, 610, 410))
        tesstr = pytesseract.image_to_string(cv2.cvtColor(np.array(cap), cv2.COLOR_BGR2GRAY), lang='eng')
        print(tesstr)
        time.sleep(1)


imToString()
