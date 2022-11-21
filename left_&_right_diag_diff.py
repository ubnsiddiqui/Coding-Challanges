def diaDiff(mat):
    rows = len(mat)
    columns = len(mat[0])
    left_diag_sum = 0
    right_diag_sum = 0
    abs_dif = 0
    if rows != columns:
        print('Array should Be Square')
    else:
        for i in range(rows):
            for j in range(rows):
                if i == j:
                    left_diag_sum = left_diag_sum + mat[i][j]
                    break
        for k in range(rows):
            for l in range(rows):
                if k + l == rows-1:
                    right_diag_sum = right_diag_sum + mat[k][l]
                else:
                    continue
    abs_dif = abs(left_diag_sum - right_diag_sum)

    return abs_dif
print(diaDiff([[1,2,3],[4,5,6],[9,8,9]]))
            
