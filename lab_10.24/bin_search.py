WORDS = "tree, mountain, river, cloud, book, chair, light, window, phone, mirror, sky, dream, road, smile, shadow"

def str_to_int(s):
    string_of_codes = "".join([str(ord(char)) for char in s])
    print(str)
    return int(string_of_codes)

words_list = [word.strip() for word in WORDS.split(",")]
codes_list = [str_to_int(word) for word in words_list]
words_dict = dict(zip(codes_list, words_list))

print("Список слов:", *words_list)

print("-" * 30)

sorted_words_dict = dict(sorted(words_dict.items()))

words_list = list(sorted_words_dict.items())

user_input = input("Введите слово для поиска:")
code_for_searching = str_to_int(user_input)

upper_bound = len(words_list) - 1
lower_bound = 0
median = len(words_list) // 2

while lower_bound <= upper_bound:
    middle_code, middle_word = words_list[median]
    if code_for_searching == middle_code:
        break
    if code_for_searching > middle_code:
        lower_bound = median + 1
    else:
        upper_bound = median - 1
    median = (lower_bound + upper_bound) // 2

if lower_bound > upper_bound:
    print("Слово не найдено.")
else:
    print("Слово в списке под номером", median)

input("Нажмите Enter для завершения программы...")