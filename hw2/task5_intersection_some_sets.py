# Get a data: list of sets
list_of_sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]

# Output a header
print("-" * 30)
print("Исходный список множеств")

result_set = list_of_sets[0]
for next_set in list_of_sets:
    result_set = next_set.intersection(result_set)
    print(next_set)

print("-" * 30)
# Let's show the result
print("Пересечение:", result_set)
# Final line
print("-" * 30)

# Waiting for user
input("Нажмите Enter для завершения программы...")
