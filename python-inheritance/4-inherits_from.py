#!/usr/bin/python3
"""DOCUMENTED"""


def inherits_from(obj, a_class):
    """DOCUMENTED"""
    a = isinstance(obj, a_class)
    b = type(obj) is not a_class
    return a and b
