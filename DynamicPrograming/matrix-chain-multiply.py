import numpy as np

# maxValue = np.iinfo(np.int64).max
maxValue = 10000000

##################### INPUT ########################s

numOfMatrix = 4
# Array of matrix is flattened
arrDimension = np.array([10, 5, 15, 25, 20])       

#################### END INPUT #####################

# Array of optimal value of matrix multiply
matrixCost = np.full((numOfMatrix, numOfMatrix), maxValue, dtype=np.int64)  
# Array of index devide for optimal value
matrixIndexDivide = np.zeros((numOfMatrix, numOfMatrix), dtype=np.int16)    

def createMatrixChain(arrDimension, matrixCost, matrixIndexDivide):
    length = len(arrDimension) - 1  # number of matrix
    for i in range(length):
        matrixCost[i][i] = 0
    
    # l is length of the chain = number of matrix
    for l in range(2, length + 1):
        for startPoint in range(length - l + 1):
            endPoint = startPoint + l - 1
            for index in range(startPoint, endPoint):
                value = matrixCost[startPoint][index] + matrixCost[index + 1][endPoint] \
                + arrDimension[startPoint] * arrDimension[index + 1] * arrDimension[endPoint + 1]  
                if value < matrixCost[startPoint][endPoint]:
                    matrixCost[startPoint][endPoint] = value
                    matrixIndexDivide[startPoint][endPoint] = index + 1


def getOrder(demand, matrixIndexDivide):
    start, end = demand
    divideLocation = matrixIndexDivide[start - 1][end - 1]
    if (start == end - 1):      # Stop condition where only two matrix
        return "A" + str(start) + "A" + str(end)
    
    if (start == divideLocation):       # Take first matrix and multiply with remain
        return "A" + str(start) + "(" + getOrder((start + 1, end), matrixIndexDivide) + ")"
    elif (end == divideLocation + 1):   # Take last matrix and multiply with remain
        return "(" + getOrder((start, divideLocation), matrixIndexDivide) + ")" + "A" + str(end)
    else:                               # Devide to two part of multiply
        return "(" + getOrder((start, divideLocation), matrixIndexDivide) + ")" + \
            "(" + getOrder((divideLocation + 1, end), matrixIndexDivide) + ")"
    

createMatrixChain(arrDimension, matrixCost, matrixIndexDivide)
order = getOrder((1,numOfMatrix), matrixIndexDivide)
print(order)









    
