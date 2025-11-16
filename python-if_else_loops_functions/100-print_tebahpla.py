#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{0}{1}".format(chr(122-i*2%2-i if i % 2 == 0 else 90-i), ""), end='')

