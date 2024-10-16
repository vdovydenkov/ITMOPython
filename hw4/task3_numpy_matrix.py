# Д.З. 4. Задание 3. Работа с матрицами в numpy
import numpy as np

matrix = np.random.randint(low=0, high=10, size=(10, 10))

print("Случайная матрица 10X10, с целыми числами от 0 до 10")
print(matrix)

det = np.linalg.det(matrix)
print("-" * 30)
print("Определитель матрицы равен ", det)

print("-" * 30)
print("Транспонированная матрица")
print(matrix.T)

rang = np.linalg.matrix_rank(matrix)
print("-" * 30)
print("Ранг матрицы равен ", rang)

values, vectors = np.linalg.eig(matrix)
print("-" * 30)
print("Собственные значения")
print(values)
print("-" * 30)
print("Собственные векторы")
print(vectors)

matrix2 = np.random.randint(low=0, high=10, size=(10, 10))
print("-" * 30)
print("Случайная матрица для операций сложения и умножения матриц")
print(matrix2)

print("-" * 30)
print("Результат сложения матриц")
print(matrix + matrix2)

print("-" * 30)
print("Результат умножения матриц")
print(matrix @ matrix2)

# Ждем реакции пользователя
input("Нажмите Enter для завершения программы...")