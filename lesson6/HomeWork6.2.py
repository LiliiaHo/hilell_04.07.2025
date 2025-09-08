def seconds_to_date(total_seconds: int) -> str:
    days = total_seconds // 86400
    hours = (total_seconds // 3600) % 24
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_word = "дні"
    else: day_word = "днів"

    return f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

user_number = int(input("Введіть число за умовою (0 <= ваше число < 8640000): "))

print(seconds_to_date(user_number))