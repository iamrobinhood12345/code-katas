import pytest


PARAMS_NTH_SERIES = []


@pytest.mark.parametrize("n, result", PARAMS_NTH_SERIES)
def test_sum_nth_series(n, result):
    from sum_nth_series import series_sum
    assert series_sum(n) == result

# Test.describe("Basic tests")
# Test.assert_equals(series_sum(1), "1.00")
# Test.assert_equals(series_sum(2), "1.25")
# Test.assert_equals(series_sum(3), "1.39")
# Test.assert_equals(series_sum(4), "1.49")
# Test.assert_equals(series_sum(5), "1.57")
# Test.assert_equals(series_sum(6), "1.63")
# Test.assert_equals(series_sum(7), "1.68")
# Test.assert_equals(series_sum(8), "1.73")
# Test.assert_equals(series_sum(9), "1.77")
# Test.assert_equals(series_sum(15), "1.94")
# Test.assert_equals(series_sum(39), "2.26")
# Test.assert_equals(series_sum(58), "2.40")
# Test.assert_equals(series_sum(0), "0.00")

# Test.describe("Random tests")
# from random import randint
# sol=lambda n: '0.00' if n==0 else (lambda s: s[:-2]+"."+s[-2:])(str(int(round(sum([1.0/(1+i*3) for i in range(n)])*100))))
# for _ in range(40):
#     n=randint(0,100)
#     Test.it("Testing for "+str(n))
#     Test.assert_equals(series_sum(n),sol(n),"It should work for random inputs too")