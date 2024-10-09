# HW 3. Task 1. Change a list of numbers
from functools import reduce

# Some constants
STOP_STRING = "."

# Get a data
print(f"Введите числа для обработки ('{STOP_STRING}' - для завершения)")
num_list = []
while True:
    user_input = input("Введите число:")
    if user_input == STOP_STRING:
        break
    try:
        num_list.append(float(user_input))
    except ValueError:
        print("Введенное значение - не число!")

if len(num_list) < 2:
    print("Недостаточно данных для обработки!")
    exit()

# Output a start line
print("-" * 30)
print("Исходный список чисел:\n", *num_list)
print("-" * 30)

# Raise to the power
cube_list = list(map(lambda x: x**3, num_list))
# Output the first result
print("Список чисел, возведенных в третью степень:\n", *cube_list)

# Get even numbers only
even_list = list(filter(lambda x: x % 2 == 0, cube_list))
# Output the second result
print("Выбраны только четные числа из списка кубов:\n", *even_list)

product = reduce(lambda x, y: x*y, even_list)
# Output the third result
print("Результат перемножения всех чисел второго списка:\n", product)

# Waiting for user
input("Нажмите Enter для завершения программы...")
