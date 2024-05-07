#!/usr/bin/env python3
"""this contains a python module to loop 10 times """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator - function to loop 10 times
    Arguments:
        no arguments
    Returns:
        None
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
