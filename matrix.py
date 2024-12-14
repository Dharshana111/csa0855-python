def matrix_addition(mat1, mat2):
    mat_sum = []

    for i in range(len(mat1)):
        row_sum = []
        for j in range(len(mat1[i])):
            row_sum.append(mat1[i][j] + mat2[i][j])
        mat_sum.append(row_sum)

    return mat_sum

mat1 = [[1, 2], [5, 3]]
mat2 = [[2, 3], [4, 1]]

mat_sum = matrix_addition(mat1, mat2)

for row in mat_sum:
    print(" ".join(map(str, row)))
