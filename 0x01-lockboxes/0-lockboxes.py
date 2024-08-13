#!/usr/bin/python3
"""contains a module that define a lockAll class"""
def canUnlockAll(boxes):
    """defines a countall method"""
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    opened_boxes = set([0])
    keys = set(boxes[0])  # Keys from the first box

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in opened_boxes:
            opened_boxes.add(new_key)
            keys.update(boxes[new_key])

    return len(opened_boxes) == n
