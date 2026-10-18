def word_count(text: str) -> int:
    return len(text.split())


def char_count(text: str) -> int:
    return sum(1 for char in text if not char.isspace())
