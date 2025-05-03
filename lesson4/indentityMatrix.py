import numpy as np

mat1 = np.random.randint(10, size=(2, 2))
print(mat1)

# identity Matrix
mat2 = [[1, 0], [0, 1]]


def multiplication_matrices(mat1, mat2):
    # finding the dimentions
    m = len(mat1)
    n = len(mat1[0])
    p = len(mat2[0])
    print(m)
    print(n)
    print(p)

    if n != len(mat2):
        raise ValueError("Number of columns in A must equal number of rows in B")
    # initailize result matrix
    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += int(mat1[i][k] * mat2[k][j])
    return result


mul_matrix = multiplication_matrices(mat1, mat2)

for row in mul_matrix:
    print(row)
