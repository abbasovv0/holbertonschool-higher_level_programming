#!/usr/bin/python3
"""
Module that provides a function to return the list of
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        A list containing the object's attributes and methods.
    """
    return dir(obj)
