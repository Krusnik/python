#!/usr/bin/python3


from sys import stdin, stdout

count = stdin.read().split()

sum = int(count[0])+int(count[1])-1

print (sum - int(count[0]), sum - int(count[1]), sep = " ")
