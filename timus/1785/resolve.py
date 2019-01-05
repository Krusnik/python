#!/usr/bin/python3


from sys import stdin, stdout

count = stdin.read()

def get_text_of_count(count):
    return {
          1 <= count <= 4:   	'few',
          5 <= count <= 9:   	'several',
         10 <= count <= 19:  	'pack',
         20 <= count <= 49:  	'lots',
         50 <= count <= 99:  	'horde',
        100 <= count <= 249:   	'throng',
        250 <= count <= 499:   	'swarm',
        500 <= count <= 999:  	'zounds',
       1000 <= count:  		'legion'
    }[True]

print (get_text_of_count(int(count)))
