#!/usr/bin/python3
"""Defines tha class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name (str): Tha first name of tha student.
            last_name (str): Tha last name of tha student.
            age (int): Tha age of tha student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of tha Student."""
        return self.__dict__
