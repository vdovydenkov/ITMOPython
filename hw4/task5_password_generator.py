# Д.З. 4. Задание 5. Сгенерировать пароль заданной длины
import random
import string

SYMBOLS = string.ascii_letters + string.digits + ".,!@#$%^&*()_+-="

try:
    password_length = int(input("Введите количество символов в пароле (от 4 до 30):"))
except ValueError:
    print("Вы ввели не целое число.")
    exit()

if password_length < 4 or password_length > 30:
    print("Вы ввели число, не подходящее по диапазону.")
    exit()


# Чтобы начинался с буквы
password = random.choice(string.ascii_letters)
password += "".join([random.choice(SYMBOLS) for _ in range(password_length - 1)])
print("-" * 30)
print("Ваш пароль:", password)

# Ждем реакции пользователя
input("Нажмите Enter для завершения программы...")
