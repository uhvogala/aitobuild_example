def minimum(values: list[int]) -> int:
    if not values:
        raise ValueError("values must not be empty")
    return min(values)


def maximum(values: list[int]) -> int:
    if not values:
        raise ValueError("values must not be empty")
    return max(values[1:] or values)
