import cv2 as cv

img = cv.imread("./images/kirby.png")

converted_color = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# gaussian blur with 3x3 kernel
gaussian_blurred = cv.GaussianBlur(img, (11, 11), sigmaX = 10, sigmaY=0.5)


cv.imshow("image", gaussian_blurred)
cv.waitKey(0)
cv.destroyAllWindows()
