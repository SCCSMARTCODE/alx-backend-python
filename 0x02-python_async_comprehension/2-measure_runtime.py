#!/usr/bin/env python3
"""This module a python function to measure the execution time"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - function execute async_com 4 times
    Arguments:
        no arg
    Returns:
        the total execution time required to complete the task
    """
    start = time.perf_counter()
    task = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task)
    end = time.perf_counter()
    return end - start
