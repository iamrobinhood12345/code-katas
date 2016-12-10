import pytest

PARAMS_CONVERT_STRING = [
    (("Robin Singh"), ["Robin", "Singh"]),
    (("CodeWars"), ["CodeWars"]),
    (("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"]),
    (("1 2 3"), ["1", "2", "3"]),
    ((""), [""]),
]

@pytest.mark.parametrize("n, result", PARAMS_CONVERT_STRING)
def test_convert_string(n, result):
    from convert_string import string_to_array
    assert string_to_array(n) == result


# Test.assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
# Test.assert_equals(string_to_array("CodeWars"), ["CodeWars"])
# Test.assert_equals(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
# Test.assert_equals(string_to_array("1 2 3"), ["1", "2", "3"])
# Test.assert_equals(string_to_array(""), [""])

# Test.describe("Random tests")
# from random import randint
# sol=lambda s: s.split(" ")
# base="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# for _ in range(40):
#     s=" ".join(["".join([base[randint(0,len(base)-1)] for q in range(randint(1,20))]) for k in range(randint(1,15))])
#     Test.it("Testing for "+repr(s))
#     Test.assert_equals(string_to_array(s),sol(s),"It should work for random inputs too")