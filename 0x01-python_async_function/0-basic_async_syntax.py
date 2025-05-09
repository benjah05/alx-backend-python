#!/usr/bin/env python3
"""
the basics of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random: create asynchronous coroutine
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)

    return delay_time
