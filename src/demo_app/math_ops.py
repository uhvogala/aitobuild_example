def add(left: int, right: int) -> int:
    return left + right


def square(value: int) -> int:
    return value * value


def clamp(value: int, low: int, high: int) -> int:
    if low > high:
        raise ValueError("low must not be greater than high")
    if value < low:
        return low
    if value > high:
        return high
    return value