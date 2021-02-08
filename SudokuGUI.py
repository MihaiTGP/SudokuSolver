import pygame, sys
from SudokuSolver import solve_sudoku, string_to_integer, integer_to_string #Importing from SudokuSolver
pygame.init()
#The sudoku gird
grid = [
    ["","","","","","","","",""],
    ["","","","","","","","",""],
    ["","","","","","","","",""],
    ["","","","","","","","",""],
    ["","","","","","","","",""],
    ["","","","","","","","",""],
    ["","","","","","","","",""],
    ["","","","","","","","",""],
    ["","","","","","","","",""]
]
#CONSTANTS
WIDTH = 900
HEIGHT = 900
BLACK = (0, 0, 0)
WIN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Sudoku Solver")

dest = (0, 0)
GRIDSIZE = 100
GRID_WIDTH = WIDTH // GRIDSIZE
GRID_HEIGHT = HEIGHT // GRIDSIZE

base_font = pygame.font.Font(None, 70)
#Drawing the 4 lines that make the 3x3 squares
def draw_lines():
    B1 = pygame.Rect(295, 0, 10, 900)  # horizontal 1
    B2 = pygame.Rect(595, 0, 10, 900)   # horizontal 2
    B3 = pygame.Rect(0, 295, 900, 10)  # vertical 1
    B4 = pygame.Rect(0, 595, 900, 10)  # vertical 2

    pygame.draw.rect(WIN, BLACK, B1)
    pygame.draw.rect(WIN, BLACK, B2)
    pygame.draw.rect(WIN, BLACK, B3)
    pygame.draw.rect(WIN, BLACK, B4)
#Drawing the grid(9x9)
def draw_grid():
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(WIN, (150, 150, 150), r)
            else:
                rr = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(WIN, (255, 255, 255), rr)


#Drawing the grid(numbers)
def draw_numbers(grid):
    surf = pygame.Surface(WIN.get_size(), pygame.SRCALPHA).convert_alpha() # creates a clear surface
    r = 0
    for row in grid:
        c = 0
        for cell in row:
            text_surface = base_font.render(cell, True, BLACK).convert_alpha()
            surf.blit(text_surface, (c*GRIDSIZE + 35,r*GRIDSIZE + 30))
            c+=1
        r+=1

    WIN.blit(surf, (0,0))



#Drawing the completed sudoku
def solved_sudoku(grid):
    solve_sudoku(grid)
    integer_to_string(grid)
    draw_grid()
    draw_lines()
    draw_numbers(grid)

selected_cell = None
#The main function
def main():
    run = True
    global grid, selected_cell
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #Checking for user clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // GRIDSIZE
                row = pos[1] // GRIDSIZE
                selected_cell = [col, row]

            #Checking for keys pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB: #If the key is TAB solve the puzzle
                    string_to_integer(grid)
                    solved_sudoku(grid)

                elif selected_cell != None: #Else add to the grid that number
                    user_text = event.unicode
                    grid[selected_cell[1]][selected_cell[0]] = user_text
                    selected_cell = None


        #Drawing everthing and updating the display
        draw_grid()
        draw_lines()
        draw_numbers(grid)
        pygame.display.update()


if __name__ == '__main__':
    main()
