import pytest
import calculator


def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0


def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(10, 15) == -5


def test_multiply():
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10


def test_divide():
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(9, 4) == 2.25


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)


def test_power():
    assert calculator.power(5, 2) == 25
    assert calculator.power(10, 0) == 1  # power 0 results in 1
    assert calculator.power(8, 1) == 8  # power 1 results in base value
    assert (calculator.power(-2, 2) == 4)  # negative base by *even* expoent results in *positive*
    assert (calculator.power(-3, 3) == -27)  # negative base by *odd* expoent results in *negative*
