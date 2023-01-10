#!/usr/bin/env python3
""" Module to execute multiple coroutines at the same time with async. """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ A function to spawn wait_random n times with the
    specified max_delay and return a list of the delays
    in ascending order.
    """
    delays = []
    for i in range(n):
        task = await wait_random(max_delay)
        delays.append(task)
    return
