def correct_sentence(text: str) -> str:

    right_var = text[:1].upper() + text[1:]
    if not right_var.endswith("."):
        right_var += "."
    return right_var


assert correct_sentence("greetings, friends") == "Greetings, friends.", "Test1"
assert correct_sentence("hello") == "Hello.", "Test2"
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", "Test3"
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", "Test4"

print("OK")