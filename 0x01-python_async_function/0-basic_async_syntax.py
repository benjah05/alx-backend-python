#!/usr/bin/env python3
"""
the basics of async
"""

import asyncio
import random
from typing import Generator


async def wait_random(max_delay: int = 10) -> Generator[None, None, float]:
    """
    main: create asynchronous coroutine
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)

    return delay_time
