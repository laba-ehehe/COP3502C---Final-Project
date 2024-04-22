import pygame
import sys
from SudokuGenerator import generate_sudoku
from Board import Board
from Cell import Cell

SIDE = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (213, 100, 124)
BOLD = 13
LIGHT = 10

pygame.init()

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

        self.board = generate_sudoku(9, self.difficulty)
        self.hehe = []
        self.original = []
        self.selected = None

        for row_index, row_value in enumerate(self.board):
            current_row = []
            for col_index, col_value in enumerate(row_value):
                current_row.append(Cell(col_value, row_index, col_index, self.screen))
            self.hehe.append(current_row)

        for row_index, row_value in enumerate(self.board):
            current_row = []
            for col_index, col_value in enumerate(row_value):
                current_row.append(Cell(col_value, row_index, col_index, self.screen))
            self.original.append(current_row)

        # self.test_board = copy.deepcopy(self.board)

    def draw(self): # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. Draws every cell on this board.

        for i in range(0, 10): # draw horizontal lines
            if i & 3 == 0:
                pygame.draw.line(self.screen, BLACK, (0, i * (SIDE / 9)), (SIDE, i * (SIDE / 9)), BOLD)
            else:
                pygame.draw.line(self.screen, BLACK, (0, i * (SIDE / 9)), (SIDE, i * (SIDE / 9)), LIGHT)

        for i in range(0, 10): # draw vertical lines
            if i & 3 == 0:
                pygame.draw.line(self.screen, BLACK, (i * (SIDE / 9), 0), (i * (SIDE / 9), SIDE), BOLD)
            else:
                pygame.draw.line(self.screen, BLACK, (i * (SIDE / 9), 0), (i * (SIDE / 9), SIDE), LIGHT)

        for row in self.hehe: # draw cells
            for cell in row:
                cell.draw()

    def select(self, row, col): # Marks the cell at (row, col) in the board as the current selected cell. Once a cell has been selected, the user can edit its value or sketched value.
        # draw border around selected cell
        pygame.draw.line(self.screen, PINK, (row * (SIDE / 9), col * (SIDE / 9)), (row * (SIDE / 9), (col + 1) * (SIDE / 9)), LIGHT)
        pygame.draw.line(self.screen, PINK, (row * (SIDE / 9), (col + 1) * (SIDE / 9)), ((row + 1) * (SIDE / 9), (col + 1) * (SIDE / 9)), LIGHT)
        pygame.draw.line(self.screen, PINK, ((row + 1) * (SIDE / 9), col * (SIDE / 9)), ((row + 1) * (SIDE / 9), (col + 1) * (SIDE / 9)), LIGHT)
        pygame.draw.line(self.screen, PINK, (row * (SIDE / 9), col * (SIDE / 9)), ((row + 1) * (SIDE / 9), col * (SIDE / 9)), LIGHT)

        self.selected = self.hehe[row][col] # assign selected_cell

    def click(self, x, y): # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col) of the cell which was clicked. Otherwise, this function returns None.
        if 0 <= x <= SIDE and 0 <= y <= SIDE:
            row = int(x // (SIDE / 9))
            col = int(y // (SIDE / 9))
            return (row, col)
        else:
            return None

    def clear(self): # Clears the value cell. Note that the user can only remove the cell values and sketched value that are filled by themselves.
        if self.selected.can_be_cleared == True:
            self.selected.value = 0

    def sketch(self, value): # Sets the sketched value of the current selected cell equal to user entered value. It will be displayed at the top left corner of the cell using the draw() function.
        if self.selected.can_be_cleared:
            self.selected.set_sketched_value(value)

    def place_number(self, value): # Sets the value of the current selected cell equal to user entered value. Called when the user presses the Enter key.
        if self.selected.can_be_cleared:
            self.selected.set_cell_value(value)
    def reset_to_original(self): # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        self.hehe = self.original

    def is_full(self): # Returns a Boolean value indicating whether the board is full or not.
        for row in range(0, 9):
            for col in range(0, 9):
                if self.hehe[row][col].value == 0:
                    return False
        return True

    def update_board(self): # Updates the underlying 2D board with the values in all cells.
        for row in range(0, 9):
            for col in range(0, 9):
                self.board[row][col] = self.hehe[row][col].value

    def find_empty(self): # Finds an empty cell and returns its row and col as a tuple (x, y).
        woa = False
        x, y = 0, 0

        for row in range(0, 9):
            for col in range(0, 9):
                if self.hehe[row][col].value == 0:
                    x = self.hehe[row][col].row
                    y = self.hehe[row][col].col
                    woa = True

        if woa == True:
            return (x, y)
        else:
            return None

    def check_board(self): # Check whether the Sudoku board is solved correctly.
        for row in self.board:
            for num in range(1, 10):
                if num not in row:
                    return False

        for index in range(0, 9):
            count = 0
            # Makes a temporary list for all ints in each col.
            temp_col = []
            while count < 9:
                temp_col.append(self.board[count][index])
                count += 1
            # Checks temp_col for each single digit int.

            for num in range(1, 10):
                if num not in temp_col:
                    return False

        for row in range(0, 9, 3):
            # by using increments of 3 we can evaluate the boxes as boxes!

            for col in range(0, 9, 3):
                # turning it into a matter of boxes we can check the final win condition all at once!
                box = (self.board[row][col:col + 3] + self.board[row + 1][col:col + 3] + self.board[row + 2][col:col + 3])
                if len(set(box)) != 9:
                    return False
        return True
        