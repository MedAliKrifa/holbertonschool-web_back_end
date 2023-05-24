#!/usr/bin/env python3
"""
sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplication
    """
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
