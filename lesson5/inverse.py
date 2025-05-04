import numpy as np

matrix = np.random.randint(10, size=(2, 2))
for row in matrix:
    print(row)


def inverse_2x2(matrix):
    if matrix.shape != (2, 2):
        raise ValueError("Only 2x2 matrices are supported.")

    a, b = matrix[0]
    c, d = matrix[1]

    det = a * d - b * c
    if det == 0:
        raise ValueError("Matrix is singular and not invertible.")

    inverse = (1 / det) * np.array([[d, -b], [-c, a]])
    return inverse


inverse = inverse_2x2(matrix)
for row in inverse:
    print(row)

# From now on i will rely on in build libraries
matrix2 = np.random.randint(10, size=(3, 3))
for row in matrix2:
    print(row)


# Finding the inverse of a matrix other then 2x2
def inverse_Matrix(matrix2):
    determined = np.linalg.det(matrix)
    print(determined)
    # by using the in build function
    inverse = np.linalg.inv(matrix)
    print(inverse)


inverse_Matrix(matrix2)
