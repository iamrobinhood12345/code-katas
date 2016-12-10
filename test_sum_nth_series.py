def series_sum(n):
    # Happy Coding ^_^
    denominator = 1
    num = 0
    for i in range(0, n):
        if i == 0:
            num = 1
        else:
            num = float(num) + float(1/denominator)
        denominator += 3
    return '{:.2f}'.format(num)