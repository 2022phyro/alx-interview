#!/usr/bin/python3
"""This file attempts to check if a string is a valid UTF8 encoding
"""

def validUTF8(data):
    """Checks if the numbers in the data is a valid utf8 encoding

    Args:
        data (int): a sequence representing bytes
    """
    return all(x >= 0 and x < 256 for x in data)