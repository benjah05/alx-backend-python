#!/usr/bin/env python3
from typing import Iterable, List, Tuple, Sequence
"""
let's duck type an iterable object
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length: iterate through a sequence and return a list of tuple
    """
    return [(i, len(i)) for i in lst]
