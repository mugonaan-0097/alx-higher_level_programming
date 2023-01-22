#!/usr/bin/python3
# 1-number_of_lines.py
# Danladi Mugonaan Daloek <@Alx.com>
"""Defines a text file characters number function."""


def write_file(filename="", text=""):
    """Return the number of characters in a text file."""
    characters = 0
    with open(filename) as f:
        for character in f:
            characters += 1
        return characters
