#!/usr/bin/python3
"""Parsing log files with python"""

import re
import sys

ma1 = r'^(\d+\.\d+\.\d+\.\d+) -' 
ma2 = r' \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\]' 
ma3 = r' "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$' 
regex = ma1 + ma2 + ma3
codes = [200, 301, 400, 401, 403, 404, 405, 500]


def printf(codes, fsize):
	"""Prints in the required format"""
	print("File size: {}".format(fsize))
	for k, v in sorted(codes.items()):
		print("{}: {}".format(k, v))

if __name__ == "__main__":
	res = {}
	fsize = 0
	try:
		for i, line in enumerate(sys.stdin, 1):
			matches = re.match(regex, line)
			if matches:
				x = int(matches.group(3))
				if x in res:
					res[x] += 1
				elif x in codes:
					res[x] = 1
					codes.remove(x)
				fsize += int(matches.group(4))
			if i % 10 == 0:
				printf(res, fsize)
	except KeyboardInterrupt:
		printf(res, fsize)
