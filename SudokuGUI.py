import pygame, sys
from SudokuLogic import solve_sudoku, string_to_integer, integer_to_string, is_valid, reset_grid, add_numbers, check_win  # importing from SudokuSolver
import time, math
# the sudoku grid
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
# CONSTANTS
WIN_WIDTH = 802
WIN_HEIGHT = 702
WIDTH = 702 #The sudoku witdh
HEIGHT = 702 #The sudoku height
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
# initialize the game
pygame.init()
WIN = pygame.display.set_mode((WIN_WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Sudoku")

# the only valid keys
VALID_KEYS = [pygame.K_1, pygame.K_2, pygame.K_3,
              pygame.K_4, pygame.K_5, pygame.K_6,
              pygame.K_7, pygame.K_8, pygame.K_9,
              pygame.K_TAB, pygame.K_SPACE, pygame.K_BACKSPACE, pygame.K_ESCAPE]
GRIDSIZE = 78
GRID_WIDTH = WIDTH // GRIDSIZE
GRID_HEIGHT = HEIGHT // GRIDSIZE
#The fonts for the text and for the time
BASE_FONT = pygame.font.Font(None, 70)
TIME_FONT = pygame.font.Font(None, 50)

# drawing the 4 lines that make the 3x3 squares
def draw_lines():
    pygame.draw.line(WIN, BLACK, (233, 0), (233, 701), width=2)
    pygame.draw.line(WIN, BLACK, (467, 0), (467, 701), width=2)
    pygame.draw.line(WIN, BLACK, (0, 233), (701, 233), width=2)
    pygame.draw.line(WIN, BLACK, (0, 467), (701, 467), width=2)
    pygame.draw.line(WIN, BLACK, (702, 0), (702, 701), width=4)


# drawing the grid(9x9 squares)
def draw_grid():
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(WIN, (150, 150, 150), r)
            else:
                rr = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(WIN, (255, 255, 255), rr)


# drawing the grid(numbers)
def draw_numbers(grid):
    integer_to_string(grid)
    surf = pygame.Surface(WIN.get_size(), pygame.SRCALPHA).convert_alpha()  # creates a clear surface
    r = 0
    for row in grid:
        c = 0
        for cell in row:
            text_surface = BASE_FONT.render(cell, True, BLACK).convert_alpha()
            surf.blit(text_surface, (c * GRIDSIZE + 26, r * GRIDSIZE + 20))
            c += 1
        r += 1

    WIN.blit(surf, (0, 0))

# Shadow the selected square
def draw_shadow(grid):
    if selected_cell:
        shadow_grid = pygame.Rect(selected_cell[0] * 78, selected_cell[1] * 78, 78, 78)
        pygame.draw.rect(WIN, (255, 0, 0), shadow_grid, 3)

#Drawing the text in case someone wins/loses
def draw_text(text):
    draw_text = BASE_FONT.render(text, 1, RED)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)
#Drawing the life of the player
def draw_life(life, can_solve):
    if can_solve == False: #We only show the life if we can't call the solve_sudoku function
        life_text = BASE_FONT.render(str(life), 1, RED)
        WIN.blit(life_text, (730, 100))
#Formating the time to seconds
def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat
#Drawing the time
def draw_time(time):
    white_rect = pygame.Rect(704, 0, 102, 702)
    pygame.draw.rect(WIN, (255, 255, 255), white_rect)
    time_surface = TIME_FONT.render(format_time(time), True, BLACK).convert_alpha()
    WIN.blit(time_surface, (700, 50))

selected_cell = None

# the main function
def main(gamemode):
    global grid, selected_cell
    life = 5
    array = [['' for i in range(9)] for x in range(9)]
    running = True
    can_solve = True # Allows us to acces
    solved = False
    start = time.time()
    if gamemode != 'solver':
        can_solve = False
        array = add_numbers(grid)


    while running:
        if solved == False:
            play_time = round(time.time() - start)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # checking for user clicks
            if event.type == pygame.MOUSEBUTTONDOWN and solved == False:
                pos = pygame.mouse.get_pos()
                col = pos[0] // GRIDSIZE
                row = pos[1] // GRIDSIZE
                if col <= 8:
                    selected_cell = [col, row]

            # checking for keys pressed
            if event.type == pygame.KEYDOWN and event.key in VALID_KEYS:  # the key can only be 1,2,3..9 or TAB, SPACE or BACKSPACE
                if event.key == pygame.K_TAB and selected_cell == None and can_solve:  # if the key is TAB solve the puzzle
                    string_to_integer(grid)
                    solve_sudoku(grid)
                    solved = True  # don't let the user change the grid anymore


                if event.key == pygame.K_ESCAPE:
                    running = False
                    reset_grid(grid)
                    solved = False

                elif selected_cell != None:  # else add that number to the grid or delete that number from the grid
                    if event.key == pygame.K_SPACE and can_solve:# SPACE and BACKSPACE deletes the number
                        grid[selected_cell[1]][selected_cell[0]] = ''
                        selected_cell = None
                    # if the position is valid                                                 You can't draw TAB or SPACE, they have other uses             you can't replace an item from the generated grid
                    elif is_valid(grid, event.unicode, selected_cell[1], selected_cell[0]) and event.key != pygame.K_TAB and event.key != pygame.K_SPACE and grid[selected_cell[1]][selected_cell[0]] != array[selected_cell[1]][selected_cell[0]] or can_solve:
                        user_text = event.unicode
                        grid[selected_cell[1]][selected_cell[0]] = user_text
                        selected_cell = None
                    # if the event isn't valid
                    else:
                        life -= 1
                        selected_cell = None

                if life == 0 and can_solve == False:
                    draw_time(play_time)
                    draw_life(life, can_solve)
                    draw_text('You lost!')
                    reset_grid(grid)
                    running = False
        # drawing everthing and updating the display
        if check_win(grid) and can_solve == False:
            draw_numbers(grid)
            draw_text('You won!')
            reset_grid(grid)
            running = False
        draw_grid()
        draw_lines()
        draw_numbers(grid)
        draw_shadow(grid)
        draw_time(play_time)
        draw_life(life, can_solve)
        pygame.display.update()


if __name__ == '__main__':
    main('solver')
