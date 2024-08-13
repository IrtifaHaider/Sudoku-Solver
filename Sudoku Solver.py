class Board:
    def __init__(self, board):
        self.board = board # Initialize the board with the provided 2D list.

    def __str__(self):
        board_str = '' # Return a string representation of the board.
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try: # Find the first 0 in the row
                col = contents.index(0)
                return row, col  # Return the position of the empty cell
            except ValueError:
                pass  # Continue if 0 is not found in this row
        return None  # Return None if no empty cells are found

    def valid_in_row(self, row, num):
        return num not in self.board[row] # Check if a number can be placed in the specified row.

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(len(self.board))) #Check if a number can be placed in the specified column.

    def valid_in_square(self, row, col, num):
        # Check if a number can be placed in the 3x3 sub-grid.
        square_size = int(len(self.board) ** 0.5) # Calculate sub-grid size
        row_start = (row // square_size) * square_size
        col_start = (col // square_size) * square_size
        for row_no in range(row_start, row_start + square_size):
            for col_no in range(col_start, col_start + square_size):
                if self.board[row_no][col_no] == num:
                    return False  # Return False if number is found in the sub-grid
        return True

    def is_valid(self, empty, num):
        # Check if placing a number in the specified cell is valid.
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square]) # All conditions must be true

    def solver(self):
        # Solve the Sudoku puzzle using backtracking.
        if (next_empty := self.find_empty_cell()) is None:
            return True  # Return True if the puzzle is solved (no empty cells left)
        row, col = next_empty

        for guess in range(1, len(self.board) + 1):
            if self.is_valid(next_empty, guess):
                self.board[row][col] = guess # Place the guess on the board
                # print(f'Placed {guess} at ({row}, {col}):\n{self}')
                
                if self.solver():
                    return True  # Recursively attempt to solve the rest of the board
                self.board[row][col] = 0  # Backtrack
                # print(f'Backtracked at ({row}, {col}):\n{self}')
        return False # Trigger backtracking if no valid numbers work

def get_puzzle_from_user():
    size = int(input("Enter the size of your puzzle (e.g., 9 for a 9x9 puzzle): "))
    board = []
    print(f"Enter your {size}x{size} Sudoku puzzle row by row. Use 0 for empty cells.")
    for i in range(size):
        row = input(f"Enter row {i + 1} (comma-separated, {size} digits): ")
        board.append([int(x) for x in row.split(',')])
    return board

def solve_sudoku(board):
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

def main():
    puzzle = get_puzzle_from_user()
    solve_sudoku(puzzle)

main()
