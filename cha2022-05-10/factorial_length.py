
from math import log, pi, e, ceil

def count(n):
    return ceil(n*log(n/e, 10) + log(2*pi*n, 10)/2)
