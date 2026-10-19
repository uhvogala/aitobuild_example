def capitalize_words(text: str) -> str:
    words = text.split()
    return " ".join(word[:1].upper() + word[1:] for word in words)


def count_vowels(text: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)
