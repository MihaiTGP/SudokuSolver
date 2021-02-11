def find_next_empty(grid):
    #As the name suggests this will find the next ''
    for row in range(9):
        for col in range(9):
            if grid[row][col] == '':
                return row, col
    #If it can't find '' that means the puzzle is solved/almost solved and so doesn't return a row and a col
    return None, None
#This function is checking to see if our numbers respect the rules of the game
def is_valid(grid, guess, row, col):
    row_vals = grid[row]
    col_vals = [grid[i][col] for i in range(9)]
    #Checking the rows and the columns
    if guess in row_vals or guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    #Checking the 3x3 squares
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if grid[r][c] == guess:
                return False
    #If it respects all of the rules it's a good move
    return True

def solve_sudoku(grid):
    #This is the function where we actually solve sudoku
    row, col = find_next_empty(grid)
    #If there aren't any more numbers that means we solved the puzzle
    if row is None:
        return True
    #If there are '' in the grid
    for guess in range(1, 10):
        if is_valid(grid, guess, row, col): #It check's if the number is valid
            grid[row][col] = guess #If it is set it as the number
            if solve_sudoku(grid): #This is a backtracking function so it calls itself
                return True
        #If the numer isn't valid then we set it back to ''
        grid[row][col] = ''
    #If there is no possible solution, return False
    return False
#This function is to transform the grid so the text_surface doesn't throw an error
def string_to_integer(grid): #First we change all of the elements on the grid into integers, so solve_sudoku() can work
    for row in range(9):
        for col in range(9):
            if grid[row][col] != '':
                grid[row][col] = int(grid[row][col])

def integer_to_string(grid): #Then we change all of the numbers on the grid into strings, so text_surface works
    for row in range(9):
        for col in range(9):
            grid[row][col] = str(grid[row][col])

