from app import app
import pytest
import unittest

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5