import pytest
from pytestzoo import strings

def test_reverse_string():
    assert strings.reverse_string("hello") == "olleh"
    assert strings.reverse_string("") == ""
    assert strings.reverse_string("a") == "a"
    assert strings.reverse_string("وقال") == "لاقو"
    with pytest.raises(TypeError):
        strings.reverse_string(None)
    with pytest.raises(TypeError):
        strings.reverse_string(1)


def test_is_palindrome():
    assert strings.is_palindrome("racecar")
    assert strings.is_palindrome("race-car")
    assert strings.is_palindrome("A man, a plan, a canal, Panama")
    assert not strings.is_palindrome("hello")
    assert strings.is_palindrome("tacocat")
    assert strings.is_palindrome("tAcocaT")


def test_count_vowels():
    assert strings.count_vowels("hello") == 2
    assert strings.count_vowels("bcdfg") == 0
    assert strings.count_vowels("AEIOUaeiou") == 10
    assert strings.count_vowels("abüó") == 3


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("café", "cafe"),
        ("résumé", "resume"),
        ("naïve", "naive"),
        ("São Paulo", "Sao Paulo"),
        ("déjà vu", "deja vu"),
        ("", ""),           # Empty string
        ("normal", "normal"), # No accents
        ("áéíóúý", "aeiouy"), # Vowels with acute accents
        ("𝓗𝓮𝓵𝓵𝓸", "Hello"), # Fancy Unicode letters normalized (NFKD turns them into plain)
    ]
)
def test_strip_accents(input_string, expected_output):
    assert strings.strip_accents(input_string) == expected_output

