from demo_app.textstats import char_count, word_count


def test_normal_mixed_words_and_spaces() -> None:
    text = "hello world"
    assert word_count(text) == 2
    assert char_count(text) == 10


def test_empty_string() -> None:
    assert word_count("") == 0
    assert char_count("") == 0


def test_whitespace_only() -> None:
    assert word_count("   ") == 0
    assert char_count("   ") == 0
    assert word_count("\t\n  ") == 0
    assert char_count("\t\n  ") == 0
    assert word_count("\n") == 0
    assert char_count("\n") == 0


def test_leading_trailing_repeated_whitespace() -> None:
    text = "  hello   world  "
    assert word_count(text) == 2
    assert char_count(text) == 10

    text_with_tabs_and_newlines = "\thello\n\nworld  foo\t"
    assert word_count(text_with_tabs_and_newlines) == 3
    assert char_count(text_with_tabs_and_newlines) == 13
