# TODO
- [] Converting image of sudoku to CSV file
- [] Fully understand backtracking algorithm, implement my own version with the generation of other solutions (if possible)
- [] Coloring Text in terminal
- [] Creating an animation

# Useful Links
- [printable Sudoku](https://sudoku.com/sudoku-printable)
- [blog post about the project](https://encord.com/blog/sudoku-solver-cv-project/)
- [similar GitHub project](https://github.com/Aryann15/SUDOKU_SOLVER)

# Image -> Grid of Sudoku Logic

| **Step** | **Method / Function**                | **Purpose**                               | **Inputs**                        | **Outputs**             | **Notes**                                          |
| -------- | ------------------------------------ | ----------------------------------------- | --------------------------------- | ----------------------- | -------------------------------------------------- |
| 1        | `cv2.imread()`                       | Load the Sudoku image                     | File path (str)                   | Image (NumPy array)     | Supports various formats (jpg, png, etc.)          |
| 2        | `cv2.cvtColor()`                     | Convert image to grayscale                | Color image                       | Grayscale image         | Use `cv2.COLOR_BGR2GRAY`                           |
| 2        | `cv2.GaussianBlur()`                 | Smooth image to reduce noise              | Grayscale image, kernel size      | Blurred image           | Kernel usually `(5, 5)`                            |
| 2        | `cv2.adaptiveThreshold()`            | Convert image to binary (black and white) | Blurred image + parameters        | Thresholded image       | `ADAPTIVE_THRESH_GAUSSIAN_C` + `THRESH_BINARY_INV` |
| 3        | `cv2.findContours()`                 | Find contours (edges) in binary image     | Thresholded image                 | List of contours        | Use `RETR_EXTERNAL` for outer edges                |
| 3        | `max(contours, key=cv2.contourArea)` | Find largest contour (likely grid)        | List of contours                  | Single contour          | Assumes the grid is the largest area               |
| 3        | `cv2.approxPolyDP()` *(optional)*    | Approximate the contour to 4 points       | Contour + epsilon                 | Approximated polygon    | Ensures square corners                             |
| 3        | `cv2.getPerspectiveTransform()`      | Get transform matrix for warping          | Source points, destination points | 3x3 perspective matrix  | Needs 4 corner points                              |
| 3        | `cv2.warpPerspective()`              | Apply perspective warp                    | Image + transform matrix + size   | Warped (top-down) image | Extracts flat view of grid                         |
| 4        | *(custom loop logic)*                | Split grid into 81 cells                  | Warped image, grid size           | List of 81 cell images  | Uses slicing with NumPy                            |
| 5        | `cv2.threshold()`                    | Binarize each cell for OCR                | Cell image + threshold type       | Thresholded cell        | Good for isolating digits                          |
| 5        | `pytesseract.image_to_string()`      | Recognize digit in each cell              | Cell image + config               | String (digit or empty) | Use `--psm 10` for single character                |
| 6        | `int()` + `str.strip()`              | Convert OCR output to number              | String digit                      | Integer or 0            | Handle empty/invalid OCR results                   |
| 6        | `np.array().reshape()`               | Create 9×9 grid                           | Flat list of 81 ints              | 9×9 NumPy array         | Validates number count                             |
| 7        | `pd.DataFrame()`                     | Create DataFrame from array               | 2D list/array                     | Pandas DataFrame        | Easy CSV export                                    |
| 7        | `df.to_csv()`                        | Save grid as CSV file                     | DataFrame, file name              | CSV file                | Set `index=False`, `header=False`                  |

