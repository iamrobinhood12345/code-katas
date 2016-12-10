import pytest

PARAMS_FAKE_BINARY = [
    ["01011110001100111", "45385593107843568"],
    ["101000111101101", "509321967506747"],
    ["011011110000101010000011011", "366058562030849490134388085"],
    ["01111100", "15889923"],
    ["100111001111", "800857237867"],
]

@pytest.mark.parametrize("result, n", PARAMS_FAKE_BINARY)
def test_fake_binary(result, n):
    from fake_binary import fake_bin
    assert fake_bin(n) == result


# test.describe("Example Tests")
# tests = [
#     # [expected, input]
#     ["01011110001100111", "45385593107843568"],
#     ["101000111101101", "509321967506747"],
#     ["011011110000101010000011011", "366058562030849490134388085"],
#     ["01111100", "15889923"],
#     ["100111001111", "800857237867"],
# ]

# for exp, inp in tests:
#     test.assert_equals(fake_bin(inp), exp)