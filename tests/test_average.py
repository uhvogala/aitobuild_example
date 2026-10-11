from demo_app.math_ops import average


def test_average_single_value() -> None:
    assert average([7]) == 7.0


def test_average_several_values() -> None:
    assert average([1, 2, 3, 4]) == 2.5
    assert average([10, 20, 30]) == 20.0
