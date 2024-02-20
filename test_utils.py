import pytest
import utils

def test_fact():
    assert utils.fact(5) == 120
    with pytest.raises(ValueError):
        utils.fact(-3)

def test_roots():
    assert utils.roots(1, 2, 1) == tuple([-1])
    assert utils.roots(2, 0, -2) == tuple([-1, 1])
    assert utils.roots(2, 3, 3) == tuple()
    assert utils.roots(0, 0, 1) == tuple()

def test_integrate():
    assert abs(utils.integrate('x**2 - 2*x', 1, 4) - 6) < 0.0000001
