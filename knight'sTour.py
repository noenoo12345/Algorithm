arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

a = [1,2,2,1,-1,-2,-2,-1]
b = [2,1,-1,-2,-2,-1,1,2]
c = False
count = 0

def tour(i, x, y, q1):
    global count
    if (i == 1):
        arr[x][y] = i
        i = i + 1
    k = 0
    while (k < 8 and not q1):
        u = x + a[k]
        v = y + b[k]
        k = k + 1
        if ( 0 <= u <= 4 and 0 <= v <= 4):
            if arr[u][v] == 0:
                count += 1
                arr[u][v] = i
                if i < 25:
                    q1 = tour(i + 1, u, v, q1)
                    if not q1: 
                        arr[u][v] = 0
                else:
                    print(arr)
                    print(count)
                    return True
    return q1

tour(1, 1, 1, False)