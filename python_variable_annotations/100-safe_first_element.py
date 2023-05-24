#!/usr/bin/env python3
"""
Duck typing
"""
from typing import Optional, Union


def safe_first_element(lst: Optional[list]) -> Union[None, object]:
    """
    first element of a sequence
    """
    if lst:
        return lst[0]
    else:
        return None
