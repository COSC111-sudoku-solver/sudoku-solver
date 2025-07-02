import cv2 as cv

img = cv.imread("./images/sudoku.png", cv.IMREAD_GRAYSCALE)

# Apply adaptive thresholding
# I guess to make sure all the grids are of the same brightness?
thresh = cv.adaptiveThreshold(img, 255,
                               cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv.THRESH_BINARY,
                               blockSize=11,
                               C=5)

# regular thresholding
# thresh = cv.threshold(img, 255, 127, cv.THRESH_BINARY)


cv.imshow("image", thresh)
cv.waitKey(0)
cv.destroyAllWindows()
