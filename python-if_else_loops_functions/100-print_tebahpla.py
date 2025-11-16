#!/usr/bin/python3
for i in range(26):
    print("{}".format(chr(122 - i*2) if i % 2 == 0 else chr(90 - i*2 + 1)), end='')
