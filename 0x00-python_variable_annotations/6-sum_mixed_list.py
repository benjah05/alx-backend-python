#!/usr/bin/env python3
from typing import List, Union
"""
complex types - mixed lists
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list: take a list of both integers and floats and return sum
    mxd_lst(args): list of both int and float
    """
    return sum(mxd_lst)
