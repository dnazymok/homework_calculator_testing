""" Home task calculator module """
import math


class Calculator:
    """ Calculator implementation """

    def add(self, x: int, y: int) -> int:
        """ Add to attributes to each other """
        if isinstance(x, int) and isinstance(y, int):
            return x + y
        raise TypeError

    def subtract(self, x: int, y: int) -> int:
        """ Subtract one attribute from another """
        if isinstance(x, int) and isinstance(y, int):
            return x - y
        raise TypeError

    def divide(self, x: int, y: int) -> float:
        """ Divide x attribute on y """
        if isinstance(x, int) and isinstance(y, int):
            return x / y
        raise TypeError

    def multiply(self, x: int, y: int) -> int:
        """ Multiply x attribute on y """
        if isinstance(x, int) and isinstance(y, int):
            return x * y
        raise TypeError

    def mod(self, x: int, y: int) -> int:
        """ Take mod of one attribute from another """
        if isinstance(x, int) and isinstance(y, int):
            return x % y
        raise TypeError

    def power(self, x: int, y: int) -> int:
        """ Raise attributes x to a power y """
        if isinstance(x, int) and isinstance(y, int):
            return x ** y
        raise TypeError

    def root(self, x: int) -> float:
        """ Take a root from attributes """
        if x < 0:
            raise ValueError
        if isinstance(x, int):
            return math.sqrt(x)
        raise TypeError
