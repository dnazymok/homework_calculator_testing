import pytest

from calculator import Calculator

invalid_data = [
    ("1", 2),
    (1, "2"),
    (0.5, 1),
    ([1, 2, 3], 5),
    (3, "300"),
    ({"a": 1, "b": 2}, {1, 2, 3})
]


@pytest.fixture()
def calculator():
    return Calculator()


@pytest.mark.parametrize("x, y, result",
                         [(1, 2, 3), (-1, -2, -3), (0, 300, 300)])
def test_add_valid(calculator, x, y, result):
    assert calculator.add(x, y) == result


@pytest.mark.parametrize("x, y", invalid_data)
def test_add_invalid(calculator, x, y):
    with pytest.raises(TypeError):
        calculator.add(x, y)


@pytest.mark.parametrize("x, y, result",
                         [(3, 2, 1), (-3, -2, -1), (-3, 3, -6)])
def test_subtract_valid(calculator, x, y, result):
    assert calculator.subtract(x, y) == result


@pytest.mark.parametrize("x, y", invalid_data)
def test_subtract_invalid(calculator, x, y):
    with pytest.raises(TypeError):
        calculator.subtract(x, y)


@pytest.mark.parametrize("x, y, result",
                         [(10, 2, 5), (100, -2, -50), (-50, 5, -10)])
def test_divide_valid(calculator, x, y, result):
    assert calculator.divide(x, y) == result


@pytest.mark.parametrize("x, y", invalid_data)
def test_divide_invalid(calculator, x, y):
    with pytest.raises(TypeError):
        calculator.divide(x, y)


def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)


@pytest.mark.parametrize("x, y, result",
                         [(1, 1, 1), (2, -5, -10), (0, 2, 0)])
def test_multiply_valid(calculator, x, y, result):
    assert calculator.multiply(x, y) == result


@pytest.mark.parametrize("x, y", invalid_data)
def test_multiply_invalid(calculator, x, y):
    with pytest.raises(TypeError):
        calculator.multiply(x, y)


@pytest.mark.parametrize("x, y, result",
                         [(5, 2, 1), (12, -5, -3), (0, 12, 0)])
def test_mod_valid(calculator, x, y, result):
    assert calculator.mod(x, y) == result


@pytest.mark.parametrize("x, y", invalid_data)
def test_mod_invalid(calculator, x, y):
    with pytest.raises(TypeError):
        calculator.mod(x, y)


def test_mod_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.mod(1, 0)


@pytest.mark.parametrize("x, y, result",
                         [(3, 2, 9), (-12, 2, 144), (0, 2, 0)])
def test_power_valid(calculator, x, y, result):
    assert calculator.power(x, y) == result


@pytest.mark.parametrize("x, y", invalid_data)
def test_power_invalid(calculator, x, y):
    with pytest.raises(TypeError):
        calculator.power(x, y)


@pytest.mark.parametrize("x, result", [(9, 3), (144, 12), (0, 0)])
def test_root_valid(calculator, x, result):
    assert calculator.root(x) == result


@pytest.mark.parametrize("x", invalid_data)
def test_root_invalid(calculator, x):
    with pytest.raises(TypeError):
        calculator.root(x)


def test_root_negative(calculator):
    with pytest.raises(ValueError):
        calculator.root(-4)
