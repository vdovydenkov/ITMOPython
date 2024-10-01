# Get a dictionary
source_dict = {'a': 1, 'b': 2, 'c': 3}

result_dict = dict(zip(source_dict.values(), source_dict.keys()))

# Let's show the result
print("-" * 30)
print("Исходный словарь:\n", source_dict)
print("Результат перестановки ключей и значений:\n", result_dict)
print("-" * 30)

# Waiting for user
input("Нажмите Enter для завершения программы...")
