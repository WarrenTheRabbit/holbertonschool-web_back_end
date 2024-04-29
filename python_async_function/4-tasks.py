#!/usr/bin/env python3
"""
Demonstrates utilisation of asyncio task.
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns ascending list of delays as floats.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
