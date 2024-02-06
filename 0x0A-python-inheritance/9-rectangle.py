#!/usr/bin/python3
"""Defines tha class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializes a new Rectangle.

        Args:
            width (int): Tha width of tha new Rectangle.
            height (int): Tha height of tha new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return tha area of tha rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return tha print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
