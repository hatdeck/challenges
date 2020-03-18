def cart_prod(*sets):
    # https://docs.python.org/3/library/itertools.html#itertools.forbiddenword
    pools = [tuple(pool) for pool in sets]
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    return {tuple(prod) for prod in result} if sets else set()
