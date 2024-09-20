# Выборка из списка нечетных чисел

# Генерируем список нечетных чисел от 1 до 60
odd_numbers = [x for x in range(1, 61) if x % 2 == 1]
print("Список сформирован: ", odd_numbers)

print("-" * 30)

# Числа, делящееся на 3 или 5, и при этом не делящееся на 15
favorite_nums = []
for num in odd_numbers:
    # Делится ли на 3 или 5
    if (num % 3 == 0) or (num % 5 == 0):
        # Не делится на 15
        if num % 15 != 0:
            favorite_nums.append(num)
list_length = len(favorite_nums)
if list_length > 0:
    print(f"Найдено {list_length} значений, делящихся на 3 или 5, и не делящихся на 15: \n", favorite_nums)
else:
    print("В этом списке нет значений, делящихся на 3 или на 5, и, при этом, не делящихся на 15.")

# Последнее значение
print("Последнее значение списка: ", odd_numbers[-1])

print("-" * 30)

# Пауза перед завершением
input("Нажмите Enter для завершения.")