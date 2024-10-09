# HW 3. Task 6. Hash table processor.

SIZE_TABLE = 256
PROMPT = "HW3> "
DOCUMENTATION = '''
Используйте префиксы перед строкой:
1 | Добавить   2 | удалить   3 | Поиск
. (Одиночная точка) - выход.
~ (тильда) - генерировать тестовую таблицу.
Enter - Вывести хеш-таблицу.
------------------------------
Пример: "1 В лесу родилась елочка." - добавить строку "В лесу родилась елочка."
Пример: "2 Голубой вагон бежит качается." - удалить строку "Голубой вагон бежит качается."
'''

def my_hash(s):
    hash_string = ""
    for char in s:
        hash_string += str(ord(char))
    return int(hash_string) % SIZE_TABLE

def add_to_table(hash_table, new_string, the_hash):
    if the_hash in hash_table:
        if new_string in hash_table[the_hash]:
            print("Такая строка уже существует.")
        else:
            hash_table[the_hash].append(new_string)
            print("Строка добавлена.")
    else:
        hash_table[the_hash] = [new_string]
        print("Строка добавлена.")
    return hash_table

def remove_from_table(hash_table, remove_string, the_hash):
    if the_hash in hash_table:
        if remove_string in hash_table[the_hash]:
            if len(hash_table[the_hash]) > 1:
                updated_list = [s for s in hash_table[the_hash] if s != remove_string]
                hash_table[the_hash] = updated_list
            else:
                del hash_table[the_hash]    
        else:
            print("Такой строки в таблице не существует.")
    else:
        print("Такого индекса в таблице не существует.")
    return hash_table

def search_in_table(hash_table, search_string, the_hash):
    if the_hash in hash_table:
        if search_string in hash_table[the_hash]:
            the_index = hash_table[the_hash].index(search_string)
            return {the_hash: the_index}
        else:
            return False
    else:
        return False
def show_hash_table(hash_table):
    if len(hash_table) == 0:
        print("Таблица пуста.")
        return
    for key, value in hash_table.items():
        print(key)
        for s in value:
            print("   ", s)
    return

hash_dict = {}

print(DOCUMENTATION)

while True:
    user_input = input("HW3> ")
    if user_input == ".":
        break
    elif user_input == "":
        show_hash_table(hash_dict)
    elif user_input == "~":
        s = "В лесу родилась елочка."
        hash_dict = add_to_table(hash_dict, s, my_hash(s))
        s = "Голубой вагон бежит качается."
        hash_dict = add_to_table(hash_dict, s, my_hash(s))
        s = "В траве сидел кузнечик."
        hash_dict = add_to_table(hash_dict, s, my_hash(s))
        show_hash_table(hash_dict)
    elif user_input == "?":
        print(DOCUMENTATION)
    elif user_input[0] == "1":
        s = user_input[1:].strip()
        hash_dict = add_to_table(hash_dict, s, my_hash(s))
    elif user_input[0] == "2":
        s = user_input[1:].strip()
        hash_dict = remove_from_table(hash_dict, s, my_hash(s))
    elif user_input[0] == "3":
        s = user_input[1:].strip()
        search_result = search_in_table(hash_dict, s, my_hash(s))
        if search_result == False:
            print("Строка не найдена.")
        else:
            (key, value), = search_result.items()
            print(f"Хеш {key} Индекс {value}")
    else:
        print("Не понял. ВВедите точку ()'.') для завершения программы, или вопросительный знак ('?') для справки.")
