class SudokuGenerator:
    def __init__(self, row_length, removed_cells):

    def get_board(self): # Returns a 2D python list of numbers, which represents the board
    
    def print_board(self): # Displays the board to the console.

    def valid_in_row(self, row, num): # Returns a Boolean value. Determines if num is contained in the given row of the board.

    def valid_in_col(self, col, num): # Returns a Boolean value. Determines if num is contained in the given column of the board.
    
    def valid_in_box(self, row_start, col_start, num): # Returns a Boolean value. Determines if num is contained in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)

    def is_valid(self, row, col, num): # Returns if it is valid to enter num at (row, col) in the board. This is done by checking the appropriate row, column, and box.
    
    def fill_box(self, row_start, col_start): # Randomly fills in values in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2). Uses unused_in_box to ensure no value occurs in the box more than once.

    def fill_diagonal(self): # Fills the three boxes along the main diagonal of the board. This is the first major step in generating a Sudoku.

    def fill_remaining(self, row, col): # This will return a completely filled board (the Sudoku solution).

    def fill_values(self): # It constructs a solution by calling fill_diagonal and fill_remaining.
    
    def remove_cells(self): # This method removes the appropriate number of cells from the board

def generate_sudoku(size, removed): # Given size and removed, this function generates and returns a size-by-size sudoku board.
