from pytestzoo import strings

def test_reverse_string():
    assert strings.reverse_string("hello") == "olleh"
    assert strings.reverse_string("") == ""
    assert strings.reverse_string("a") == "a"


def test_is_palindrome():
    assert strings.is_palindrome("racecar")
    assert strings.is_palindrome("A man, a plan, a canal, Panama")
    assert not strings.is_palindrome("hello")
    assert strings.is_palindrome("tacocat")
    assert strings.is_palindrome("tAcocaT")


def test_count_vowels():
    assert strings.count_vowels("hello") == 2
    assert strings.count_vowels("bcdfg") == 0
    assert strings.count_vowels("AEIOUaeiou") == 10
