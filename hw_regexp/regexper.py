# Скрипт разархивирует файл atlas_shrugged.zip из папки со скриптом
# И отыскивает в нем соответствия регулярным выражениям

import zipfile
import os
import re

# Константы регулярных выражений
REGEXPS = [
    # Слово из 20 и более букв
    r'[А-я]{20,}',
    # Предложения со словом человечество во всех словоформах
    r'.*?\bчеловечеств[а-я]*\b.*?[.!?]',
    # Любые повторяющиеся через тире слова
    r'\b([А-я]+)-\1+\b'
]

def print_matches(regexp, content):
    matches = re.findall(regexp, content)
    if len(matches) > 0:
        # Приводим к нижнему регистру
        matches = [match.lower() for match in matches]
        # Выбираем уникальные значения
        unique_matches = list(set(matches))
        print(f'Найдено {len(matches)} совпадений по выражению `{regexp}`\nВывод 10 уникальных элементов:')
        print('-' * 30)
        for index in range(10):
            if index == len(unique_matches):
                break
            print(unique_matches[index])
        print('-' * 30)
    else:
        print(f'Совпадений с выражением {regexp} не найдено.')

    return

# Путь к архиву
zip_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'atlas_shrugged.zip')

# Путь к директории, куда будет разархивирован файл
extract_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# Создаем директорию, если она не существует
os.makedirs(extract_dir, exist_ok=True)

# Открываем и разархивируем архив
with zipfile.ZipFile(zip_filepath, 'r') as archive:
    archive.extractall(extract_dir)

# Берем содержимое директории extract_dir и фильтруем только файлы
ls = os.listdir(extract_dir)
files = [f for f in ls if os.path.isfile(os.path.join(extract_dir, f))]
# Формируем полный путь к файлу
filepath = os.path.join(extract_dir, files[0])

with open(filepath, 'r', encoding='utf-8') as file:
    text= file.read()

# Выводим все совпадения по всем regexp
[print_matches(regexp, text) for regexp in REGEXPS]

# Удаляем файл и директорию
os.remove(filepath)
os.rmdir(extract_dir)

# Ожидаем реакции пользователя
input('Нажмите Enter для завершения программы...')
