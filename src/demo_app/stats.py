def minimum(values: list[int]) -> int:
    if not values:
        raise ValueError("cannot compute minimum of empty input")
    return min(values)


def maximum(values: list[int]) -> int:
    if not values:
        raise ValueError("cannot compute maximum of empty input")
    return max(values)
