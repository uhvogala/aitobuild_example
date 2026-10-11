from demo_app.math_ops import clamp


def test_clamp() -> None:
    assert clamp(1, 5, 10) == 5
    assert clamp(7, 5, 10) == 7
    assert clamp(15, 5, 10) == 10
