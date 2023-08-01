import pytest

from src.fourth import check_palindrom


@pytest.mark.parametrize(
    ('string', 'result'),
    [
        ('a', True),
        ('aba', True),
        ('abcd', False),
        ('abcba', True)
    ]
)
def test_fourt(string, result):
    assert check_palindrom(string) is result
