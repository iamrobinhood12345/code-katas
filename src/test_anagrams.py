import pytest

PARAMS_ANAGRAMS = [
    (('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa']),
    (('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer']),
    (('a', ['a', 'b', 'c', 'd']), ['a']),
    (('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer']), ['ab', 'ba']),
    (('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa']), ['aabb', 'bbaa', 'abab', 'baba', 'baab']),
    (('big', ['gig', 'dib', 'bid', 'biig']), []),
]

@pytest.mark.parametrize("n, result", PARAMS_ANAGRAMS)
def test_anagrams(n, result):
    from anagrams import anagrams
    a = n[0]
    b = n[1]
    assert anagrams(a, b) == result

# Test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
# Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
# Test.assert_equals(anagrams('a', ['a', 'b', 'c', 'd']), ['a'])
# Test.assert_equals(anagrams('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer']), ['ab', 'ba'])
# Test.assert_equals(anagrams('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa']), ['aabb', 'bbaa', 'abab', 'baba', 'baab'])
# Test.assert_equals(anagrams('big', ['gig', 'dib', 'bid', 'biig']), [])