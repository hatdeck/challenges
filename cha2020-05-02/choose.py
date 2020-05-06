def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def numrolls(k, n, s):
    return sum((-1)**i * choose(n, i) * choose(k-s*i-1, k-s*i-n) for i in range((k-n)//s + 1))


def reg_sum_hits(n, s):
    return [[k, numrolls(k, n, s)] for k in range(n, s*n+1)]
