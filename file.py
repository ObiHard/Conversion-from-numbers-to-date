seconds = int(input("Введите количество секунд (0 ≤ число < 8640000): "))
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in [2, 3, 4] and not 11 <= days % 100 <= 14:
    day_word = "дня"
else:
    day_word = "дней"
time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(f"{days} {day_word}, {time_str}")
