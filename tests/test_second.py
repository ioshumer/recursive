import pytest

from src.second import define_digit_sum


@pytest.mark.parametrize(
    ('number', 'result'),
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (10, 1),
        (11, 2),
        (111, 3),
        (22, 4),
        (123, 6)
    ]
)
def test_digit_sum(number, result):
    assert result == define_digit_sum(number)