#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    This function computes the factorial of a number `n` using recursion. 
    The factorial of a non-negative integer `n` is defined as the product of 
    all positive integers less than or equal to `n`. The base case is 
    when `n` equals 0, where the factorial is defined to be 1.

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.
        
    Returns:
        int: The factorial of the given number `n`.

    Example:
        factorial(4) -> 24
        factorial(0) -> 1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if len(sys.argv) != 2:
    # Check if exactly one argument (number) is provided
    print("Usage: ./factorial_recursive.py <number>")
    sys.exit(1)

# Get the input number from command line arguments
try:
    f = factorial(int(sys.argv[1]))  # Call the factorial function
    print(f)  # Output the result
except ValueError:
    # Handle the case where the input is not a valid integer
    print("Please provide a valid integer.")
