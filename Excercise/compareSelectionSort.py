arr = [1, 30, 6, 4, 3032]

def compare(a, b):
    arr1 = str(a)
    arr2 = str(b)
    length = len(arr1) if len(arr1) > len(arr2) else len(arr2)

    for i in range(length):
        if (int(arr1[i % len(arr1)]) > int(arr2[i % len(arr2)])):
            return True
        elif (int(arr1[i % len(arr1)]) < int(arr2[i % len(arr2)])):
            return False

for i in range(len(arr)):
    max = arr[i]
    for j in range(i, len(arr)):
        if (not compare(max, arr[j])):
            max = arr[j]
    
    k = arr.index(max)
    arr[k] = arr[i]
    arr[i] = max

print(arr)
    



    