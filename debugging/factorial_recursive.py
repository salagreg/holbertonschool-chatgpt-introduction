#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Args:
        n: An integer. The number to compute the factorial of.

    Returns:
        The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
