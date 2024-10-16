# HW 3. Task 5. Merge some files
import os

# Some constants
STOP_STRING = "."
RESULT_FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "merged_text.txt")
# Errors
NOT_A_LIST_ERROR = 1
NOT_A_BOOL_ERROR = 2
EMPTY_LIST_ERROR = 3
FILE_NOT_FOUND_ERROR = 4
EMPTY_RESULT_ERROR = 5
WRITE_ERROR = 6

def merge_files(files_list, need_save=True):
    '''
    Collect files to string.
    If the second argument is True, save the string to a file.
    Args: file paths list, Need save - boolean.
    Return 0 to success or error code.
    '''

    if not isinstance(files_list, list):
        return NOT_A_LIST_ERROR
    if not isinstance(need_save, bool):
        return NOT_A_BOOL_ERROR
    if len(files_list) == 0:
        return EMPTY_LIST_ERROR
    error_code = 0
    result = ""
    # Takes a filename from list
    for file in files_list:
        try:
            with open(file, "r", encoding="utf-8") as f:
                # Add a new text
                result += f.read()
        except FileNotFoundError:
            error_code = FILE_NOT_FOUND_ERROR
    if not result:
        # If result is empty and there are no errors
        if error_code == 0:
            return EMPTY_RESULT_ERROR
        else:
            return error_code
    else: # The result is not empty
        # Write to file
        try:
            with open(RESULT_FILENAME, "w", encoding="utf-8") as f:
                f.write(result)
        except:
            return WRITE_ERROR
        return result

# Test the function
# Get a data
print("Введите список файлов для объединения.")
files_list = []
while True:
    user_filepath = input(f"Введите путь к файлу ()'{STOP_STRING}' - для завершения):")
    if user_filepath == STOP_STRING:
        break
    files_list.append(user_filepath)

# Output the start line
print("-" * 30)

# Call the function
merged_text = merge_files(files_list)
if isinstance(merged_text, str):
    print("Результат слияния:")
    print(merged_text)
elif merged_text == NOT_A_LIST_ERROR:
    print("Первый параметр функции долджен быть списком: список путей к объединяемым файлам.")
elif merged_text == NOT_A_BOOL_ERROR:
    print("Второй параметр функции должен быть boolean: записать ли результат в файл (True/False).")
elif merged_text == EMPTY_LIST_ERROR:
    print("В функцию передан пустой список.")
elif merged_text == FILE_NOT_FOUND_ERROR:
    print("Файл не найден.")
elif merged_text == EMPTY_RESULT_ERROR:
    print("Файлы не содержат текста.")
elif merged_text == WRITE_ERROR:
    print("Ошибка записи в файл:", RESULT_FILENAME)

# Waiting a user
input("Нажмите Enter для завершения программы...")