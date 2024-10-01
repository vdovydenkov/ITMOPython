# HW 2. Task 2. Concatinate some two lists

# Some constants
STOP_STRING = ""

# Get a data
print("Введите два списка с одинаковым количество значений.")
print(f"Введите значения первого списка ('{STOP_STRING}' - для завершения):", end=" ")
list1 = [value for value in iter(input, STOP_STRING)]
print(f"\nВведите значения второго списка ('{STOP_STRING}' - для завершения):", end=" ")
list2 = [value for value in iter(input, STOP_STRING)]

# Output a start line
print("-" * 30)
# Output the data
print("Первый список:", list1, " Размер:", len(list1))
print("Второй список:", list2, " Размер:", len(list2))

if len(list1) == len(list2):
    # Create a empty result
    result_list = []

    # Get a pair values
    for value1, value2 in zip(list1, list2):
        result_list.append(value1)
        result_list.append(value2)
    # Output the result
    print("Результат слияния: ", result_list)
else:
    print("Списки не равны!")

# Output final line
print("-" * 30)

# Waiting for user
input("Нажмите Enter для завершения программы...")
