from task2_binary_tree_classes import *

HELP = '''СПРАВКА
    Для добавления в дерево введите "1", Пробел и целое число в качестве значения
    Для удаления из дерева введите "2", Пробел и удаляемое значение
    Для поиска введите "3", Пробел и искомое значение
    Для отображения дерева просто нажмите Enter
    Для выхода введите точку (".")
    Для справки введите вопросительный знак ("?")
'''


tree = Tree()

print(HELP)
while True:
    user_input = input("HW5>")
    if user_input == "":
        tree.show()
        print()
        continue
    if user_input == ".":
        exit()
    if user_input == "?":
        print(HELP)
        continue
    if len(user_input) < 2: continue
    if user_input[:2] == "1 ":
        user_input = user_input[2:].strip()
        try:
            num = int(user_input)
            try:
                tree.insert(num)
                print(f"Значение {num} добавлено.")
            except Exception as err:
                print("Ошибка:", err)
        except ValueError:
            print("Введенное значение не целое число.")
        continue
    if user_input[:2] == "2 ":
        user_input = user_input[2:].strip()
        try:
            num = int(user_input)
            if tree.delete(num):
                print(f"Значение {num} удалено.")
            else:
                print(f"Значение {num} не найдено.")
        except ValueError:
            print("Введенное значение не целое число.")
        continue
    if user_input[:2] == "3 ":
        user_input = user_input[2:].strip()
        try:
            num = int(user_input)
            if tree.find(num):
                print(f"Значение {num} в дереве присутствует.")
            else:
                print(f"Значение {num} не найдено.")
        except ValueError:
            print("Введенное значение не целое число.")
        continue