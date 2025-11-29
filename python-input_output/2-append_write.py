#!/usr/bin/python3
"""DOCUMENTED"""


def append_write(filename="", text=""):
    """DOCUMENTED"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
