#!/usr/bin/env python3
from typing import Union, Tuple
"""
complex types - string and int/float to tuple
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv: return a tuple of k and v (float) squared
    """
    return k, v ** 2
