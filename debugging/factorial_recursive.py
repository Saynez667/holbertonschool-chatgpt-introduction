#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    This function calculates the factorial of a given non-negative integer n using recursion.

    Parameters:
    n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given number n.
          If n is 0, returns 1 (since 0! = 1).
    """
    if n == 0:  # Base case: the factorial of 0 is 1
        return 1
    else:  # Recursive case: n! = n * (n-1)!
        return n * factorial(n-1)

# Read the input number from the command line argument
f = factorial(int(sys.argv[1]))  # Call the factorial function with the argument passed to the script

# Print the result
print(f)
