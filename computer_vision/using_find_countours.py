import cv2 as cv
import time

img = cv.imread(
    "./images/sudoku.png"
)

# graying the image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# converting it to black and white (binary)
thresh = cv.adaptiveThreshold(gray, 255,
                      cv.ADAPTIVE_THRESH_MEAN_C,
                      cv.THRESH_BINARY_INV,         
                      11,                       
                      2)    

# finding the contours
contours, hierarchy  = cv.findContours(thresh,
                        cv.RETR_TREE,
                        cv.CHAIN_APPROX_SIMPLE)

filtered_contours = []
surrounding_contour = max(contours, key=cv.contourArea)
for contour in contours:
    # filter out all the numbers 
    area = cv.contourArea(contour)
    if area < 1000 or (cv.contourArea(surrounding_contour) == area):
        continue
    x, y, w, h = cv.boundingRect(contour)
    aspect_ratio = w/float(h)

    if 0.8 < aspect_ratio < 1.2:
        filtered_contours.append(contour)

print(len(filtered_contours))

cv.drawContours(img, filtered_contours, -1, (0, 255, 0), 2)
cv.imshow("Contours", img)
cv.waitKey(0)

cv.destroyAllWindows()
