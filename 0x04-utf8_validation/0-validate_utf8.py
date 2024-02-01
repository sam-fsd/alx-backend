#!/usr/bin/env python3
"""This module contains the function validateUTF8"""


def validUTF8(data):
    """This function determines if a given data set represents a valid UTF-8
    encoding

    Args:
        data (list): The data set to validate

    Returns:
        bool: True if valid UTF-8, False otherwise
    """
    num_bytes = 0
    for num in data:
        byte = format(num, '#010b')[-8:]
        if num_bytes == 0:
            for bit in byte:
                if bit == '0':
                    break
                num_bytes += 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte[0] == '1' and byte[1] == '0'):
                return False
        num_bytes -= 1
    return num_bytes == 0
