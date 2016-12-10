import pytest

PARAMS_FIND_THE_POSITION = [
    ["a", "Position of alphabet: 1"],
    ["z", "Position of alphabet: 26"],
    ["e", "Position of alphabet: 5"],
]

@pytest.mark.parametrize("n, result", PARAMS_FIND_THE_POSITION)
def test_find_the_position(n, result):
    from find_the_position import position
    assert position(n) == result

# test.describe("Example Tests")

# tests = [
#     # [input, expected]
#     ["a", "Position of alphabet: 1"],
#     ["z", "Position of alphabet: 26"],
#     ["e", "Position of alphabet: 5"],
# ]

# for inp, exp in tests:
#     test.assert_equals(position(inp), exp)