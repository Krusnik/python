#!/usr/bin/python3.5

from sys import stdin, stdout

inputText = stdin.read().split()

print (int(inputText[0]) - int(inputText[4]), int(inputText[1]) - int(inputText[3]))
