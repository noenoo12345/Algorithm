max = 1000
A = [[0, 2, 4, max, max], [max, 0, 1, 5, max], [max, max, 0, 3, max], [max, max, max, 0, 8], [max, max, 2, max, 0]]
P = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
space = len(P)

for i in range(space):
    for j in range(space):
        if A[j][i] > 0:
            for k in range(space):
                if A[i][k] > 0:
                    dis = A[j][i] + A[i][k]
                    if (A[j][k] > dis):
                        A[j][k] = dis
                        P[j][k] = i + 1

print(P)
print(A)

def distance(i, j):
    middle = P[i-1][j-1]
    if (middle != 0):
        distance(i, middle)
        print(middle)
        distance(middle, j)
