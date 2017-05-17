import pytest

PARAMS_UFC = [
(('george saint pierre'), "I am not impressed by your performance."),
(('conor mcgregor'), "I'd like to take this chance to apologize.. To absolutely NOBODY!"),
(('George Saint Pierre'), "I am not impressed by your performance."),
(('Conor McGregor'), "I'd like to take this chance to apologize.. To absolutely NOBODY!"),
]

@pytest.mark.parametrize("n, result", PARAMS_UFC)
def test_ufc(n, result):
    from ufc import quote
    assert quote(n) == result


# Test.assert_equals(quote('george saint pierre'), "I am not impressed by your performance.")
# Test.assert_equals(quote('conor mcgregor'), "I'd like to take this chance to apologize.. To absolutely NOBODY!")

# Test.assert_equals(quote('George Saint Pierre'), "I am not impressed by your performance.")
# Test.assert_equals(quote('Conor McGregor'), "I'd like to take this chance to apologize.. To absolutely NOBODY!")