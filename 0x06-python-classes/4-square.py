#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    """A class named square

    Attributes:
    attr1 (size): size of square
    """
    def __init__(self, size=0):
        """
        Args:
        size (int): size for __size attribute of class instance
        """
        self.__size = size

    def area(self):
        """Calculates the area based on size of square
        Returns:
        int: The return value. Returns the area
        """
        return self.__size * size.__size

    @property
    def size(self):
        """Gets the size of the class instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the class instance"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

