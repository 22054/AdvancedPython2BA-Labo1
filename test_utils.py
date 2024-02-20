import pytest
import utils

def test_fact():
    assert utils.fact(5) == 120

def test_roots():
    assert utils.roots(4, -10, 6) == (1)
    assert utils.roots(2, 0, -2) == (-1, 1)
    assert utils.roots(2, 3, 3) == ()

def test_integrate():
    # À compléter...
    pass
