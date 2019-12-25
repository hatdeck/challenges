from collections import Counter

def solve(a,b):
    c, d = Counter(a), Counter(b)
    return sum((c-d).values()) if c&d==d else 0
