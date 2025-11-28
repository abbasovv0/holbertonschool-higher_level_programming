#!/usr/bin/python3
"""this module documented"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
	"""CLASS IS DOCUMEMNTED"""

	def __init__(self, width, height):
		"""DOCUMENTED"""
		self.integer_validator("width", width)
        	self.integer_validator("height", height)

        	self.__width = width
        	self.__height = height
