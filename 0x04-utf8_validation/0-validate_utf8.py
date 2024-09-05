#!/usr/bin/env python3
"""
UTF-8 Validation
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    determines if a given data set represents a valid UTF-8 encoding.
    """
    count = 0

    for byte in data:
        if byte < 0 or byte > 255:
            return False

        if count == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                count = 1
            elif byte >> 4 == 0b1110:
                count = 2
            elif byte >> 3 == 0b11110:
                count = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                count -= 1
            else:
                return False

    return count == 0
