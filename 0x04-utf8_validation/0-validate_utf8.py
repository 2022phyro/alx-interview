#!/usr/bin/python3
"""This file attempts to check if a string is a valid UTF8 encoding
"""

def validUTF8(data):
    """Checks if the numbers in the data is a valid utf8 encoding

    Args:
        data (int): a sequence representing bytes
    """
    i = 0
    while i < len(data):
        # Check for 1-byte character (0xxxxxxx)
        if (data[i] & 0b10000000) == 0:
            i += 1
        # Check for 2-byte character (110xxxxx 10xxxxxx)
        elif i + 1 < len(data) and (data[i] & 0b11100000) == 0b11000000 and (data[i + 1] & 0b11000000) == 0b10000000:
            i += 2
        # Check for 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
        elif i + 2 < len(data) and (data[i] & 0b11110000) == 0b11100000 and (data[i + 1] & 0b11000000) == 0b10000000 and (data[i + 2] & 0b11000000) == 0b10000000:
            i += 3
        # Check for 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
        elif i + 3 < len(data) and (data[i] & 0b11111000) == 0b11110000 and (data[i + 1] & 0b11000000) == 0b10000000 and (data[i + 2] & 0b11000000) == 0b10000000 and (data[i + 3] & 0b11000000) == 0b10000000:
            i += 4
        else:
            return False
    return True
