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
