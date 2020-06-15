def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok / ktok
    else:
        return 0

def numrolls(k, n):
    return sum((-1)**i * choose(n, i) * choose(k-6*i-1, k - 6*i - n) for i in xrange((k-n)/6 + 1))

def rolldice_sum_prob(k, n):
    event = numrolls(k, n)
    return float(event)/(6**n)
