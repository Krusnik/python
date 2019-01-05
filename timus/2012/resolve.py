#!/usr/bin/python3


from sys import stdin, stdout

count = int(stdin.read())
if (12-((5*60)//45+count)) >= 0:
	print ("NO")
else: print ("YES")
