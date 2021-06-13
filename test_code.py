#!/usr/bin/python3
"""
Unit tests for code
Written by Gustav Larsson
"""

from functions import add, subtract

def test_add():

    assert add(2, 5) is 7

def test_subtract():

    assert subtract(5, 2) is 3