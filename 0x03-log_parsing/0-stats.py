#!/usr/bin/python3
"""PArsing log files"""
import re
import sys

regex = r'^(\d+\.\d+\.\d+\.\d+) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

count = 0

file_size = 0

try:
    for line in sys.stdin:
        if count % 10 == 0 and count != 0:
            print(f"File size: {file_size}")
            for k, v in codes.items():
                print(f"{k}: {v}")
        matches = re.match(regex, line)
        if matches:
            x = int(matches.group(3))
            if x in codes.keys():
                codes[x] += 1
                file_size += int(matches.group(4))
        count += 1
except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for k, v in codes.items():
        print(f"{k}: {v}")
