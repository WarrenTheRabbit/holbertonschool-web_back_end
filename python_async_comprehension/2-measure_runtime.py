#!/usr/bin/env python3
"""
Provides measure_runtime function
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Return the total run time of four async_comprehension calls.
    """
    start = time.time()
    result = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    total_time = end - start
    return total_time
