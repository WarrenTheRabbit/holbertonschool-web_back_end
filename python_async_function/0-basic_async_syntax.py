#!/usr/bin/env python3
"""
Defines an async function that waits a random amount
of time and then returns the number.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Return the asynchronous delay of this function.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
