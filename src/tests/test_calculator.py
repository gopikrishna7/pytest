from calculator.calculator import Calculator
import pytest

def test_add():
    calculator = Calculator()
    assert calculator.add(3, 5) == 8
    assert calculator.add(-3, 7) == 4

def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(10, 3) == 7
    assert calculator.subtract(3, 10) == -7

def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(2, 5) == 10
    assert calculator.multiply(0, 10) == 0

def test_divide():
    calculator = Calculator()
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(-10, 2) == -5

    with pytest.raises(ValueError):
        calculator.divide(10, 0)
