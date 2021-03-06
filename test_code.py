#!/usr/bin/python3
"""
Unit tests for code
Written by Gustav Larsson
"""

from functions import add, subtract
from api_lab import main

def test_add():
    """ Testing adding function """
    assert add(2, 5) == 7

def test_subtract():
    """ Testing subtraction function """
    assert subtract(5, 2) == 3

def test_request():
    """ Testing request status code """
    req_ok = 200

    assert main().status_code is req_ok
