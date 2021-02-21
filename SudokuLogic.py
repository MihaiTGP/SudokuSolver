#importing the necesary modules
import random
import numpy as np
from dokusan import generators
grid = [
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""]
]

def find_next_empty(grid):
    """this function finds the next empty cell """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == "":
                return row, col
        # if it can't find empty cells the puzzle is solved and doesn't return a row and a col
    return None, None

def is_valid(grid, guess, row, col):
    """checks if the guess respects the rules of the game"""
    row_vals = grid[row]
    col_vals = [grid[i][col] for i in range(9)]
    # checking the rows and the columns
    if guess in row_vals or guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    # checking the 3x3 squares
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if grid[r][c] == guess:
                return False
    # if it respects all of the rules it's a good guess
    return True

def solve_sudoku(grid):
    # this is the function where we actually solve sudoku
    row, col = find_next_empty(grid)
    # if there aren't any more blank spaces that means we solved the puzzle
    if row is None:
        return True
    # if there are blank spaces in the grid
    for guess in range(1, 10):
        if is_valid(grid, guess, row, col): # it checks if the number is valid
            grid[row][col] = guess # if it is set it as the number
            if solve_sudoku(grid): # this is a backtracking function so it calls itself
                return True
        # if the numer isn't valid then we set it back to a blank space
        grid[row][col] = ''
    # if there is no possible solution, return False
    return False

def string_to_integer(grid):
    """transforms all the elements in the grid to integers"""
    for row in range(9):
        for col in range(9):
            if grid[row][col] != '':
                grid[row][col] = int(grid[row][col])

def integer_to_string(grid):
    """transforms all the elements in the grid back to strings"""
    for row in range(9):
        for col in range(9):
            grid[row][col] = str(grid[row][col])

def reset_grid(grid):
    """ Transforms all the elements inside the grid to blank spaces"""
    for row in range(9):
        for col in range(9):
            grid[row][col] = ""


def add_numbers(grid):
    """ Adds the numbers to the grid, between 26-32 """
    array = []
    arr = np.array(list(str(generators.random_sudoku(avg_rank=150))))
    array = arr.reshape(9, 9)
    for row in range(9):
        for col in range(9):
            if array[row][col] == '0':
                grid[row][col] = ""
            else:
                grid[row][col] = array[row][col]

    return array

def check_win(grid):
    """Checks if the user has won"""
    for row in range(9):
        if ''  in grid[row]:
            return  False

    return True
