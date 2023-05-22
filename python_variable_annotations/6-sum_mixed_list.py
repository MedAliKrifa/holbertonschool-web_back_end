#!/usr/bin/env python3
from typing import List, Union
"""
sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns sum of list elements
    """
    return sum(mxd_lst)
