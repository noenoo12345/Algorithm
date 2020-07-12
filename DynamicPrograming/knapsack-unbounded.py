name = ["A","B","C","D"]
size = [3,5,4,7]
val = [5,10,9,13]
cost = []
best = []
capacity = 12

for i in range(capacity + 1):
    cost.append(0)
    best.append(0)

for j in range(len(size)):
    for i in range(1, capacity + 1):
        if (i >= size[j]):
            newValue = cost[i - size[j]] + val[j]
            if cost[i] < newValue:
                cost[i] = newValue
                best[i] = j

print(cost)
print([i + 1 for i in best[3:]])  

# while capacity > 0:
#     print(name[best[capacity]])
#     capacity = capacity - size[best[capacity]]

