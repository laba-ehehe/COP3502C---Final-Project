import pygame, sys
from const import *
from Cell import Cell

class Board: # This class represents an entire Sudoku board. A Board object has 81 Cell objects

    def __init__(self, width, height, screen, difficulty): # Constructor for the Board class, screen is a window from PyGame, difficulty is a variable to indicate if the user chose easy, medium, or hard.
        self.width = width
        self.height = height
        self.screen = screen

        if difficulty == 'EASY':
            self.difficulty = 30
        elif difficulty == 'MEDIUM':
            self.difficulty = 40
        elif difficulty == 'HARD':
            self.difficulty = 50

        pygame.init()
        screen.pygame.display.set_mode(WIDTH, HEIGHT)
        pygame.display.set_caption('SUDOKU')
        screen.fill(WHITE)

    def draw(self): # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. Draws every cell on this board.

        for i in range(0, BOARD_ROWS + 1): # draw horizontal lines
            if i & 3 == 0:
                pygame.draw.line(self.screen, BLACK, (0, i * ()), (WIDTH, i * SQUARE_SIZE), BOLD)
            else:
                pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), BOLD)

        for i in range(0, BOARD_COLS + 1): # draw vertical lines
            pygame.draw.line(self.screen, BLACK, (i * SQUARE_SIZE, 0),(i * SQUARE_SIZE, HEIGHT), LIGHT)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)



    # draws the vertical lines every 3rd bolded
    for index in range(0, 10):
        if index % 3 == 0:
            pygame.draw.line(self.screen, (0, 0, 0), (index * (600 / 9), 0), (index * (600 / 9), 600), 10)
        else:
            pygame.draw.line(self.screen, (0, 0, 0), (index * (600 / 9), 0), (index * (600 / 9), 600), 5)

    # draws the horizontal lines every 3rd bolded
    for index in range(0, 10):
        if index % 3 == 0:
            pygame.draw.line(self.screen, (0, 0, 0), (0, index * (600 / 9)), (600, index * (600 / 9)), 10)
        else:
            pygame.draw.line(self.screen, (0, 0, 0), (0, index * (600 / 9)), (600, index * (600 / 9)), 5)

    # draws the cells
    for row in self.cells:
        for cell in row:
            cell.draw()


    def select(self, row, col): # Marks the cell at (row, col) in the board as the current selected cell. Once a cell has been selected, the user can edit its value or sketched value.
        if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS:
            self.selected_cell = (row, col)

    def click(self, x, y): # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col) of the cell which was clicked. Otherwise, this function returns None.
        if x < WIDTH and y < HEIGHT:
            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE
            self.select(row, col)
            return (row, col)
        return None

    def clear(self): # Clears the value cell. Note that the user can only remove the cell values and sketched value that are filled by themselves.
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].set_cell_value(0)  # assuming you have a method to clear the cell value

    def sketch(self, value): # Sets the sketched value of the current selected cell equal to user entered value. It will be displayed at the top left corner of the cell using the draw() function.

    def place_number(self, value): # Sets the value of the current selected cell equal to user entered value. Called when the user presses the Enter key.

    def reset_to_original(self): # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).

    def is_full(self): # Returns a Boolean value indicating whether the board is full or not.
        return all(cell.value != 0 for row in self.cells for cell in row)

    def update_board(self): # Updates the underlying 2D board with the values in all cells.

    def find_empty(self): # Finds an empty cell and returns its row and col as a tuple (x, y).
        if self.board[row - 1][col - 1] != 0:
            return False
        else:
            return True

    def check_board(self): # Check whether the Sudoku board is solved correctly.
        