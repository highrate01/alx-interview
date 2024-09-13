#!/usr/bin/python3
"""N queens"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]

    Args:
    board (List[List[int]]): The current state of the chess board
    row (int): The row to check
    col (int): The column to check
    n (int): The size of the board

    Returns:
    bool: True if it's safe to place a queen, False otherwise
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem

    Args:
    n (int): The size of the chess board and the number of queens

    Returns:
    List[List[List[int]]]: A list of all possible solutions,
    where each solution
    is represented as a list of queen positions [row, col]
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(col):
        """
        Recursive helper function to solve N Queens problem

        Args:
        col (int): The current column being processed

        Returns:
        None: Solutions are added to the 'solutions' list
        """
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

    solve(0)
    return solutions


def print_solutions(solutions):
    """
    Print all solutions of the N Queens problem

    Args:
    solutions (List[List[List[int]]]): A list of all
    solutions to print

    Returns:
    None: Solutions are printed to stdout
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    """
    Main function to handle command-line arguments and
    solve the N Queens problem
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)
