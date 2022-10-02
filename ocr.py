import pytesseract
import sys
from PIL import Image

from translate_tts import tts


def getText(image):
    pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"
    image = Image.open(image)
    text = pytesseract.image_to_string(image, lang="eng")
    tts(text, 1)


if __name__ == "__main__":
    while True:
        getText('yolov5/img.jpg')
