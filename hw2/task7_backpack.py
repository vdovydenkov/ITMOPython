# Define a constant
BACKPACK_SIZE = 5

objects = {
    "laptop": (3, 1500),
    "camera": (0.9, 800),
    "phone": (1, 600),
    "watch": (0.5, 300),
    "headphones": (0.3, 200),
    "tablet": (2, 900),
    "brended_pen": (0.08, 50),
    "wallet": (0.4, 100)
}

# Output a start line
print("-" * 30)
# Output the source data
print("Исходный список товаров:")
for thing, value in objects.items():
    weight, cost = value
    print(thing, f"вес: {weight}, цена: {cost}")

# Sort a objects by values (cost / weight)
objects = dict(sorted(objects.items(), key=lambda item: item[1][1]/item[1][0], reverse=True))

# Define some variables
backpack = {}
capacity = BACKPACK_SIZE
total_value = 0
total_weight = 0
# Filling the backpack
for thing, value in objects.items():
    weight, cost = value
    while round(capacity, 1) >= weight:
        # Check a key, if not exist - set to 0. Doing increment
        backpack[thing] = backpack.get(thing, 0) + 1
        total_value += cost
        total_weight += weight
        capacity -= weight

# Let's show the result
print("-" * 30)
print(f"Общая стоимость рюкзака: {total_value}, общий вес: {total_weight}")
print("состав:", backpack)

# Waiting for user
input("Нажмите Enter для завершения программы...")
