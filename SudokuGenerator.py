import random
import math


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        # Initializes object by assigning passed in parameters.
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = []
        row_count, col_count = row_length, row_length
        # Creates a 2D list using assigned counting variables to conform with the row length.
        while row_count > 0:
            new_row = []
            while col_count > 0:
                # Appends nine zeros in the row.
                new_row.append(0)
                col_count -= 1
            # Appends nine rows into list.
            self.board.append(new_row)
            col_count = row_length
            row_count -= 1
        # calculate the square root of the length.
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        # Returns current board.
        return self.board

    def print_board(self):
        # Prints each row of the 2D list individually to conform with visual expectations.
        for index, item in enumerate(self.board):
            print(self.board[index])

    def valid_in_row(self, row, num):
        # Uses a for loop to compare num with other integers in the list.
        for i in self.board[row]:
            if i == num:
                # Returns False if a match is found.
                return False
        return True

    def valid_in_col(self, col, num):
        # Assigns a counter to ensure nine loops occur.
        counter = 0
        while counter < 9:
            # Compares passed in number to each element of the list.
            if self.board[counter][col] == num:
                return False
            counter += 1
        # Returns true if number is unique.
        return True

    def valid_in_box(self, row_start, col_start, num):
        # Searches for num in subsections of rows and columns that correspond with each box.
        for r in self.board[int(row_start):int(row_start) + 3]:
            if num in r[int(col_start):int(col_start) + 3]:
                return False
        return True

    def is_valid(self, row, col, num):
        # Returns False if not valid in row.
        if not self.valid_in_row(row, num):
            return False
        # Returns False if not valid in col.
        if not self.valid_in_col(col, num):
            return False
        if 0 <= row <= 2:
            if 0 <= col <= 2:
                # Top left.
                row_ind = 0
                col_ind = 0
            elif 3 <= col <= 5:
                # Top middle.
                row_ind = 0
                col_ind = 3
            else:
                # Top right.
                row_ind = 0
                col_ind = 6
        elif 3 <= row <= 5:
            if 0 <= col <= 2:
                # Middle left.
                row_ind = 3
                col_ind = 0
            elif 3 <= col <= 5:
                # Middle middle.
                row_ind = 3
                col_ind = 3
            else:
                # middle right.
                row_ind = 3
                col_ind = 6
        else:
            # Bottom left.
            if 0 <= col <= 2:
                row_ind = 6
                col_ind = 0
            # Bottom middle.
            elif 3 <= col <= 5:
                row_ind = 6
                col_ind = 3
            # Bottom right.
            else:
                row_ind = 6
                col_ind = 6
        if not self.valid_in_box(row_ind, col_ind, num):
            return False
        # Returns True if all tests pass.
        else:
            return True

    def fill_box(self, row_start, col_start):
        self.row_start = row_start
        self.col_start = col_start
        # Assigns variable with list of single-digit integers.
        unused_in_box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Assigns counter variable to restrict method to first three rows.
        row_counter = 3
        # Loop assess and modifies three by three square.
        while row_counter > 0:
            # Assigns counter variable to restrict method to first three columns.
            col_counter = 3
            while col_counter > 0:
                # strategy for randomly ordering list taken from https://note.nkmk.me/en/python-random-shuffle/.
                random.shuffle(unused_in_box)
                # Variable is assigned the new first element in the int list. Element is then removed.
                random_num = unused_in_box.pop()
                # Element is replaced with the random element.
                self.board[int(self.row_start)][int(self.col_start)] = random_num
                self.col_start += 1
                col_counter -= 1
            self.row_start += 1
            self.col_start = col_start
            row_counter -= 1

    def fill_diagonal(self):
        # Calls fill_box method and passes in the starting index for each diagonal box.
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
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

    def fill_values(self):
        # Calls methods to replace placeholder elements.
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        # Assigns temp_counter with number of cells to be removed.
        temp = self.removed_cells
        while temp >= 1:
            # Randomly selects an element of the 2D list.
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            # Checks to make sure the selected element is not already zero.
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                temp -= 1
            else:
                pass


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


# class SudokuGenerator:
#     def __init__(self, row_length=9, removed_cells=20):  # row length is always 9, and removed_cells defaults to 30 unless otherwise changed
#         self.row_length = row_length
#         self.removed_cells = removed_cells
#         self.board = [[0] * row_length for i in range(row_length)] #initializes a 2D list
#         self.box_length = int(math.sqrt(row_length))
#
#     def get_board(self):  # returns a 2D python list of numbers, which represents the board
#         return self.board
#
#     def print_board(self):  # displays the board to the console.
#         # for i in self.board:
#         #     print(" ".join(self.board[i]))
#         for index, item in enumerate(self.board):
#             print(self.board[index])
#
#     def valid_in_row(self, row, num):  # returns a Boolean value. Determines if num is contained in the given row of the board.
#         for col in range(self.row_length):
#             if num == self.board[row][col]:
#                 return False
#         return True
#
#     def valid_in_col(self, col, num):  # returns a Boolean value. Determines if num is contained in the given column of the board.
#         for row in range(self.row_length):
#             if num == self.board[row][col]:
#                 return False
#         return True
#
#     def valid_in_box(self, row_start, col_start, num):  # returns a Boolean value. Determines if num is contained in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2)
#         for row in range(3):
#             for col in range(3):
#                 if self.board[row_start + row][col_start + col] == num:
#                     return False
#         return True
#
#     def is_valid(self, row, col, num):  # returns if it is valid to enter num at (row, col) in the board. This is done by checking the appropriate row, column, and box.
#         if self.valid_in_row(row, num):
#             if self.valid_in_col(col, num):
#                 if self.valid_in_box(row - row % 3, col - col % 3, num):
#                     return True
#         return False
#
#     def fill_box(self, row_start, col_start):  # randomly fills in values in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2). Uses unused_in_box to ensure no value occurs in the box more than once.
#         for row in range(self.box_length):
#             for col in range(self.box_length):
#                 while True:
#                     num = random.randint(1, 9)  # generates a random value from 1 to 9
#                     if self.valid_in_box(row_start, col_start, num):
#                         self.board[row_start + row][col_start + col] = num
#                         break
#     def fill_diagonal(self):  # fills the three boxes along the main diagonal of the board. This is the first major step in generating a Sudoku.
#         for num in range(0, self.row_length, 3):
#             self.fill_box(num, num)
#
#     def fill_remaining(self, row, col): # This will return a completely filled board (the Sudoku solution).
#         if col >= self.row_length and row < self.row_length - 1:
#             row += 1
#             col = 0
#
#         if row >= self.row_length and col >= self.row_length:
#             return True
#
#         if row < 3:
#             if col < 3:
#                 col = 3
#
#         elif row < self.row_length - 3:
#             if col == int(row // 3 * 3):
#                 col += 3
#
#         else:
#             if col == self.row_length - 3:
#                 row += 1
#                 col = 0
#                 if row >= self.row_length:
#                     return True
#
#         for num in range(1, self.row_length + 1):
#             if self.is_valid(row, col, num):
#                 self.board[row][col] = num
#                 if self.fill_remaining(row, col + 1):
#                     return True
#                 self.board[row][col] = 0
#         return False
#
#         # if (col >= self.row_length and row < self.row_length - 1):
#         #     row += 1
#         #     col = 0
#         # if row >= self.row_length and col >= self.row_length:
#         #     return True
#         # if row < self.box_length:
#         #     if col < self.box_length:
#         #         col = self.box_length
#         # elif row < self.row_length - self.box_length:
#         #     if col == int(row // self.box_length * self.box_length):
#         #         col += self.box_length
#         # else:
#         #     if col == self.row_length - self.box_length:
#         #         row += 1
#         #         col = 0
#         #         if row >= self.row_length:
#         #             return True
#         #
#         # for num in range(1, self.row_length + 1):
#         #     if self.is_valid(row, col, num):
#         #         self.board[row][col] = num
#         #         if self.fill_remaining(row, col + 1):
#         #             return True
#         #         self.board[row][col] = 0
#         # return False
#
#     def fill_values(self):  # it constructs a solution by calling fill_diagonal and fill_remaining.
#         self.fill_diagonal()
#         self.fill_remaining(0, self.box_length)
#
#     def remove_cells(self):  # this method removes the appropriate number of cells from the board
#         cells = self.removed_cells
#         while cells > 0:
#             row = random.randint(0, self.row_length - 1)
#             col = random.randint(0, self.row_length - 1)
#             if self.board[row][col] != 0:
#                 cells -= 1
#                 self.board[row][col] = 0
#
#     def answer(board):
#         answer = []
#         for i in range(len(board)):
#             temp = []
#             for j in range(len(board[i])):
#                 temp.append(board[i][j])
#             answer.append(temp)
#         return answer
#
#
# def generate_sudoku(size, removed): # Given size and removed, this function generates and returns a size-by-size sudoku board.
#     sudoku = SudokuGenerator(size, removed)
#     sudoku.fill_values()
#     sudoku.remove_cells()
#     board = sudoku.get_board()
#     return board
#
#     # sudoku = SudokuGenerator(size, removed)
#     # sudoku.fill_values()
#     # board = sudoku.get_board()
#     # answer = answer(board)
#     # sudoku.remove_cells()
#     # board = sudoku.get_board()
#     # print(*board, sep="\n")
#     # print("")
#     # print(*answer, sep="\n")
#     # print("\n\n")
#     # return board, answer