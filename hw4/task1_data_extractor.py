# Д.З. 4. Задание 1. Извлечь из файла e-mail и телефоны и записать в новый файл.
import os
import re

# Имя выходного файла
OUTPUT_FILENAME = "data_extractor_result.txt"
# Разделитель данных в выходном файле
SEPARATOR = "\n"
# Заголовок
TITLE = "Data_Extractor извлекает e-mail и телефоны из файла и записывает в файл " + OUTPUT_FILENAME
# Приглашение
PROMPT = "Введите имя файла:"

# Регулярные выражения для выборки
regexps = [
           # Шаблон для e-mail
           r"[a-zA-Zа-яА-Я0-9._%+-]+@[a-zA-Zа-яА-Я0-9.-]+\.[a-zA-Zа-яА-Я]{2,}",
           # Шаблон для телефона в формате +7...
           r"\+7\d{10}",
           # Шаблон для телефона в формате 8...
           r"8\d{10}",
           # Шаблон для телефона в формате XXX-XX-XX
           r"\d{3}\-\d{2}\-\d{2}"
]          

print(TITLE)
user_filename = input(PROMPT)
# Добавляем путь к имени файла
user_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), user_filename)

# Строка перед выводом
print("-" * 30)

try: # Пытаемся открыть на чтение
    with open(user_filename, "r", encoding="utf-8") as file:
        # Считываем файл
        source_text = [line for line in file]
except FileNotFoundError:
    print("Файл не найден.")
    exit()
except Exception as err:
    print("Ошибка чтения файла: ", err)
    exit()

try: # Пытаемся открыть на запись
    # Добавляем путь к имени выходного файла
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), OUTPUT_FILENAME)
    print("Создаем файл ", filename)
    with open(filename, "w", encoding="utf-8") as file:
        print("Выбранные данные:")
        # Проходим по строкам исходного текста
        for line in source_text:
            # Перебираем все регулярные выражения
            for regexp in regexps:
                # Ищем выражение в строке
                result = re.findall(regexp, line)
                if result: # Если нашли
                    print(*result)
                    # Добавляем разделитель
                    result = [line + SEPARATOR for line in result]
                    file.writelines(result)
except Exception as err:
    print(f"Не удалось записать в файл {filename}. Ошибка: {err}")
    exit()

input("Нажмите Enter для завершения программы...")