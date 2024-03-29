#!/usr/bin/python3
"""Defines a class student"""


class student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = firts_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
