from functools import reduce
def print_board(sudoku_grid:list) -> None:
    """
    Simply prints the board with a given a sudoku grid.

    sudoku_grid (list): a 2d list of dimensions 9x9  representing a sudoku grid

    """

    col_index = "  " + reduce(lambda a, b: a + b, [f"\033[0;{31+(i%5)}m{i}   " for i in range(9)]) + "\n"

    top = "\033[0;31m╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗\033[0m\n"
    middle_normal = "\033[0;31m╟\033[0;32m━━━┿━━━┿━━━\033[0;31m╫\033[0;32m━━━┿━━━┿━━━\033[0;31m╫\033[0;32m━━━┿━━━┿━━━\033[0;31m╢\033[0m\n"
    middle_bold = "\033[0;31m╠═══╪═══╪═══╫═══╪═══╪═══╫═══╪═══╪═══╣\033[0m\n"
    bottom = "\033[0;31m╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝\033[0m\n"

    # i sure do hope these are only pointers... otherwise rip memory (altho modern computers OP)
    x_grid_list = [
        middle_normal,
        middle_normal,
        middle_bold,
        middle_normal,
        middle_normal,
        middle_bold,
        middle_normal,
        middle_normal,
        bottom,
    ]
    grid = col_index + top
    for i, rows in enumerate(sudoku_grid):
        grid += "\033[0;31m║\033[0;32m {} ┃ {} ┃ {} \033[0;31m║\033[0;32m {} ┃ {} ┃ {} \033[0;31m║\033[0;32m {} ┃ {} ┃ {} \033[0;31m║\033[0m \033[0;{}m{}\n".format(*[f"\033[0m{cell}\033[0;32m" for cell in rows], 31+(i%5), i) + x_grid_list[i]
    print(grid)
    

#    f"""
# ┏━┳━┳━╥━┳━┳━╥━┳━┳━┓
# ┃ ┃ ┃ ║ ┃ ┃ ║ ┃ ┃ ┃
# ┣━┿━┿━╫━┿━┿━╫━┿━┿━┫
# ┃ ┃ ┃ ║ ┃ ┃ ║ ┃ ┃ ┃
# ╠═╬═╬═╬═╬═╬═╬═╬═╬═╣

# ╚═╩═╩═╩═╩═╩═╩═╩═╩═╝
# ┏━┳━┳━╥━┳━┳━╥━┳━┳━┓
#    """
def show_help():
    help_text = """
📘 SUDOKU GAME HELP

🔢 WHAT IS SUDOKU?
Sudoku is a logic-based number puzzle. The game board is a 9x9 grid divided into nine 3x3 boxes.

🎯 GOAL:
Fill the grid so that:
- Each ROW contains numbers 1 to 9 with no repeats.
- Each COLUMN contains numbers 1 to 9 with no repeats.
- Each 3x3 BOX contains numbers 1 to 9 with no repeats.

🕹️ HOW TO PLAY:
- Use logic to figure out where each number goes.
- You can’t repeat numbers in any row, column, or box.
- Start with the given clues and build from there.

💡 TIPS:
- Look for rows, columns, or boxes that are almost full.
- Use process of elimination.
- No guessing — it's all about logic.

Type 'help' to see this message again.
"""
    print(help_text)

def double_check(sudoku_grid:list):
    """
    asks the user to enter a command.
    command list:
    - help: print the command list, give more info
    - ok: exit out of the function
    - replace x y n: replace the number in that given cell
    """    
    while True:
        print_board(grid) 
        print('Please recheck your sudoku board:')
        print('-help')
        print('-ok')
        print('-replace <x> <y> <n>')
        user_input = input("input a command: ").strip().lower()

        if user_input == "ok":
            print("✅ Final board accepted.")
            break
        elif user_input == "help":
            show_help()
        elif user_input.startswith("replace"):
            try:
                parts = user_input.split()
                x, y, n = map(int, parts[1:])
                if 0 <= x < 9 and 0 <= y < 9 and 0 <= n <= 9:
                    grid[y][x] = n  # update value
                else:
                    print("Invalid values")
            except:
                print("Format: replace x y n")
        else:
            print("Unknown command")


        # user_input == "replace x y n".split()
        # grid[y][x] = n
        # print(sudoku_grid)
if __name__ == "__main__":
    grid = [[5, 3, 4, 6, 7, 8, 1, 9, 2],
            [6, 7, 2, 1, 9, 5, 4, 3, 8],
            [1, 9, 8, 3, 4, 2, 6, 5, 7],
            [8, 1, 9, 7, 6, 4, 5, 2, 3],
            [4, 2, 6, 8, 5, 3, 9, 7, 1],
            [7, 5, 3, 9, 2, 1, 8, 4, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 3, 6, 5],
            [3, 4, 5, 2, 8, 6, 7, 1, 9]]
    double_check(grid)
