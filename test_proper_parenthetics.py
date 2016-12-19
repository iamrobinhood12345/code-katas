"""Tests for proper_parenthetics.py."""

import pytest

PARAMS_PAREN = [
	('()()()()', 0),
	(')()()()', -1),
	('()()()(', 1),
	('()((()', 1),
	('()))()', -1),
	('))((', -1),
	('lkasjdkjfkl(lskdjflasf)lksjdkj', 0),
	('lkasjdkj(fkl(lskdjflasf)lksjdkj', 1),
	('lkasjdkj(fkl(lskdjf)lasf)lksjdkj', 0),
	('lkasjd()kj(fkl(lskdjf)lasf)lks)jdkj', -1),
	('lkasjdkj(fkl(lskd()jflasf)lksjdkj', 1),
	('lka(((sjdkj(fkl(lskd()jflasf)lksjdkj', 1),
	('lka(((sjdkj(fkl(lskd()jfla))))))))sf)lksjdkj', -1),
]

@pytest.mark.parametrize('text, result', PARAMS_PAREN)
def test_parenthetics(text, result):
	"""Tests the proper_parenthetics function."""
	from proper_parenthetics import proper_parenthetics
	assert proper_parenthetics(text) == result