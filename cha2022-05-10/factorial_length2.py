"""
Bit of a refactor

In this Kata, you will implement a function count that takes an integer and returns the number of digits in factorial(n).

For example, count(5) = 3, because 5! = 120, and 120 has 3 digits.

More examples in the test cases.

Brute force is not possible. A little research will go a long way, as this is a well known series.
"""

from math import log10, pi, e

def count(n):
    return int(n*log10(n/e) + log10(2*pi*n)/2) + 1
