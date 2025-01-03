import pytest
from operations.addition import Addition
from operations.soustraction import Soustraction
from operations.multiplication import Multiplication
from operations.division import Division

def test_addition():
    assert Addition.calculer(2, 3) == 5

def test_soustraction():
    assert Soustraction.calculer(10, 4) == 6

def test_multiplication():
    assert Multiplication.calculer(3, 3) == 9

def test_division():
    assert Division.calculer(10, 2) == 5
