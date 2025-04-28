from typer.testing import CliRunner
from pytestzoo.main import app

runner = CliRunner()

def test_reverse_string():
    result = runner.invoke(app, ["reverse-string", "hello"])
    assert result.exit_code == 0
    assert result.output.strip() == "olleh"


def test_reverse_string_prompted():
    result = runner.invoke(app, ["reverse-string"], input="world\n")
    assert result.exit_code == 0
    assert "Please enter a string to reverse" in result.output  # It asked for prompt
    assert "dlrow" in result.output  # Output after prompt


def test_is_palindrome_yes():
    result = runner.invoke(app, ["is-palindrome", "Racecar"])
    assert result.exit_code == 0
    assert result.output.strip() == "Yes"


def test_is_palindrome_prompted():
    result = runner.invoke(app, ["is-palindrome"], input="hello\n")
    assert result.exit_code == 0
    assert "Please enter a string to check for palindrome" in result.output
    assert "No" in result.output


def test_is_palindrome_no():
    result = runner.invoke(app, ["is-palindrome", "hello"])
    assert result.exit_code == 0
    assert result.output.strip() == "No"


def test_count_vowels():
    result = runner.invoke(app, ["count-vowels", "hello"])
    assert result.exit_code == 0
    assert result.output.strip() == "2"


def test_count_vowels_prompted():
    result = runner.invoke(app, ["count-vowels"], input="AEIOU\n")
    assert result.exit_code == 0
    assert "Please enter a string to count vowels" in result.output
    assert "5" in result.output
