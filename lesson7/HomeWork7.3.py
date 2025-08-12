def second_index(text: str, some_str: str) -> int | None:

    first_entry = text.find(some_str)
    if first_entry == -1:
        return None

    second_entry = text.find(some_str, first_entry + 1)
    if second_entry == -1:
        return  None
    else:
        return second_entry


assert second_index("sims", "s") == 3, "Test1"
assert second_index("find the river", "e") == 12, "Test2"
assert second_index("hi", "h") is None, "Test3"
assert second_index("Hello, hello", "lo") == 10, "Test4"