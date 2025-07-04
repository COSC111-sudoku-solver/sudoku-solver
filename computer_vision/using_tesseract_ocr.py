import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

back_to_505 = "./images/shakesphere_text.png"
# digit = "./output/sudoku_grids/1-1.png"

img = cv2.imread(back_to_505)
# 
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 
# thresh = cv2.adaptiveThreshold(gray, 255,
#                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                cv2.THRESH_BINARY_INV,
#                                11, 2)

cv2.imshow("my image", img)

cv2.waitKey(0)
text = pytesseract.image_to_string(img, 
                   # config='--psm 10 -c tessedit_char_whitelist=0123456789',
                   lang='eng')
print(text)
