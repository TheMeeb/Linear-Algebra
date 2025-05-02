import numpy as np

mat1 = np.random.randint(10, size=(2, 2))
mat2 = np.random.randint(10, size=(2, 2))
print(mat1)
print(mat2)


def add_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(int(mat1[i][j] + mat2[i][j]))
        result.append(row)
    return result


sum_matrix = add_matrices(mat1, mat2)
for row in sum_matrix:
    print(row)
