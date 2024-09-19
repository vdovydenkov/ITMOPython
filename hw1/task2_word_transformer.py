# Трансформер   слова.

import sys

user_word = None

attempts = 5
while attempts > 0:
    user_input = input("Введите слово: ")
    if user_input: # Если ввод не пустой.
        # Берем первое слово.
        user_word = user_input.split()[0]
        break
    else:
        print("Вы ввели пустую строку. Попробуйте еще раз, или нажмите Ctrl+C для завершения программы.")
    attempts -= 1    
if user_word == None:
    print("Что-то пошло не так.")    
    sys.exit(1)

print("-" * 30)

# Показываем каждый второй символ.
print(f"Выборка каждого второго символа: {user_word[1::2]}")
# Строка наоборот.
print(f"Инвертируем слово: {user_word[::-1]}")

print("-" * 30)

# Пауза перед завершением.
input("Нажмите Enter для завершения программы.")