import zipfile
import os
import sys

# Проверяем, передан ли путь к архиву
if len(sys.argv) < 2:
    print("Пожалуйста, укажите путь к архиву.")
    sys.exit(1)

# Путь к архиву из аргумента командной строки
zip_path = sys.argv[1]

# Путь к директории, куда будет разархивирован файл
extract_dir = os.path.join(os.getcwd(), 'data')

# Создаем директорию, если она не существует
os.makedirs(extract_dir, exist_ok=True)

# Открываем и разархивируем архив
with zipfile.ZipFile(zip_path, 'r') as archive:
    archive.extractall(extract_dir)

print(f'Архив разархивирован в {extract_dir}')
