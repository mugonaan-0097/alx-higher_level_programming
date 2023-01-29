#!/usr/bin/python3
"""Defines a JSON-to-object funtion."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a string."""
    return json.loads(my_str)
