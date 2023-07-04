#!/usr/bin/python3
"""This file attempts to solve the lockbox problem"""


def canUnlockAll(boxes):
    """Checks if all boxes can be unlocked"""
    visited = {0: True}
    mark = len(boxes)
    if len(boxes) == 0:
        return True
    startkey = boxes[0]
    for key in startkey:
        if key < len(boxes) and key not in visited:
            visited[key] = False
    count = 1
    while True:
        flag = True
        for k, v in visited.copy().items():
            if v is False:
                for key in boxes[k]:
                    if key < len(boxes) and key not in visited:
                        visited[key] = False
                        flag = False
                visited[k] = True
                count += 1
            else:
                continue
        if count == mark:
            return True
        if flag is True:
            return False
