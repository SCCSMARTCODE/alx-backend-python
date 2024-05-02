#!/usr/bin/env python3
"""
This contains the Duck typing element_length function
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    :param lst:
    :return:
    """
    return [(i, len(i)) for i in lst]
