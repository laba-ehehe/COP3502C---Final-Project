
class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells=20): #row length is always 9, and removed_cells is always 30 unless otherwise changed
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for i in range(row_length)] #initializes a 2D list
        self.box_length = int(math.sqrt(row_length))

    def get_board(self): #returns a 2D python list of numbers, which represents the board
        return self.board
    
    def print_board(self): #displays the board to the console.
        for i in self.board:
            print(" ".join(self.board[i]))

    def valid_in_row(self, row, num): #returns a Boolean value. Determines if num is contained in the given row of the board.
        for col in range(self.row_length):
            if num == self.board[row][col]:
                return False
        return True

    def valid_in_col(self, col, num): #returns a Boolean value. Determines if num is contained in the given column of the board.
        for row in range(self.row_length):
            if num == self.board[row][col]:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num): #returns a Boolean value. Determines if num is contained in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
        for row in range(3):
            for col in range (3):
                if self.board[row_start + i][col_start + j] == num:
                    return False
            return True

    def is_valid(self, row, col, num): #returns if it is valid to enter num at (row, col) in the board. This is done by checking the appropriate row, column, and box.
        if self.valid_in_row(row, num):
            if self.valid_in_col(col, num):
                if self.valid_in_box(row - row % 3, col - col % 3, num):
                    return True
        return False

    def fill_box(self, row_start, col_start): #randomly fills in values in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2). Uses unused_in_box to ensure no value occurs in the box more than once.
        num = 0
        for row in range(self.box_length):
            for col in range(self.box_length):
                while True:
                    num = random.randint(1, 9) #generates a random value from 1 to 9
                    if self.valid_in_box(row_start, col_start, num): #checks if the randomly generated number is valid for the current 3x3 cell
                        self.board[row_start + row][col_start + col] = num #if not valid, loops through until a valid value is found
                        break
    def fill_diagonal(self): # Fills the three boxes along the main diagonal of the board. This is the first major step in generating a Sudoku.
        for i in range(0, self.size, 3):
            self.fill_box(i, i)

    def fill_remaining(self, row, col): # This will return a completely filled board (the Sudoku solution).
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
    
    def fill_values(self): # It constructs a solution by calling fill_diagonal and fill_remaining.
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self): # This method removes the appropriate number of cells from the board

def generate_sudoku(size, removed): # Given size and removed, this function generates and returns a size-by-size sudoku board.
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board