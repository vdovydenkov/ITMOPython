# HW 2. Task 2. Get sorted and filtered ages

# Output start line
print("-" * 30)

# Define some constants
FILTERED_FIELD = 1 # Number of list's field
BOTTOM_AGE = 18 # The bottom of age for filtering

# Get a data
data = [
    ("Игорь", 25),
    ("Андрей", 61),
    ("Наталья", 16),
    ("Дмитрий", 12),
    ("Николай", 37)
]

# Output raw data
print("Исходные данные: ", data)
# Output a conditions of task
print(f"Фильтруем список по полю {FILTERED_FIELD + 1}: оставляем старше {BOTTOM_AGE}, и сортируем его в обратном порядке.")

filtered_list = [item for item in data if item[FILTERED_FIELD] > BOTTOM_AGE]
filtered_list.sort(key=lambda item: item[FILTERED_FIELD], reverse=True)

# Output a result
print("Результат: ", filtered_list)

# Output final line
print("-" * 30)

# Waiting for user
input("Нажмите Enter для завершения программы...")
