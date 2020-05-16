# -*- coding: utf-8 -*-

import pytest
from trade_for_me.btc_climber import btc_climber

__author__ = "Hung Nguyen"
__copyright__ = "Hung Nguyen"
__license__ = "mit"


def test_btc_climber():
    assert btc_climber(1,'REP') == 1
 
    with pytest.raises(AssertionError):
        btc_climber(-10,'REP')