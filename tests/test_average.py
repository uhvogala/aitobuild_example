from demo_app.math_ops import average


def test_average_single_value() -> None:
    assert average([5]) == 5.0


def test_average_several_values() -> None:
    assert average([1, 2, 3, 4, 5]) == 3.0
    assert average([10, 20, 30]) == 20.0
