import pytest

from src.third import define_length


@pytest.mark.parametrize(
    ('list_', 'result'),
    [
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 3)
    ]
)
def test_fourt(list_, result):
    assert define_length(list_) == result
