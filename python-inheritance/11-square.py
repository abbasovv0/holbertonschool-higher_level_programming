#!/usr/bin/python3
"""DOCUMENTED"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """DOCUMENTED"""
    def __init__(self, size):
        """DOCUMENTED"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
