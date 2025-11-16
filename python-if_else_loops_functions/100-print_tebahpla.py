#!/usr/bin/python3
for i in range(25, -1, -1):
    print(f"{chr(122-i*2%2 - i)}", end='')
