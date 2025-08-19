import string

def is_palindrome(text: str) -> bool:

    only_text = [ch.lower() for ch in text if ch.isalnum()]
    reversed_list = only_text[::-1]

    return reversed_list == only_text


assert is_palindrome("A man, a plan, a canal: Panama") is True, "Test1"
assert is_palindrome("QP") is False, "Test2"
assert is_palindrome("a") is True, "Test3"
assert is_palindrome("aurora") is False, "Test4"

print("OK")