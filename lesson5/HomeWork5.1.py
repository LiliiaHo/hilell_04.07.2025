import keyword
import string


entered_name = input("Enter tne name of variable: ")

def is_entered_name_allowed (name: str|None) -> bool:

    if not name:
        return False

    if set(name) == {"_"} and len(name) > 1:
        return False

    if name[0].isdigit():
        return False

    if any(ch.isupper() for ch in name):
        return False

    for ch in name:
        if ch in string.punctuation and ch != "_":
            return False
        if ch.isspace():
            return False

    if name in keyword.kwlist:
        return False

    else:
        return True


print(is_entered_name_allowed(entered_name))
