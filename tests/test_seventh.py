import pytest

from src.seventh import define_max_number

@pytest.mark.parametrize(
    ('list_', 'result'),
    [
        ([], (None, None)),
        ([1], (1, None)),
        ([3, 5], (5, 3)),
        ([5, 3, 5], (5, 5)),
        ([5, 3, 4], (5, 4)),
        ([5, 3, 4, 2], (5, 4)),
        ([5, 3, 4, 2, 0], (5, 4)),
        ([5, 3, 4, 2, 0, 1], (5, 4)),
    ]
)
def test_fourt(list_, result):
    assert define_max_number(list_) == result
