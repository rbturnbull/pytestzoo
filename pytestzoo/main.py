import typer

from . import strings

app = typer.Typer()

@app.command()
def reverse_string(string: str = typer.Argument("", help="A string to reverse")):
    """Reverse a string."""
    if not string:
        string = typer.prompt("Please enter a string to reverse")
    result = strings.reverse_string(string)
    print(result)


@app.command()
def is_palindrome(string: str = typer.Argument("", help="A string to check for palindrome")):
    """Check if a string is a palindrome."""
    if not string:
        string = typer.prompt("Please enter a string to check for palindrome")
    result = strings.is_palindrome(string)
    print("Yes" if result else "No")


@app.command()
def count_vowels(string: str = typer.Argument("", help="A string to count vowels")):
    """Count the number of vowels in a string."""
    if not string:
        string = typer.prompt("Please enter a string to count vowels")
    result = strings.count_vowels(string)
    print(result)
