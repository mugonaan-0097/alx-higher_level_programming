#!/usr/bin/python3
# 1-number_of_lines.py
# Danladi Mugonaan Daloek <@Alx.com>
"""Defines a text file characters number function."""


def write_file(filename="", text=""):
    """Return the number of characters in a text file."""
    nb_characters = 0
    with open(filename) as f:
        for nb_character in f:
            nb_characters += 1
        return nb_characters
