matrix = [[0,1,0,0], [0,0,0,1], [0,0,0,0], [1,0,1,0]]

space = len(matrix)

for i in range(space):
    for j in range(space):
        if matrix[j][i]:
            for k in range(space):
                if matrix[i][k]:
                    matrix[j][k] = 1

print(matrix)