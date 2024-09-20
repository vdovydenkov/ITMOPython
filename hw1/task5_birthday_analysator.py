# ДЗ1. Задание 5.
# Анализируем дату  рождения.

birthday_day, birthday_month, birthday_year = 6, 2, 1979
today_day, today_month, today_year = 20, 9, 2024

print(f"Дата рождения: {birthday_day:02}/{birthday_month:02}/{birthday_year}")
print(f"Сегодня: {today_day:02}/{today_month:02}/{today_year}")

print("-" * 30)

# Определяем квартал даты рождения
if birthday_month < 4:
    print("Дата рождения приходится на первый квартал года.")
elif birthday_month < 7:
    print("Дата рождения приходится на второй квартал года.")
elif birthday_month < 10:
    print("Дата рождения приходится на третий квартал года.")
else:
    print("Дата рождения приходится на четвертый квартал года.")

# Определяем високосность
if (birthday_year % 400 == 0) or (birthday_year % 4 == 0 and birthday_year % 100 != 0):
    print("Год рождения был високосным.")
else:
    print("Год рождения не был високосным.")    

# Вычисляем количество дней от дня рождения до сегодняшней даты
# Вычисляем количество дней от начала эры до дня рождения
days_from_the_beginning_bd = birthday_year*365.25 +birthday_month*30 + birthday_day
# Количество дней от начала до сегодняшнего дня
days_from_the_beginning_td = today_year*365.25 + today_month*30 + today_day
# Вычисляем количество дней как разницу, делаем из результата целое число
num_of_days = int(days_from_the_beginning_td - days_from_the_beginning_bd)
# На всякий случай...
if num_of_days > 0:
    print(f"С даты рождения прошло {num_of_days} дней.")
else:
    print("Ошибка в датах, корректно рассчитать разницу невозможно.")

print("-" * 30)

# Пауза перед завершением
input("Нажмите Enter для завершения программы...")
