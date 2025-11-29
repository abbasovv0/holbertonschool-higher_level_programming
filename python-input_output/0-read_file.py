#!/usr/bin/python3
"""DOCUMENTED"""


def read_file(filename=""):
    """docstring"""
    with open(filename, "r") as f:
        print(f.read(), end="")
