import string

def make_hashtag(text: str) -> str:

    clean_text = "".join(ch if ch not in string.punctuation else " " for ch in text)
    words = clean_text.split()
    core = "".join(w.capitalize() for w in words)
    hashtag = "#" + core

    return hashtag[:140] if len(hashtag) > 140 else hashtag

user_text = input("Enter the text for hashtag: ")

print(make_hashtag(user_text))
