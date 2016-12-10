import pytest

PARAMS_REMOVE_FIRST_LAST = [
    (('eloquent'), 'loquen'),
    (('country'), 'ountr'),
    (('person'), 'erso'),
    (('place'), 'lac'),
    (('ok'), ''),
]

@pytest.mark.parametrize("n, result", PARAMS_REMOVE_FIRST_LAST)
def test_remove_first_last(n, result):
    from remove_first_last import remove_char
    assert remove_char(n) == result


# Test.describe("Tests")
# Test.assert_equals(remove_char('eloquent'), 'loquen')
# Test.assert_equals(remove_char('country'), 'ountr')
# Test.assert_equals(remove_char('person'), 'erso')
# Test.assert_equals(remove_char('place'), 'lac')
# Test.assert_equals(remove_char('ok'), '')