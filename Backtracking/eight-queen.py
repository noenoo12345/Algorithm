horizontal = [False, False, False, False, False, False]
diagonal_1 = [False, False, False, False, False, False, False, False, False, False, False]
diagonal_2 = [False, False, False, False, False, False, False, False, False, False, False]
result = [-1, -1, -1, -1, -1, -1]
length = 6



# def queen(i, flag):
#     j = 0
#     while (j < length and not flag):
#         if not (horizontal[j] or diagonal_1[i + j] or diagonal_2[i - j + length - 1]):
#             result[i] = j
#             horizontal[j] = True
#             diagonal_1[i + j] = True
#             diagonal_2[i - j + length - 1] = True
#             if (i < length - 1):
#                 flag = queen(i + 1, flag)
#                 if (not flag):
#                     result[i] = -1
#                     horizontal[j] = False
#                     diagonal_1[i + j] = False
#                     diagonal_2[i - j + length - 1] = False
#             else:
#                 flag = True
#         j += 1
#     return flag

def queen(i):
    j = 0
    while (j < length):
        if not (horizontal[j] or diagonal_1[i + j] or diagonal_2[i - j + length - 1]):
            result[i] = j
            horizontal[j] = True
            diagonal_1[i + j] = True
            diagonal_2[i - j + length - 1] = True
            if (i == length - 1):
                print(result)
            queen(i + 1)
            result[i] = -1
            horizontal[j] = False
            diagonal_1[i + j] = False
            diagonal_2[i - j + length - 1] = False  
        j += 1
    
queen(0)

