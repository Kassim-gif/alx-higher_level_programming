#!/usr/bin/python3
"""Defines tha Rectangle class."""


class Rectangle:
    """Represent tha rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize tha new Rectangle.

        Args:
            width (int): Tha width of tha new rectangle.
            height (int): Tha height of tha new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set tha width of tha Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set tha height of tha Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return tha area of tha Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return tha perimeter of tha Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
