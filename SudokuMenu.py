# Setup pygame/window ---------------------------------------- #
import pygame, sys, os
from pygame.locals import *
from SudokuGUI import main #Importing main() from SudokuGUI

#CONSTANTS
pygame.init()
pygame.display.set_caption('Sudoku')

screen = pygame.display.set_mode((802, 702), 0, 32)

ICON_IMAGE = pygame.image.load(os.path.join('Assets', 'icon.png'))

BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'image.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (802, 702))

#Setting the icon
pygame.display.set_icon(ICON_IMAGE)

BLACK = (0, 0, 0)

RECT_WIDTH = 200
RECT_HEIGHT = 50

font = pygame.font.SysFont(None, 80)
font_small = pygame.font.SysFont(None, 60)

#Drawing the text (play, solver, quit)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False
#The main_menu function
def main_menu():
    mainClock = pygame.time.Clock()
    while True:
        #Adding the background
        screen.blit(BACKGROUND, (0, 0))
        draw_text('Sudoku', font, (0, 0, 0), screen, 300, 151)
        #Getting the mouse position
        mx, my = pygame.mouse.get_pos()
        #Adding the 3 necesary buttons
        button_1 = pygame.Rect(300, 251, RECT_WIDTH, RECT_HEIGHT)
        button_2 = pygame.Rect(300, 322, RECT_WIDTH, RECT_HEIGHT)
        button_3 = pygame.Rect(300, 393, RECT_WIDTH, RECT_HEIGHT)
        #The play text
        play_text = 'Play'
        play_surface = font_small.render(play_text, True, BLACK).convert_alpha()
        #The solver text
        solver_text = 'Solver'
        solver_surface = font_small.render(solver_text, True, BLACK).convert_alpha()
        #The quit text
        quit_text = 'Quit'
        quit_surface = font_small.render(quit_text, True, BLACK).convert_alpha()
        #If the cursor hovers over the button
        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (0, 0, 255), button_1) #fill that rect
            if click:
                main('play')

        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(screen, (0, 0, 255), button_2)
            if click:
                main('solver')

        if button_3.collidepoint((mx, my)):
            pygame.draw.rect(screen, (0, 0, 255), button_3)
            if click:
                pygame.quit()
        #Drawing the text
        pygame.draw.rect(screen, (0, 0, 255), button_1, 3)
        screen.blit(play_surface, (356, 257))

        pygame.draw.rect(screen, (0, 0, 255), button_2, 3)
        screen.blit(solver_surface, (335, 327))

        pygame.draw.rect(screen, (0, 0, 255), button_3, 3)
        screen.blit(quit_surface, (353, 398))
        #Resetting the click variable
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: #If the user pressed escape then close the program
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN: #If the user clicked set click to True
                if event.button == 1:
                    click = True
        #Updating the display
        pygame.display.update()
        mainClock.tick(60)

main_menu()