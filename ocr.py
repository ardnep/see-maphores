# Import modules
from PIL import Image
import pytesseract
import sys


def getText(image):
    pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
    image = Image.open(image)
    text = pytesseract.image_to_string(image, lang="eng")
    print(text)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_path = sys.argv[1]
    else:
        img_path = "sample.jpg"
    getText(img_path)
