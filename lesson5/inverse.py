# From now on i will rely on in build libraries

import numpy as np

matrix = np.random.randint(10, size=(3, 3))
for row in matrix:
    print(row)


# Finding the inverse of a matrix
def inverse_Matrix(matrix):
    determined = np.linalg.det(matrix)
    print(determined)
    # by using the in build function
    inverse = np.linalg.inv(matrix)
    print(inverse)


inverse_Matrix(matrix)
