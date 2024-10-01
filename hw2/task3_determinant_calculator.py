import numpy as np

# Get a data
square_matrix = [
    [5, 4, 3, 4],
    [-4, 25, 6, -7],
    [7, 38, 9, 11],
    [12, 15, 17, 18],
]

def check_for_matrix(checked_matrix):
    '''
    Validate a matrix.
    Arg: list of lists.
    '''
    
    # Check for types
    if not (isinstance(checked_matrix, list) and
            all(isinstance(row_of_matrix, list) for row_of_matrix in checked_matrix)):
        return 1
    matrix_size = len(checked_matrix)
    # Check for squeare: lengths of rows are equal
    if not all(matrix_size == len(row_of_matrix) for row_of_matrix in checked_matrix):
        return 2
    # Iterate through all rows of the matrix to check for numbers
    if not all(all(isinstance(value, (int, float)) for value in row_of_matrix) for row_of_matrix in checked_matrix):
        return 3
    return 0

def det_2x2_matrix(matrix_2x2):
    '''
    Calculate a 2x2 matrix determinant
    Arg: a list of lists
    Only a validated argument is needed!
    '''

    if not isinstance(matrix_2x2, list):
        print("det_2x2_matrix: Переданная матрица не список!")
        return None
    if len(matrix_2x2) != 2:
        print("det_2x2_matrix: Ошибка размера матрицы: ", len(matrix_2x2), "вместо 2!")
        return None
    if not all(all(isinstance(value, (int, float)) for value in row) for row in matrix_2x2):
        print("det_2x2_matrix: какое-то Значение в переданном списке не число!")
        return None
    a, b = matrix_2x2[0]
    c, d = matrix_2x2[1]
    return a*d - b*c

def det_matrix_calculator(matrix):
    '''
    The determinant of a square matrix Calculator.
    Arg: square matrix - list of values list.
    Only a validated argument is needed!
    '''
    
    matrix_size = len(matrix)
    if matrix_size == 1:
        # Matrix 1X1 case
        return matrix[0][0]
    if matrix_size == 2:
        # Matrix 2X2 case
        return det_2x2_matrix(matrix)
    determinant = 0
    # i - row, j - collumn
    j = 0
    for i in range(matrix_size):
        value = matrix[j][i]
        # Cut the collumn
        tmp_matrix = [(row[:i] + row[i+1:]) for row in matrix]
        # Cut the row
        tmp_matrix.pop(j)
        minor = det_matrix_calculator(tmp_matrix)
        cofactor = minor * ((-1) ** (i + j))
        determinant += value * cofactor
    return determinant

# Output a start line
print("-" * 30)

# Output the source data
print("Матрица для расчета определителя:")
for row in square_matrix:
    print(row)

# Validate the matrix
match check_for_matrix(square_matrix):
    case 0: # Validated data
        det = det_matrix_calculator(square_matrix)
        print("-" * 30)
        print("Определитель равен", det)
    case 1:
        print("Некорректные данные: это не список списков!")
    case 2:
        print("Некорректные данные: размер списков не совпадает, матрица не квадратная!")
    case 3:
        print("Некорректные данные: не все значения являются числами!")
    case _:
        print("Некорректные данные!")

# Verifing a result by numpy
np_matrix = np.array(square_matrix)
np_determinant = np.linalg.det(np_matrix)
print("Определитель, рассчитанный numpy: ", np_determinant)

# Output final line
print("-" * 30)

# Waiting for user
input("Нажмите Enter для завершения программы...")