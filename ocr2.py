import easyocr
import sys


def getText(image):
    reader = easyocr.Reader(["en"])
    # reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(image)
    # result = reader.readtext(IMAGE_PATH, paragraph="False")
    print(result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_path = sys.argv[1]
    else:
        img_path = "sample.jpg"
    getText(img_path)
