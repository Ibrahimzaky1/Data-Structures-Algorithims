

####################### Lesson 7 #######################


A = [-3, -1, 0, 1, 4, 7]

if -1 in A:
    print(True)

def binary_seaarch(arr, target):

    N = len(A)
    L = 0
    R = N -1

    while L <= R:
        M = L + ((R-L) // 2)

        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1
    
    

    return False

binary_seaarch(A, 0)

B = [False, False, False, False, True, True, True]

def binary_search_condition(arr):
    N = len(arr)
    L = 0
    R = N -1

    while L < R:
        M = (L + R) // 2

        if B[M]:
            R = M
        else:
            L = M + 1

        return L
    
binary_search_condition(B)