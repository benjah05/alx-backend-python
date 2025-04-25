#!/usr/bin/env python3
from typing import Iterable, List, Tuple, Sequence
"""
let's duck type an iterable object
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
