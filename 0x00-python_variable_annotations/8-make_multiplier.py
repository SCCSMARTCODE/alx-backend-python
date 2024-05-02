#!/usr/bin/env python3
"""
This contains the Duck typing make_multiplier function
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    :param multiplier:
    :return:
    """
    return lambda x: multiplier*x
