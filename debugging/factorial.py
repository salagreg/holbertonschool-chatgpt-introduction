#!/usr/bin/python3
import sys


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


if len(sys.argv) != 2:
    print("Usage: ./script.py <non-negative-integer>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        raise ValueError("Negative number")
except ValueError:
    print("Please provide a non-negative integer.")
    sys.exit(1)

f = factorial(int(sys.argv[1]))
print(f)
