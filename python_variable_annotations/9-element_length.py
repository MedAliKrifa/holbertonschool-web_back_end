#!/usr/bin/env python3
"""
Annotated Function
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    sum_mixed_list which takes a list
    mxd_lst of integers and floats and returns their sum as a float.
    """
    return [(i, len(i)) for i in lst]
