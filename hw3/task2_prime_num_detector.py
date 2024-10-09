# HW 3. Task 2. Detect a prime number

def is_prime(integer):
    '''
    Detect a prime number
    Argument: integer
    None if argument is invalid
    '''

    if isinstance(integer, int):
        if integer < 2:
            return False
        if integer in [2, 3]:
            return True
        for divisor in range(2, (integer // 2) + 1):
            if integer % divisor == 0:
                return False
        return True
    return None

# Test the function
print("Список простых чисел до 100")
for i in range(100):
    if is_prime(i):
        print(i)

# Waiting for user
input("Нажмите Enter для завершения программы...")