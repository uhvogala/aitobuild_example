from demo_app.math_ops import cube


def test_cube() -> None:
    assert cube(3) == 27
    assert cube(-2) == -8
    assert cube(0) == 0
