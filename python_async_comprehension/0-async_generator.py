#!/usr/bin/env python3
"""
Documents module.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Returns 10 random numbers between 0 and 10 asynchronously.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
