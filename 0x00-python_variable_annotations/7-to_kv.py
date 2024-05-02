#!/usr/bin/env python3
"""
This contains the Duck typing to_kv function
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    :param k:
    :param v:
    :return:
    """
    return k, v**2
