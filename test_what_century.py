import pytest

PARAMS_WHAT_CENTURY = [
    (("1999"), "20th"),
    (("2011"), "21st"),
    (("2154"), "22nd"),
    (("2259"), "23rd"),
    (("1234"), "13th"),
    (("1023"), "11th"),
    (("2000"), "20th"),
]

@pytest.mark.parametrize("n, result", PARAMS_WHAT_CENTURY)
def test_what_century(n, result):
    from what_century import whatCentury
    assert whatCentury(n) == result

# Test.assert_equals(whatCentury("1999"), "20th", "With input '1999' solution produced wrong output")
# Test.assert_equals(whatCentury("2011"), "21st", "With input '2011' solution produced wrong output");
# Test.assert_equals(whatCentury("2154"), "22nd", "With input '2154' solution produced wrong output");
# Test.assert_equals(whatCentury("2259"), "23rd", "With input '2259' solution produced wrong output");
# Test.assert_equals(whatCentury("1234"), "13th", "With input '1234' solution produced wrong output");
# Test.assert_equals(whatCentury("1023"), "11th", "With input '1023' solution produced wrong output");
# Test.assert_equals(whatCentury("2000"), "20th", "With input '2000' solution produced wrong output");