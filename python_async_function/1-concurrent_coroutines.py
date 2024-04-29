#!/usr/bin/env python3
"""
Demonstrates async task scheduling and execution.
"""
import asyncio
from typing import List
wait_random = __import__("python_async_function/0-basic_async_syntax.py")


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns ascending list of delays as floats.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
