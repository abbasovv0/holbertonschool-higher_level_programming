#!/usr/bin/python3
"""document"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """documented"""
    def __init__(self, size):
        """document"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
