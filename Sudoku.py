import copy
import numpy as np

all_subset = []


def subset_sum(arr, sum):
    """
    Given a list of integers 'arr' and an integer 'sum', this method should return a list of all the
    subsets of 'arr' that add up to 'sum'.
    """
    possible_subset = []
    all_subset.clear()
    subset_sum_help(arr, sum, possible_subset)
    return all_subset


def subset_sum_help(arr, sum, subset):
    if sum == 0:
        if subset not in all_subset:
            copy_subset = copy.deepcopy(subset)
            all_subset.append(copy_subset)
        return
    if sum < 0:
        return
    for i, num in enumerate(arr):
        subset.append(num)
        # sorted the subset in order to prevent duplicated subsets
        sorted_subset = copy.copy(subset)
        sorted_subset.sort()
        new_arr = arr[:i] + arr[i + 1:]
        subset_sum_help(new_arr, sum - num, sorted_subset)
        subset.pop()
    return


def partition_equal_subset_sum(arr):
    """
    Given a list of integers 'arr', this method should return True if 'arr' can be partitioned into 
    two subsets such that the sum of elements in both subsets is equal, otherwise return False.
    """
    sub_arr = []
    return partition_equal_subset_sum_help(arr, sub_arr)


def partition_equal_subset_sum_help(arr, sub_arr):
    if sum(arr) == sum(sub_arr):
        return True
    if len(arr) == 0:
        return
    for i, num in enumerate(arr):
        sub_arr.append(num)
        new_arr = arr[:i] + arr[i + 1:]
        result = partition_equal_subset_sum_help(new_arr, sub_arr)
        if result:
            return True
        sub_arr.pop()
    return False



def sudoku_solver(board):
    """
    Given a 2D list 'board' representing a Sudoku puzzle, this method should return True if the puzzle 
    has a solution, and False otherwise.
    """
    if is_valid_board(board):
        print(board)
        return True

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for digit in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if (is_valid_cube(board, row, col, digit)
                            and is_valid_row(board, row, digit)
                            and is_valid_column(board, col, digit)):
                        board[row][col] = digit
                        valid = sudoku_solver(board)
                        if valid:
                            return True
                        else:
                            board[row][col] = 0
                    if digit == 9:
                        return False

    return False


def is_valid_cube(board, row, col, digit):
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == digit:
                return False
    return True


def is_valid_row(board, row, digit):
    for j in range(9):
        if digit == board[row][j]:
            return False
    return True


def is_valid_column(board, col, digit):
    for i in range(9):
        if digit == board[i][col]:
            return False
    return True


def non_zero(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True


def is_valid_board(board):
    transpose_board = np.transpose(board)

    if not non_zero(board):
        return False
    else:
        for row in board:
            if len(row) != len(set(row)):
                return False
        for row in transpose_board:
            if len(row) != len(set(row)):
                return False

        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                cube = cube_to_list(board, row, col)
                if len(cube) != len(set(cube)):
                    return False
    return True


def cube_to_list(board, start_row, start_col):
    lst = []
    for i in range(3):
        for j in range(3):
            lst.append(board[i + start_row][j + start_col])
    return lst

