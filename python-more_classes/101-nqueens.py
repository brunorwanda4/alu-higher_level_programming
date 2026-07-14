#!/usr/bin/python3
"""Solve the N queens puzzle."""
import sys


def solve_nqueens(size):
    """Print every valid arrangement of size queens."""
    columns = set()
    descending_diagonals = set()
    ascending_diagonals = set()
    solution = []

    def place_queen(row):
        """Place a queen in each row using backtracking."""
        if row == size:
            print(solution)
            return

        for column in range(size):
            descending = row - column
            ascending = row + column
            if (column in columns or
                    descending in descending_diagonals or
                    ascending in ascending_diagonals):
                continue

            solution.append([row, column])
            columns.add(column)
            descending_diagonals.add(descending)
            ascending_diagonals.add(ascending)

            place_queen(row + 1)

            solution.pop()
            columns.remove(column)
            descending_diagonals.remove(descending)
            ascending_diagonals.remove(ascending)

    place_queen(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(board_size)
