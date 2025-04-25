#!/usr/bin/env python3
from typing import List, Union
"""
complex types - mixed lists
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    take a list of both integers and floats and return their float sum
    """
    return sum(mxd_lst)
