from demo_app.math_ops import add


def test_add() -> None:
    assert add(3, 4) == 7
    assert add(-2, 5) == 3
    assert add(8, 0) == 8