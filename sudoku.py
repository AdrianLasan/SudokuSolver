def initiate():
    box = []
    row = []
    column = []
    for i in range(0, 81, 9):
        row.append(range(i, i + 9))
    for i in range(9):
        column.append(range(i, 80 + i, 9))
    box.extend([
        [0, 1, 2, 9, 10, 11, 18, 19, 20],
        [3, 4, 5, 12, 13, 14, 21, 22, 23],
        [6, 7, 8, 15, 16, 17, 24, 25, 26],
        [27, 28, 29, 36, 37, 38, 45, 46, 47],
        [30, 31, 32, 39, 40, 41, 48, 49, 50],
        [33, 34, 35, 42, 43, 44, 51, 52, 53],
        [54, 55, 56, 63, 64, 65, 72, 73, 74],
        [57, 58, 59, 66, 67, 68, 75, 76, 77],
        [60, 61, 62, 69, 70, 71, 78, 79, 80]
    ])
    return box, row, column


def is_valid(grid, n, pos, box, row, column):
    current_row = pos // 9
    current_col = pos % 9
    current_box = (current_row // 3) * 3 + (current_col // 3)

    # Check row
    for i in row[current_row]:
        if grid[i] == n:
            return False

    # Check column
    for i in column[current_col]:
        if grid[i] == n:
            return False

    # Check box
    for i in box[current_box]:
        if grid[i] == n:
            return False

    return True


def solve_sudoku(grid, given, box, row, column):
    i = 0
    proceed = True

    while i < 81:
        if given[i]:
            if proceed:
                i += 1
            else:
                i -= 1
        else:
            n = grid[i] + 1
            found_valid = False

            while n <= 9:
                if is_valid(grid, n, i, box, row, column):
                    grid[i] = n
                    proceed = True
                    found_valid = True
                    break
                n += 1

            if not found_valid:
                grid[i] = 0
                proceed = False

            i = i + 1 if proceed else i - 1

    return grid


def sudoku_solver(board):
    if len(board) != 81:
        raise ValueError("Invalid board size. Must contain exactly 81 values.")

    grid = board[:]
    given = [bool(x) for x in grid]
    box, row, column = initiate()

    try:
        solved_grid = solve_sudoku(grid, given, box, row, column)
        return solved_grid
    except Exception as e:
        return None


# Example Usage
if __name__ == "__main__":
    # Input grid with 0s representing empty spaces
    board = [
        5, 3, 0, 0, 7, 0, 0, 0, 0,
        6, 0, 0, 1, 9, 5, 0, 0, 0,
        0, 9, 8, 0, 0, 0, 0, 6, 0,
        8, 0, 0, 0, 6, 0, 0, 0, 3,
        4, 0, 0, 8, 0, 3, 0, 0, 1,
        7, 0, 0, 0, 2, 0, 0, 0, 6,
        0, 6, 0, 0, 0, 0, 2, 8, 0,
        0, 0, 0, 4, 1, 9, 0, 0, 5,
        0, 0, 0, 0, 8, 0, 0, 7, 9
    ]

    solved_board = sudoku_solver(board)
    if solved_board:
        for i in range(0, 81, 9):
            print(solved_board[i:i + 9])
    else:
        print("The board is unsolvable.")
