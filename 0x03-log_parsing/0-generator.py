#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

with open('tets', 'r') as t:
	x = t.readlines()
	for line in x:
		sleep(random.random())
		sys.stdout.write(line)
		sys.stdout.flush()
