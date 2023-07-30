import pytest

from src.first import define_number_power


@pytest.mark.parametrize('number', list(range(10)))
@pytest.mark.parametrize('power', list(range(10)))
def test_number_power(number, power):
    assert int(pow(number, power)) == define_number_power(number, power)
