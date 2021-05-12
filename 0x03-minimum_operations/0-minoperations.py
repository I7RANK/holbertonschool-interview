#!/usr/bin/python3
"""This module contains the minOperations function that
calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (Int): The number of H

    Returns:
        [Int]: The least number of operations
    """
    fewest_num = 0
    multi = 2
    tmp = n
    tmp_int = n

    if type(n) != int or n < 1:
        return 0

    while (True):
        tmp = tmp_int / multi

        if tmp_int == 1:
            break

        if not tmp.is_integer():
            multi += 1
        elif tmp.is_integer():
            fewest_num += multi
            multi = 2
            tmp_int = tmp
        elif tmp_int == multi:
            fewest_num += multi
            break

    return fewest_num
