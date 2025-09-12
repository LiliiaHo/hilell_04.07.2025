import codecs
import re

def delete_html_tags(html_file: str, result_file: str = "cleaned.txt") -> None:
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()

    text = re.sub(r"<[^>]*>", "", html, flags=re.DOTALL)

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    cleaned_text = "\n".join(lines)

    with codecs.open(result_file, "w", "utf-8") as file:
        file.write(cleaned_text)

if __name__ == "__main__":
    delete_html_tags("draft.html", "cleaned.txt")
    print ("File was cleaned. Result is in cleaned.txt")
