# HW 3. Task 3. own_map function
import types # For type validation

def own_map(some_list, some_func):
    '''
    The map function own implementation.
    Args: list, function
    None if argument is invalid.
    '''
    if not isinstance(some_list, list) \
       or not isinstance(some_func, types.FunctionType):
        return None
    return list([some_func(value) for value in some_list])

# Test the function
print("Тест функции own_map")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]
own_map_result = own_map(numbers, lambda x: x*2)
if own_map_result == None:
    print("Задан неверный параметр функции own_map.")
    exit()

print("Исходный список:", *numbers)
print("Результат применения функции (умножение на 2):", *own_map_result)

# Waiting for user
input("Нажмите Enter для завершения программы...")
