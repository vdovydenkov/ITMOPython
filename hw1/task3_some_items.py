# ДЗ1. Задание 3.
# Выборка элементов списка

# Подключаем собственный модуль. Функция get_integer
from hw1_module import get_float, goodbye

print("Введите последовательно любые  числа. Для завершения, введите -1")

user_num = get_float("")
# Если первый же ввод дал ошибку
if user_num == None:
    goodbye(1)

# Создаем пустой список
user_list = []

# Пока ввод не закончится минус единицей или ошибкой
while (user_num != -1) and (user_num != None):
    user_list.append(user_num)
    user_num = get_float("")

print("Ввод закончен. Список чисел сформирован.")
print("-" * 30)

# Длина списка
list_length = len(user_list)
print(f"Список содержит {list_length} элементов.")

# Подсчет суммы циклом
sum_of_items = 0
for num in user_list:
    sum_of_items += num
print("Сумма, рассчитанная циклом: ", sum_of_items)

# Подсчет суммы функцией
print("Сумма элементов, рассчитанная функцией sum(): ", sum(user_list))

# Выбираем четные значения
even_numbers = []
for item in user_list:
    if item % 2 == 0:
        even_numbers.append(item)
# Проверяем, есть ли четные значения
if len(even_numbers) > 0:
    print("Все четные значения списка: ", even_numbers)
else:
    print("Четных значений в списке нет.")

print("-" * 30)

# Пауза перез завершением.
goodbye(0)