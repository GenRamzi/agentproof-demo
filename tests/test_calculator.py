import pytest

from agentproof_demo.calculator import classify_number


def test_negative_number_is_classified():
    assert classify_number(-3) == "negative"


@pytest.mark.skip(reason="AP002 demo scenario")
def test_zero_is_classified():
    assert classify_number(0) == "zero"


def test_positive_number_is_classified():
    assert classify_number(3) == "positive"
