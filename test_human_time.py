# import pytest

# PARAMS_HUMAN_TIME = [
#     ((0), "00:00:00"),
#     ((59), "00:00:59"),
#     ((3599), "00:59:59"),
#     ((3600), "01:00:00"),
#     ((86399), "23:59:59"),
#     ((86400), "24:00:00"),
#     ((359999), "99:59:59"),
# ]

# @pytest.mark.parametrize("n, result", PARAMS_HUMAN_TIME)
# def test_human_time(n, result):
#     from human_time import make_readable
#     assert make_readable(n) == result



# from random import randint

# make_readable_solution = lambda seconds: "{:02}:{:02}:{:02}".format(seconds / 3600, seconds / 60 % 60, seconds % 60)

# print "Running tests..."
# Test.assert_equals(make_readable(0), "00:00:00")
# Test.assert_equals(make_readable(59), "00:00:59")
# Test.assert_equals(make_readable(60), "00:01:00")
# Test.assert_equals(make_readable(3599), "00:59:59")
# Test.assert_equals(make_readable(3600), "01:00:00")
# Test.assert_equals(make_readable(86399), "23:59:59")
# Test.assert_equals(make_readable(86400), "24:00:00")
# Test.assert_equals(make_readable(359999), "99:59:59")
# print "Running random tests"
# for i in xrange(100):
#     random_number = randint(0, 359999)
#     Test.assert_equals(make_readable(random_number), make_readable_solution(random_number))