#!/usr/bin/python3

from sys import stdin, stdout
tokens = reversed(stdin.read().split())
sum = 0
for t in tokens:
	sum = sum + float(t)

print("%.0f" % sum)


