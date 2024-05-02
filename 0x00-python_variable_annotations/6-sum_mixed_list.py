#!/usr/bin/env python3
"""
This contains the Duck typing sum_list function
"""
import typing


def sum_mixed_list(input_list: typing.List[typing.Union[int, float]]) -> float:
    """
    :param input_list:
    :return:
    """
    return sum(input_list)
