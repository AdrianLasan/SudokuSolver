import unittest
from sudoku import sudoku_solver

class TestSudokuSolver(unittest.TestCase):

    def test_valid_board_1(self):
        """Test a valid Sudoku board with a known solution."""
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
        solution = sudoku_solver(board)
        expected = [
            5, 3, 4, 6, 7, 8, 9, 1, 2,
            6, 7, 2, 1, 9, 5, 3, 4, 8,
            1, 9, 8, 3, 4, 2, 5, 6, 7,
            8, 5, 9, 7, 6, 1, 4, 2, 3,
            4, 2, 6, 8, 5, 3, 7, 9, 1,
            7, 1, 3, 9, 2, 4, 8, 5, 6,
            9, 6, 1, 5, 3, 7, 2, 8, 4,
            2, 8, 7, 4, 1, 9, 6, 3, 5,
            3, 4, 5, 2, 8, 6, 1, 7, 9
        ]
        self.assertEqual(solution, expected)

    def test_valid_board_2(self):
        """Test another valid Sudoku board."""
        board = [
            0, 0, 0, 2, 6, 0, 7, 0, 1,
            6, 8, 0, 0, 7, 0, 0, 9, 0,
            1, 9, 0, 0, 0, 4, 5, 0, 0,
            8, 2, 0, 1, 0, 0, 0, 4, 0,
            0, 0, 4, 6, 0, 2, 9, 0, 0,
            0, 5, 0, 0, 0, 3, 0, 2, 8,
            0, 0, 9, 3, 0, 0, 0, 7, 4,
            0, 4, 0, 0, 5, 0, 0, 3, 6,
            7, 0, 3, 0, 1, 8, 0, 0, 0
        ]
        solution = sudoku_solver(board)
        expected = [
            4, 3, 5, 2, 6, 9, 7, 8, 1,
            6, 8, 2, 5, 7, 1, 4, 9, 3,
            1, 9, 7, 8, 3, 4, 5, 6, 2,
            8, 2, 6, 1, 9, 5, 3, 4, 7,
            3, 7, 4, 6, 8, 2, 9, 1, 5,
            9, 5, 1, 7, 4, 3, 6, 2, 8,
            5, 1, 9, 3, 2, 6, 8, 7, 4,
            2, 4, 8, 9, 5, 7, 1, 3, 6,
            7, 6, 3, 4, 1, 8, 2, 5, 9
        ]
        self.assertEqual(solution, expected)

    def test_invalid_board(self):
        """Test an invalid Sudoku board."""
        board = [
            5, 5, 0, 0, 7, 0, 0, 0, 0,  # Duplicate 5 in the first row
            6, 0, 0, 1, 9, 5, 0, 0, 0,
            0, 9, 8, 0, 0, 0, 0, 6, 0,
            8, 0, 0, 0, 6, 0, 0, 0, 3,
            4, 0, 0, 8, 0, 3, 0, 0, 1,
            7, 0, 0, 0, 2, 0, 0, 0, 6,
            0, 6, 0, 0, 0, 0, 2, 8, 0,
            0, 0, 0, 4, 1, 9, 0, 0, 5,
            0, 0, 0, 0, 8, 0, 0, 7, 9
        ]
        solution = sudoku_solver(board)
        self.assertIsNone(solution, "The function should return None for invalid boards.")

    def test_incorrect_size_board(self):
        """Test a board with incorrect size."""
        board = [0] * 80  # Only 80 cells instead of 81
        with self.assertRaises(ValueError):
            sudoku_solver(board)

    def test_empty_board(self):
        """Test an empty board (all zeros)."""
        board = [0] * 81
        solution = sudoku_solver(board)
        self.assertIsNotNone(solution, "The function should solve an empty board.")
        self.assertTrue(all(solution), "The solution should fill all cells.")

    def test_already_solved_board(self):
        """Test an already solved board."""
        board = [
            5, 3, 4, 6, 7, 8, 9, 1, 2,
            6, 7, 2, 1, 9, 5, 3, 4, 8,
            1, 9, 8, 3, 4, 2, 5, 6, 7,
            8, 5, 9, 7, 6, 1, 4, 2, 3,
            4, 2, 6, 8, 5, 3, 7, 9, 1,
            7, 1, 3, 9, 2, 4, 8, 5, 6,
            9, 6, 1, 5, 3, 7, 2, 8, 4,
            2, 8, 7, 4, 1, 9, 6, 3, 5,
            3, 4, 5, 2, 8, 6, 1, 7, 9
        ]
        solution = sudoku_solver(board)
        self.assertEqual(solution, board, "The function should return the same board if it's already solved.")

if __name__ == "__main__":
    unittest.main()
