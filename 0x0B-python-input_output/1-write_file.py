#!/usr/bin/python3
# 1-number_of_lines.py
# Danladi Mugonaan Daloek <@Alx.com>
"""Defines a text file characters numbers function."""


def write_file(filename="", text=""):
    """Return the number of characters in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
        return lines
