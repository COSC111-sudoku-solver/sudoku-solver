import csv
import numpy as np
import copy
import sudoku_utils

def read_sudoku_csv(file_path:str)->list:
    """
    reads a sudoku puzzle stored as a CSV file

    file_path (str): path to the csv file

    return: 2d list representing a sudoku grid
    """
    sudoku_puzzle = []
    with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # converting the numbers from string to int
                sudoku_puzzle.append([int(n) if n != '' else 0 for n in row])
    return sudoku_puzzle
    

def is_possible(sudoku_puzzle:list, x:int, y:int, n:int)->bool:
    """
    Checks whether its possible to place a digit, n at coordinates x, y

    sudoku_puzzle (list): a 2d list of integers representing a sudoku puzzle (9x9)

    x (int): coordinates of the x axis from 0 to 8 

    y (int): coordinates of the y axis from 0 to 8

    n (int): a digit to place at coordinate (x, y)

    return: a boolean that states whether it's possible to put that value n at coordinates x, y
    """
    
    # first check for rows
    fits_rows = not (n in sudoku_puzzle[y])
    # then checks for columns
    fits_columns = not (n in [row[x] for row in sudoku_puzzle])

    # finally, check for squares
    
    # first dividing the grid to 3x3 squares
    x_square = x//3
    y_square = y//3
    
    fits_squares = not (n in [sudoku_puzzle[y_in_square][x_in_square] for x_in_square in range(x_square*3, (x_square+1)*3) for y_in_square in range(y_square*3, (y_square+1)*3)])
    
    return fits_rows and fits_columns and fits_squares

# def solve_sudoku(sudoku_puzzle:list, x:int=0, y:int=0) -> bool:
#     """
#     sudoku_puzzle (list): passing a pointer to a list that's outside the scope of the function. This program will search left to right, top to down.
# 
#     x (int): the x coordinates
# 
#     y (int): the y coordinates
# 
#     return: a bool representing whether the path is value or invalid
#     """
# 
#     if y == 9:
#         # if this program has reached the end. 
#         # since the scope of x and y is from 0 to 8, if it reaches 9, then we're done
#         return True
#     # what a nesting mess...
#     elif x == 9:
#         # if we've reached the end of the row, drop down by one
#         return solve_sudoku(sudoku_puzzle, 0, y+1)
#     elif sudoku_puzzle[y][x] != 0:
#         # now if we're our isn't actually replacable, then go on to the next
#         return solve_sudoku(sudoku_puzzle, x+1, y)
#     else:
#         # now if our x, y coordinates have a 0, try to replace it from 1 to 9
#         for k in range(1, 10):
#             if is_possible(sudoku_puzzle, x, y, k):
#                 # if k is possible replace the value at that coordinates with k
#                 sudoku_puzzle[y][x] = k
#                 # now see if we can actually try solve it given that our value of k is of such.
# 
#                 # move on and assume that our k is valid
#                 if solve_sudoku(sudoku_puzzle, x+1, y):
#                     return True
#                 else:
#                     # if the puzzle isn't solved yet, backtrack and try to replace k again
#                     
#                     sudoku_puzzle[y][x] = 0
#         # if we've looped through, we know we didn't return True
#         return False


def solve_sudoku(sudoku_puzzle:list, solutions_list:list) -> None:
    """
    solves the sudoku puzzle and returns the list of all possible solutions

    sudoku_puzzle (list) 2d list representing a sudoku grid

    solution_list (list) a list of 2d list that 'collects' the solution
    """

    # first loop through the sudoku grid

    for y in range(9):
        for x in range(9):
            if sudoku_puzzle[y][x] != 0:
                # i kinda hate 'continue' and 'break' but no thanks to nesting hell...
                continue
            for n in range(1, 10):
                # try to continue with n as the solution
                if not is_possible(sudoku_puzzle, x, y, n):
                    continue 
                sudoku_puzzle[y][x] = n
                solve_sudoku(sudoku_puzzle, solutions_list)
                # but now we've traveled crossed dimensions and came back here
                # but now we know... and so, backtracking...
                sudoku_puzzle[y][x] = 0
                
                # now it'll go from left to right with no problems until it reaches this y,x and tries the same thing...
                # but let's just say it has looped through DEEP into the sudoku grid and found out, it can't continue (how???)
            # well, we can say that if it's out of the loop, we've reached a dead end
            # so gotta return...
            return
    solutions_list.append(copy.deepcopy(sudoku_puzzle))



if __name__ == "__main__":
    puzzle = read_sudoku_csv("./sudoku_puzzle.csv")
    
    # want to duplicate it such that we have one puzzle, and one solution.
    solved_sudoku = copy.deepcopy(puzzle)

    solved_sudoku = []
    solve_sudoku(puzzle, solved_sudoku)    

    print("Puzzle: ")
    print(np.matrix(puzzle))

    print("Solution: ")
    print([np.matrix(sol) for sol in solved_sudoku])
    
    
