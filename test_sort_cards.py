import pytest

PARAMS = [
    ('39A5T824Q7J6K', ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']),
    ('Q286JK395A47T', ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']),
    ('54TQKJ69327A8', ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']),
    ('A', ['A']),
    ('96J32QK', ['2', '3', '6', '9', 'J', 'Q', 'K']),
]


@pytest.mark.parametrize("n, result", PARAMS)
def test_sort_cars(n, result):
    from sort_cards import sort_cards
    assert sort_cards(n) == result
