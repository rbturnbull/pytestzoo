import unicodedata

def reverse_string(s: str) -> str:
    """Reverses the given string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Returns True if the string is a palindrome."""
    s_clean = ''.join(c.lower() for c in s if c.isalnum())
    return s_clean == reverse_string(s_clean)


def strip_accents(s: str) -> str:
    """Remove accents from a string."""
    return ''.join(
        c for c in unicodedata.normalize('NFKD', s)
        if not unicodedata.combining(c)
    )


def count_vowels(s: str) -> int:
    """Counts the number of vowels in the string."""
    # Normalize the string to NFKC form
    s_normalized = strip_accents(s)
    
    # Lowercase and filter to alphabetic characters
    clean_string = ''.join(c.lower() for c in s_normalized if c.isalpha())

    return sum(1 for c in clean_string if c in 'aeiou')
