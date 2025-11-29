#!/usr/bin/python3
"""DOCUMENTED"""


def write_file(filename="", text=""):
    """DOCUMENTED"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
