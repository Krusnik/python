#!/usr/bin/python3


from sys import stdin, stdout
from math import sqrt
tokens = reversed(stdin.read().split())

for t in tokens:
	print ("%.4f" % sqrt(int(t)))



