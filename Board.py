import pygame, sys
from const import *

class Board: # This class represents an entire Sudoku board. A Board object has 81 Cell objects.
    def __init__(self, width, height, screen, difficulty): # Constructor for the Board class, screen is a window from PyGame, difficulty is a variable to indicate if the user chose easy, medium, or hard.
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        pygame.init()
        screen.pygame.display.set_mode(WIDTH, HEIGHT)
        pygame.display.set_caption('SUDOKU')

        screen.fill(WHITE)

    def draw(self): # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. Draws every cell on this board.
        # draw horizontal lines
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        # draw vertical lines
        for i in range(1, BOARD_COLS):
            pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0),(i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)

    def select(self, row, col): # Marks the cell at (row, col) in the board as the current selected cell. Once a cell has been selected, the user can edit its value or sketched value.
    
    def click(self, x, y): # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col) of the cell which was clicked. Otherwise, this function returns None.
    
    def clear(self): # Clears the value cell. Note that the user can only remove the cell values and sketched value that are filled by themselves.
    
    def sketch(self, value): # Sets the sketched value of the current selected cell equal to user entered value. It will be displayed at the top left corner of the cell using the draw() function.

    def place_number(self, value): # Sets the value of the current selected cell equal to user entered value. Called when the user presses the Enter key.

    def reset_to_original(self): # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).

    def is_full(self): # Returns a Boolean value indicating whether the board is full or not.

    def update_board(self): # Updates the underlying 2D board with the values in all cells.

    def find_empty(self): # Finds an empty cell and returns its row and col as a tuple (x, y).

    def check_board(self): # Check whether the Sudoku board is solved correctly. 
        