# Define the constant
PUNCTUATIONS = "!;:?.,"

# Get a data: a long string
s = "Мистер и миссис Дурсль проживали в доме номер четыре по Тисовой улице и всегда с гордостью заявляли, что они, слава богу, абсолютно нормальные люди. Уж от кого-кого, а от них никак нельзя было ожидать, чтобы они попали в какую-нибудь странную или загадочную ситуацию. Мистер и миссис Дурсль весьма неодобрительно относились к любым странностям, загадкам и прочей ерунде."

# Output a start line
print("-" * 30)
# Output a source string
print("Исходный текст:\n", s)

# Low the string
s = s.lower()
# Remove a punctuation
s = "".join([symb for symb in s if not symb in PUNCTUATIONS])

# Let's show the result
print("-" * 30)
print("Привели к нижнему регистру и удалили знаки препинания:\n", s)

# Split the string
words = s.split()

words_dictionary = {}
for word in words:
    words_dictionary[word] = words.count(word)

sorted_words_dict = dict(sorted(words_dictionary.items(), key=lambda item: item[1], reverse=True))

# Output the result
print("-" * 30)
print("Отсортированный список слов и количество вхождений слова в строку:")
for key, value in sorted_words_dict.items():
    print(key, value)

# Waiting for user
input("Нажмите Enter для завершения программы...")
