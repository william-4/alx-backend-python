#!/usr/bin/env python3
""" Module to execute multiple coroutines at the same time with async. """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns Random list of random wait time. """
    delays = [task_wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
