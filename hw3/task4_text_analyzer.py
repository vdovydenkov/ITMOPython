# HW 3. Task 4. Analysis of a text

# Import for performing actions with path
import os

# Define the constant
PUNCTUATIONS = "!;:?.,"

def text_analysis(filename):
    '''
    Function returns a number of lines, words and symbols, and also the longest word size into filename.
    Argument: file name.
    Return the dictionary.
    '''

    result_dict = {}
    try:
        with open(filename, "r", encoding="utf-8") as text:
            lines = [line for line in text]
    except FileNotFoundError:
        result_dict["error"] = f"Ошибка: файл с именем {filename} не существует!"
    except Exception as err:
        result_dict["error"] = f"Возникла ошибка {err}"

    if result_dict.get("error", ""):
        return result_dict
    if len(lines) == 0:
        result_dict["error"] = "Файл пустой."
        return result_dict

    result_dict = {
        "lines": len(lines),
        "words": 0,
        "Symbols": 0,
        "longest_word": 0
    }
    for line in lines:
        # Symbols counter
        result_dict["Symbols"] += len(line.strip())
        # Clean the line
        line = "".join([symb if not symb in PUNCTUATIONS else " " for symb in line])
        # Split the line
        words = line.split()
        # Words counter
        result_dict["words"] += len(words)
        for word in words:
            if len(word) > result_dict["longest_word"]:
                result_dict["longest_word"] = len(word)
    return result_dict

user_filename = input("Введите имя файла:")
user_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), user_filename)

# Start the output
print("Анализируемый файл:", user_filename)
print("-" * 30)
result = text_analysis(user_filename)
if result.get("error", ""):
    print(result["error"])
else: # Output the result
    print(result)

# Waiting for user
input("Нажмите Enter для завершения программы...")
