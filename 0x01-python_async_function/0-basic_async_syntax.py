#!/usr/bin/env python3
""" A basic asynchronous coroutine that uses the random module. """

import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """ Returns a randomly generated number between 0 and max_delay
    which is the number of seconds of delay.
    """
    secs = random.uniform(0, max_delay)
    await asyncio.sleep(secs)
    return
