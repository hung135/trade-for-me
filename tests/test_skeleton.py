# -*- coding: utf-8 -*-

import pytest
from trade_for_me.skeleton import fib

__author__ = "Hung Nguyen"
__copyright__ = "Hung Nguyen"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
