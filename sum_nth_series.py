"""Sums n terms of the series:
Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
"""

def series_sum(n):
    denominator = 1
    num = 0
    for i in range(0, n):
        if i == 0:
            num = 1
        else:
            num = float(num) + float(1/denominator)
        denominator += 3
    return '{:.2f}'.format(num)
