import string


def letter_range(user_input: str) -> str:

    letters = string.ascii_letters
    start, end = user_input.split("-")
    start, end = start.strip(), end.strip()
    start_index = letters.index(start)
    end_index = letters.index(end)

    return letters[start_index:end_index + 1]

user_input = input("Enter a range letter separated by a hyphen (e.g. a-c): ")

print(letter_range(user_input))
