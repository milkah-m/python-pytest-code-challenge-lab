# palindrome.py
def longest_palindromic_substring(s: str) -> str:
    """
    Returns the longest contiguous palindromic substring in `s`.
    If the string is empty, returns an empty string.
    If no multi-character palindrome exists, returns the first character.
    Case-sensitive.
    """
    n = len(s)
    if n == 0:
        return ""
    if n == 1:
        return s

    start = 0
    max_len = 1

    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(n):
        len1 = expand_around_center(i, i)       
        len2 = expand_around_center(i, i + 1)   
        max_curr_len = max(len1, len2)
        if max_curr_len > max_len:
            max_len = max_curr_len
            start = i - (max_len - 1) // 2

    return s[start:start + max_len]