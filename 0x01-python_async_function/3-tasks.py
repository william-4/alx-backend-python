#!/usr/bin/env python3
""" Module to return an asyncio.Task object. """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ A function that takes an integer max_delay
    and returns a asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
