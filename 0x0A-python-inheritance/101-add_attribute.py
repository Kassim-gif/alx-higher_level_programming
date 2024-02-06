#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): Tha object to add an attribute to.
        att (str): Tha name of tha attribute to add to obj.
        value (any): Tha value of att.
    Raises:
        TypeError: If tha attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
