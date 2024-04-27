#!/usr/bin/env python
"""
Defines an async function that waits a random amount of time and then returns the number.
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    number: float = (random.random() + 1) * max_delay 
    await asyncio.sleep(0, number)
    return number

    
