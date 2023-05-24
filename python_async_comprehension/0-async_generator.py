#!/usr/bin/env python3
"""
asynchronously wait 1 second, then yield a random number
between 0 and 10. Use the random module.
"""
import asyncio
import random


async def async_generator():
    """
    async_generator function
    """   
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
