"""Sums n terms of the series."""


def series_sum(n):
    """Sum n terms of the series: Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +..."""
    num = 0.0
    for denominator in range(1, 1 + n * 3, 3):
        num += 1 / float(denominator)
    return '{:.2f}'.format(num)
