from demo_app.strops import capitalize_words, count_vowels


def test_capitalize_words_normal() -> None:
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("one  two\tthree") == "One Two Three"


def test_capitalize_words_empty() -> None:
    assert capitalize_words("") == ""


def test_capitalize_words_whitespace_only() -> None:
    assert capitalize_words("   ") == ""
    assert capitalize_words(" \t\n ") == ""


def test_count_vowels_normal() -> None:
    assert count_vowels("hello world") == 3
    assert count_vowels("AEIOU aeiou") == 10
    assert count_vowels("rhythm") == 0


def test_count_vowels_empty() -> None:
    assert count_vowels("") == 0


def test_count_vowels_whitespace_only() -> None:
    assert count_vowels("   ") == 0
    assert count_vowels(" \t\n ") == 0
