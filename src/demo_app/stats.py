def minimum(values: list[int]) -> int:
    """Return the smallest integer in ``values``.

    Raises:
        ValueError: If ``values`` is empty.

    Examples:
        >>> minimum([3, 1, 4, 1, 5])
        1
    """
    if not values:
        raise ValueError("values must not be empty")
    return min(values)


def maximum(values: list[int]) -> int:
    """Return the largest integer in ``values``.

    Raises:
        ValueError: If ``values`` is empty.

    Examples:
        >>> maximum([3, 1, 4, 1, 5])
        5
    """
    if not values:
        raise ValueError("values must not be empty")
    return max(values)


def value_range(values: list[int]) -> int:
    """Return the difference between the largest and smallest integers in ``values``.

    Raises:
        ValueError: If ``values`` is empty.

    Examples:
        >>> value_range([3, 1, 4, 1, 5])
        4
    """
    return maximum(values) - minimum(values)
