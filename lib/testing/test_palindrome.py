# test_solution.py
import pytest
from palindrome import longest_palindromic_substring


@pytest.mark.parametrize("input_string, expected", [
    ("detartrated", "detartrated"),
    ("racecar", "racecar"),
    ("aba", "aba"),
    ("1221", "1221")  # Numeric palindrome
])
def test_full_string_palindromes(input_string, expected):
    """Tests cases where the entire string is a palindrome."""
    assert longest_palindromic_substring(input_string) == expected


@pytest.mark.parametrize("input_string, expected", [
    ("Mississippi", "ississi"),  # Longest palindrome among multiple
    ("banana", "anana"),
    ("abacabaaba", "abacaba")    # Returns first if tie
])
def test_finds_longest_among_multiple(input_string, expected):
    """Tests that the function picks the longest palindrome when several exist."""
    assert longest_palindromic_substring(input_string) == expected


@pytest.mark.parametrize("char", ["a", "Z", "5", "0"])
def test_base_cases(char):
    """Tests the minimum length constraint (1 character) with letters and digits."""
    assert longest_palindromic_substring(char) == char


@pytest.mark.parametrize("input_string, expected", [
    ("Aba", "A"),        
    ("Aa", "A"),        
    ("Racecar", "aceca") 
])
def test_case_sensitivity(input_string, expected):
    """Checks that uppercase and lowercase letters are treated as different."""
    assert longest_palindromic_substring(input_string) == expected



@pytest.mark.parametrize("long_input, expected", [
    ("a" * 100, "a" * 100),
    ("abc" + ("z" * 50) + "cba", "abc" + ("z" * 50) + "cba")
])
def test_input_boundaries(long_input, expected):
    """Tests that the function handles larger inputs efficiently."""
    assert longest_palindromic_substring(long_input) == expected

    



@pytest.mark.parametrize("input_string, expected", [
    ("abc", "a"),
    ("123", "1"),
    ("father", "f")
])
def test_no_multi_char_palindromes(input_string, expected):
    """If no palindrome > 1 exists, returns the first character."""
    assert longest_palindromic_substring(input_string) == expected


# --- 7. EMPTY STRING EDGE CASE ---
def test_empty_string():
    """Returns empty string when input is empty."""
    assert longest_palindromic_substring("") == ""