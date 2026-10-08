from demo_app.math_ops import multiply


def test_multiply_positive() -> None:
    assert multiply(3, 4) == 12
    assert multiply(7, 1) == 7


def test_multiply_negative() -> None:
    assert multiply(-3, -4) == 12
    assert multiply(-5, -2) == 10


def test_multiply_mixed_sign() -> None:
    assert multiply(-3, 4) == -12
    assert multiply(5, -2) == -10


def test_multiply_zero() -> None:
    assert multiply(8, 0) == 0
    assert multiply(0, -6) == 0
    assert multiply(0, 0) == 0
