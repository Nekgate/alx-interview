#!/usr/bin/python3
"""A module that rotates a matrix by 90 degrees clockwise.
"""

from copy import deepcopy


def rotate_2d_matrix(matrix):
    """Rotate the given 2D matrix by 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The matrix to rotate.

    Returns:
        None: The matrix is rotated in place.
    """
    # A deep copy of the matrix to avoid altering the original while rotating
    copy_matrix = deepcopy(matrix)
    matrix.clear()

    # Reverse the copied matrix to prepare for the rotation
    copy_matrix.reverse()

    # Populate the original matrix with the rotated values
    for idx in range(len(copy_matrix)):
        temp_row = [element[idx] for element in copy_matrix]
        matrix.append(temp_row)
