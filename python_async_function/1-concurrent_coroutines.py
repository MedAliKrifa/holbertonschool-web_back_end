#!/usr/bin/env python3
"""
module for the delay
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    wait random function
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    wait n function
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
