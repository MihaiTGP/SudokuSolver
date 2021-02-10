import pygame, sys
from SudokuSolver import solve_sudoku, string_to_integer, integer_to_string, is_valid #Importing from SudokuSolver
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
#The only keys
VALID_KEYS = [pygame.K_1, pygame.K_2, pygame.K_3,
              pygame.K_4, pygame.K_5, pygame.K_6,
              pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_TAB]
dest = (0, 0)
GRIDSIZE = 100
GRID_WIDTH = WIDTH // GRIDSIZE
GRID_HEIGHT = HEIGHT // GRIDSIZE

base_font = pygame.font.Font(None, 70)
#Drawing the 4 lines that make the 3x3 squares
def draw_lines():
    line1 = pygame.Rect(295, 0, 10, 900)  # horizontal 1
    line2 = pygame.Rect(595, 0, 10, 900)   # horizontal 2
    line3 = pygame.Rect(0, 295, 900, 10)  # vertical 1
    line4 = pygame.Rect(0, 595, 900, 10)  # vertical 2

    pygame.draw.rect(WIN, BLACK, line1)
    pygame.draw.rect(WIN, BLACK, line2)
    pygame.draw.rect(WIN, BLACK, line3)
    pygame.draw.rect(WIN, BLACK, line4)
#Drawing the grid(9x9 squares)
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


selected_cell = None
#The main function
def main():
    global grid, selected_cell
    run = True
    solved = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #Checking for user clicks
            if event.type == pygame.MOUSEBUTTONDOWN and solved == False:
                pos = pygame.mouse.get_pos()
                col = pos[0] // GRIDSIZE
                row = pos[1] // GRIDSIZE
                selected_cell = [col, row]

            #Checking for keys pressed
            if event.type == pygame.KEYDOWN and event.key in VALID_KEYS: #The key can only be 1,2,3..9 or TAB
                if event.key == pygame.K_TAB: #If the key is TAB solve the puzzle
                    string_to_integer(grid)
                    solve_sudoku(grid)
                    integer_to_string(grid)
                    solved = True  #And don't let the user change the grid anymore

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
