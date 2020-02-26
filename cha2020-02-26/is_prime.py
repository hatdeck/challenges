"""
Consider an array with no prime numbers or prime digit. It would start with: [1,4,6,8,9,10,14,16,18,40,44..].

12 and 15 are not in the list because 2 and 5 are primes.

You will be given an integer n and your task will be return the number at that index in the array. For example:

solve(0) = 1
solve(2) = 6
"""

def is_prime(n):
    if n < 3: return n == 2
    if not n%2: return False
    for i in range(3, int(n**0.5 + 1), 2):
        if not n%i: return False
    return True

def solve(n):
    arr = [1]
    last = 1
    while len(arr) < n + 1:
        last += 1
        if not is_prime(last) and not any(is_prime(int(i)) for i in str(last)):
            arr.append(last)
    return arr[n]
