from typer.testing import CliRunner
from pytestzoo.main import app

runner = CliRunner()

def test_reverse_string():
    result = runner.invoke(app, ["reverse-string", "hello"])
    assert result.exit_code == 0
    assert result.output.strip() == "olleh"


def test_is_palindrome_yes():
    result = runner.invoke(app, ["is-palindrome", "Racecar"])
    assert result.exit_code == 0
    assert result.output.strip() == "Yes"


def test_is_palindrome_no():
    result = runner.invoke(app, ["is-palindrome", "hello"])
    assert result.exit_code == 0
    assert result.output.strip() == "No"


def test_count_vowels():
    result = runner.invoke(app, ["count-vowels", "hello"])
    assert result.exit_code == 0
    assert result.output.strip() == "2"
