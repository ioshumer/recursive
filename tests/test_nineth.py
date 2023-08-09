import pytest

from src.nineth import parse_parenthesis


@pytest.mark.parametrize(
    ('string', 'result'),
    [
        ("", True),
        ("()", True),
        ("(())", True),
        ("()()", True),
        ("(()())", True),

        (")(", False),
        ("())", False),
        ("((())", False),
        (")(()", False),
    ]
)
def test_parenthesis_checker(string, result):
    assert parse_parenthesis(string) is result
