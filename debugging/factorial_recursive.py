#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate the factorial of the input number from the command line argument
f = factorial(int(sys.argv[1]))

# Print the computed factorial
print(f)
