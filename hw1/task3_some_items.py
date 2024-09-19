# Выборка элементов списка.

import sys

# Подключаем собственный модуль. Функция get_integer.
from hw1_module import get_integer

print("Введите последовательно любые целые числа. Для завершения, введите -1")

user_integer = get_integer()
# Если первый же ввод дал ошибку.
if user_integer == None:
    print("Превышено количество попыток, или произошла иная ошибка ввода.")
    sys.exit(1)

# Создаем пустой список.
user_list = []

# Пока ввод не закончится минус единицей или ошибкой.
while (user_integer != -1) and (user_integer != None):
    user_list.append(user_integer)
    user_integer = get_integer()    

print("Ввод закончен. Список чисел сформирован.")
print("-" * 30)


# Длина списка.
list_length = len(user_list)
print(f"Список содержит {list_length} элементов.")

# Подсчет суммы циклом.
sum_of_items = 0
for num in user_list:
    sum_of_items += num
print("Сумма, рассчитанная циклом: ", sum_of_items)

# Подсчет суммы функцией.
print("Сумма элементов, рассчитанная функцией sum(): ", sum(user_list))

# Четные элементы.
print("Все четные индексы  списка: ", user_list[1::2])

print("-" * 30)


# Пауза перез завершением.
input("Нажмите Enter для завершения программы.")