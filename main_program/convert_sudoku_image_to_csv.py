import cv2
import pytesseract
import sys
import numpy

def load_and_prepare_image(path_to_image:str)->np.ndarray:
    """
    first loads the image, then continue to prepare it for further manipulation

    path_to_image (str): the relative path to the sudoku image

    return: opencv image (NumPy array)
    """
    img = cv2.imread(path_to_image)

    # converts it to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # converts it to black and white
    thresh = cv2.adaptiveThreshold(gray,
                            255, # make the background white to the highest intensity 
                            cv2.ADAPTIVE_THRESH_MEAN_C, # not sure what the rest of these does...
                            cv2.THRESH_BINARY_INV,
                            11,
                            2) 
    return thresh
        
    
def crop_image(uncropped_img):
    """
    Crops the image based on the surrouding, external bounding box

    uncropped_img (NumPy array for opencv images): uncropped image of the sudoku grid

    return: opencv image 
    """
    # first find the external contours of the image

    surrounding_contour, _ = cv2.findContours(uncropped_img,
                                cv2.RETR_EXTERNAL,# only return the external contour
                                cv2.CHAIN_APPROX_SIMPLE) # probably some algorithm to find contour
    # surrounding contour should only of length one
    if len(surrounding_contour) == 1:
        # gets the bounding rectangle of the surrounding borders
        x, y, w, h = cv2.boundingRect(surrounding_contour)

        # crop the image
        # this syntax just says, get the pixel from y until y + h, from x until x + w
        cropped_image = img[y:y+h, x:x+h]

        return cropped_image        
        
    else:
        sys.exit("Please take another picture! The external borders aren't clear enough")
                

def get_cells(sudoku_img):
    pass
