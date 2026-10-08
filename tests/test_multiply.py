from demo_app.math_ops import multiply


def test_multiply_positive_inputs() -> None:
    assert multiply(3, 4) == 12
    assert multiply(2, 5) == 10


def test_multiply_zero_in_either_position() -> None:
    assert multiply(0, 5) == 0
    assert multiply(8, 0) == 0
    assert multiply(0, 0) == 0


def test_multiply_negative_left() -> None:
    assert multiply(-3, 4) == -12
    assert multiply(-2, 5) == -10


def test_multiply_negative_right() -> None:
    assert multiply(3, -4) == -12
    assert multiply(2, -5) == -10


def test_multiply_both_negative() -> None:
    assert multiply(-3, -4) == 12
    assert multiply(-2, -5) == 10
