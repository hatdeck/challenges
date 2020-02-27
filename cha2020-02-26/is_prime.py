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
