from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/sbin/tesseract"

img = Image.open("./images/just_505.png")

text = pytesseract.image_to_string(img, lang='eng')

print(text)
