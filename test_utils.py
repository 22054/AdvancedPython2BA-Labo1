import pytest
import utils

def test_fact():
    assert utils.fact(5) == 120

def test_roots():
    assert utils.roots(1, 2, 1) == tuple([-1])
    assert utils.roots(2, 0, -2) == tuple([-1, 1])
    assert utils.roots(2, 3, 3) == tuple()

def test_integrate():
    assert utils.integrate('x**2 - 2*x', 1, 4) == 6
