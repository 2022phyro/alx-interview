#!/usr/bin/python3
"""PArsing log files"""
import re
import sys

ma1 = r'^(\d+\.\d+\.\d+\.\d+) -'
ma2 = r' \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\]'
ma3 = r' "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
regex = ma1 + ma2 + ma3
codes = [200, 301, 400, 401, 403, 404, 405, 500]
ans = [0, 0, 0, 0, 0, 0, 0, 0]

count = 0

file_size = 0

try:
    for line in sys.stdin:
        if count % 10 == 0 and count != 0:
            print(f"File size: {file_size}")
            for k, v in zip(codes, ans):
                print(f"{k}: {v}")
        matches = re.match(regex, line)
        if matches:
            x = int(matches.group(3))
            if x in codes:
                y = codes.index(x)
                ans[y] += 1
                file_size += int(matches.group(4))
        count += 1
except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for k, v in zip(codes, ans):
        print(f"{k}: {v}")
