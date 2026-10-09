from demo_app.math_ops import square


def test_square() -> None:
    assert square(3) == 9
    assert square(-4) == 16
    assert square(0) == 0
