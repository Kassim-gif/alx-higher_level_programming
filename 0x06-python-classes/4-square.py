#!/usr/bin/python3

"""Define tha class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): Tha size of tha new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set tha current size of tha square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return tha current area of tha square."""
        return (self.__size * self.__size)
