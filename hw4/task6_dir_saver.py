# Д.З. 4. Задание 6. Утилита для бэкапа.
import pathlib as pl
import shutil
from datetime import datetime
from time import sleep

# Определяем константы
PROMPT_SOURCE_DIR = "Введите исходную директорию для backup'а (пустой ввод для завершения программы):"
PROMPT_ARCHIVE_DIR = "Введите директорию для хранения backup'а (пустой ввод для завершения программы):"
PROMPT_TIMESLEEP = "С какой периодичностью повторять резервное копирование (в секундах):"
DATETIME_FORMAT = "%y_%m_%d_%H_%M_%S"
SOUND_NUMBER = 4

# Ввод имени исходной директории
while True:
    user_input = input(PROMPT_SOURCE_DIR)
    if not user_input: # Если ввели пустую строку
        exit()
    user_path = pl.Path(user_input)
    if user_path.is_dir(): # Если директория существует
        break
    print("Такой директории не существует.")
source_dir = user_path

# Ввод директории для хранения резервных копий
while True:
    user_input = input(PROMPT_ARCHIVE_DIR)
    if not user_input: # Если ввели пустую строку
        exit()
    user_path = pl.Path(user_input)
    if user_path.is_dir(): # Если директория существует
        if user_path == source_dir: # Если архивная совпадает с исходной
            print("Директория для архива совпадает с исходной. Выберите, пожалуйста, другую директорию.")
            continue
        break # Директория существует и не совпадает с исходной
    print("Такой директории не существует.")

# Ввод периода резервного копирования
while True:
    user_input = input(PROMPT_TIMESLEEP)
    try: # Пытаемся перевести в число
        time_sleep = int(user_input)
        if time_sleep < 0:
            print("Введите положительное число.")
            continue
        break # Ввели число и оно больше нуля
    except ValueError:
        print("Введите число.")
    except Exception as err:
        print("Возникла ошибка: ", err)
        exit()

print("-" * 30)
# Запускаем цикл копирования
while True:
    # Добавляем к архивному пути текущую дату и время
    now = datetime.now()
    now = now.strftime(DATETIME_FORMAT)
    archive_dir = user_path/ now
    print("Создаю директорию ", archive_dir.resolve())
    # Создаем директорию, разрешая создавать подкаталоги и разрешая игнорировать существование директории
    archive_dir.mkdir(parents=True, exist_ok=True)
    # Цикл по исходной директории
    for item in source_dir.iterdir():
        # Добавляем имя к архивной директории
        dest = archive_dir / item.name
        print("Копирую ", item.resolve())
        # Папку копируем отдельно, файл - отдельно
        if item.is_dir():
            shutil.copytree(item, dest, dirs_exist_ok=True)
        else:
            shutil.copy2(item, dest)
    print("-" * 30)
    print(f"Пауза {time_sleep} секунд. Нажмите Ctrl+C для завершения программы.")
    # Встаем на паузу.
    try:
        sleep(time_sleep)
    except KeyboardInterrupt:
        print("Завершаем программу.")
        exit()