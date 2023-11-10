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

image_file = ""

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(5)
        res = requests.get('http://192.168.178.21:9999/get-image')
        url = res.json()['image']
        print(url)
        if os.path.isfile("./image.png") == True:
            urllib.request.urlretrieve(url, "./image2.png") 
            image_file = "./image2.png"
            image = Image.open(image_file)

            # Configuration for the matrix
            options = RGBMatrixOptions()
            options.rows = 32
            options.cols = 64
            options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

            matrix = RGBMatrix(options = options)

            # Make image fit our screen.
            image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

            matrix.SetImage(image.convert('RGB'))
            os.chmod("./image.png",stat.S_IWOTH)
            os.remove("./image.png")
        else:
            urllib.request.urlretrieve(url, "./image.png") 
            image_file = "./image.png"
            image = Image.open(image_file)

            # Configuration for the matrix
            options = RGBMatrixOptions()
            options.rows = 32
            options.cols = 64
            options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

            matrix = RGBMatrix(options = options)

            # Make image fit our screen.
            image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

            matrix.SetImage(image.convert('RGB'))
            os.chmod("./image2.png",stat.S_IWOTH)
            os.remove("./image2.png")
except KeyboardInterrupt:
    sys.exit(0)