

def reverse_string(s: str) -> str:
    """Reverses the given string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Returns True if the string is a palindrome."""
    s_clean = ''.join(c.lower() for c in s if c.isalnum())
    return s_clean == reverse_string(s_clean)


def count_vowels(s: str) -> int:
    """Counts the number of vowels in the string."""
    return sum(1 for c in s.lower() if c in 'aeiou')
