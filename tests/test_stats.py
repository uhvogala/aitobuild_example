import pytest

from demo_app.stats import maximum, minimum


def test_minimum_multi_value() -> None:
    assert minimum([3, 1, 4, 1, 5]) == 1


def test_maximum_multi_value() -> None:
    assert maximum([3, 1, 4, 1, 5]) == 5


def test_minimum_single_element() -> None:
    assert minimum([7]) == 7


def test_maximum_single_element() -> None:
    assert maximum([7]) == 7


def test_minimum_negative_integers() -> None:
    assert minimum([-2, 0, 5, -8]) == -8


def test_maximum_negative_integers() -> None:
    assert maximum([-2, 0, 5, -8]) == 5


def test_minimum_empty_raises_value_error() -> None:
    with pytest.raises(ValueError, match="empty"):
        minimum([])


def test_maximum_empty_raises_value_error() -> None:
    with pytest.raises(ValueError, match="empty"):
        maximum([])
