#!/usr/bin/env python3
"""
run time for four parallel comprehensions
"""

import asyncio
from 1-async_comprehension import async_comprehension


async def measure_runtime():
    """
    async_comprehension: collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers
    """

