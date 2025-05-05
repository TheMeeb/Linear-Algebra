import numpy as np

matrix = np.array([[1, 2], [3, 4]])
print(matrix)


def transpose_Matrix(matrix):
    # Using inbuild library to do so
    transpose = np.matrix_transpose(matrix)
    return transpose


# mutate the object
matrix = transpose_Matrix(matrix)
print(matrix)
