import cv2 as cv
import time

img = cv.imread(
    "./images/sudoku_not_cropped.png"
)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

thresh = cv.adaptiveThreshold(gray, 255,
                      cv.ADAPTIVE_THRESH_MEAN_C,
                      cv.THRESH_BINARY_INV,         
                      11,                       
                      2)    

surrounding_contour, _ = cv.findContours(thresh,
                        cv.RETR_EXTERNAL,
                        cv.CHAIN_APPROX_SIMPLE)

# should only be of length 1
print(len(surrounding_contour))
surrounding_contour = surrounding_contour[0]

# cropping the image based on the surrounding external contour
x, y, w, h = cv.boundingRect(surrounding_contour)
# honestly, i still can't understand how the index of a list can be a tuple or whatever...
cropped_image = img[y:y+h, x:x+h]

# height, width and number of channels
cropped_image_height, cropped_image_width = cropped_image.shape[:2]
cv.imshow(f"Cropped Image: {cropped_image_height}, {cropped_image_width}", cropped_image)
cv.waitKey(0)


# now finding contours again



cv.destroyAllWindows()
