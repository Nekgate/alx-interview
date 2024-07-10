#!/usr/bin/env python3
""" Module that contains a method that calculates
the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """Get fewest number of operations needed
    to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed.
    """
    # If n is less than 2, no operations are needed (0 operations)
    if n < 2:
        return 0

    # Initialize the number of operations and the current factor (root)
    opertn, root = 0, 2

    # Loop until root exceeds n
    while root <= n:
        # If n is divisible by root
        if n % root == 0:
            # Add root to the number of operations
            opertn += root
            # Reduce n by dividing it by root
            n = n / root
            # Decrement root to check the same factor again
            root -= 1
        # Increment root to check the next possible factor
        root += 1

    return opertn
