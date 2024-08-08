#!/usr/bin/python3
"""
contains pascal triangle module
"""


def pascal_triangle(n):
    """
    Defines a pascal triangle that returns a
    list of integers representing n
    returns empty list if n <= 0
    """
    empty_list = []
    if not isinstance(n, int):
        raise ValueError("n must be a positive integer")
    if n <= 0:
        return empty_list
    empty_list = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(empty_list[i - 1]) - 1):
            curr = empty_list[i - 1]
            temp.append(empty_list[i - 1][j] + empty_list[i - 1][j + 1])
        temp.append(1)
        empty_list.append(temp)
    return empty_list
