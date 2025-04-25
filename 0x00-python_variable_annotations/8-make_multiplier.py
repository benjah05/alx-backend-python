#!/usr/bin/env python3
from typing import Callable
"""
complex types - function
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier: return a function that multiplies a float by a multiplier
    multiplier(arg): used to multiply with the number in func
    """

    def func(num: float) -> float:
        """ multiply n by the multiplier """
        return num * multiplier

    return func
