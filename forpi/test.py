#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import requests
import json 
import urllib.request
import os
import stat

image_file1 = "/home/matrix/rpi-rgb-led-matrix/jonas/image.png"
image_file2 = "/home/matrix/rpi-rgb-led-matrix/jonas/image2.png"
try:
    print("Press CTRL-C to stop.")
    
    # Configuration for the matrix
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
    matrix = RGBMatrix(options=options)

    while True:
        time.sleep(5)
        res = requests.get('http://192.168.178.21:9999/get-image')
        url = res.json()['image']
        print(url)

        if os.path.isfile(image_file1):
            with open(image_file2, 'wb') as f:
                f.write(requests.get(url).content)
            image = Image.open(image_file2)
            with open(image_file1, 'wb') as f:
                f.write(b"")  # Leeren Sie die Datei
            os.chmod(image_file1, 0o777)
            os.remove(image_file1)
        else:
            with open(image_file1, 'wb') as f:
                f.write(requests.get(url).content)
            image = Image.open(image_file1)
            with open(image_file2, 'wb') as f:
                f.write(b"")  # Leeren Sie die Datei
            os.chmod(image_file2, 0o777)
            os.remove(image_file2)

        # Make image fit our screen.
        image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

        matrix.SetImage(image.convert('RGB'))

except KeyboardInterrupt:
    sys.exit(0)