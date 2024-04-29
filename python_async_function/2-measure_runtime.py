#!/usr/bin/env python3
"""
Provides measure_time function.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Return the time to wait for n calls to wait_random.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    average_time = total_time / n
    return average_time
