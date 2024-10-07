def divide(first, second):
    num = 0
    if second == 0:
        from math import inf
        num = inf
    else:
        num += first / second

    return float(num)

