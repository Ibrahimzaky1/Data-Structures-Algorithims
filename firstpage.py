

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


####################### Lesson 7 #######################

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

    def __str__(self):
        return str(self.val)
    

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print(A)

def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)


def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)


def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)

    pre_order_iterative(A)




########################## Lesson 9 ##########################

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq
heapq.heapify(A)

A

heapq.heappush(A, 4)

A

minn = heapq.heappop(A)

A, minn

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn

    return new_list

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

heapq.heappushpop(A, 99)

print(A)


B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)

for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)

print(B)

largest = heapq.heappop(B)

print(largest)

heapq.heappush(B, -7)

print(B)

C = [-5, 4, 2, 1, 7, 0, 3]

heap = []

for x in C:
    heapq.heappush(heap, x)
    print(heap, len(heap))


print(C)


D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter

Counter = Counter(D)

print(Counter)

heap = []

for k, v in Counter.items():
    heapq.heappush(heap, (k, v))

print(heap)


########################## Lesson 10 ##########################

#Bubble_sort

A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr [i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]

bubble_sort(A)
print(A)

#insertion Sort

B = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr [j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

insertion_sort(B)
print(B)

# selection Sort

C = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(C)
print(C)

#Merge Sort

D = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    m = n // 2
    L = merge_sort(arr[:m])
    R = merge_sort(arr[m:])
    
    l, r = 0, 0
    sorted_arr = []

    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            sorted_arr.append(L[l])
            l += 1
        else:
            sorted_arr.append(R[r])
            r += 1

    # Append remaining elements
    while l < len(L):
        sorted_arr.append(L[l])
        l += 1

    while r < len(R):
        sorted_arr.append(R[r])
        r += 1

    return sorted_arr

print(merge_sort(D))

# Quick Sort

E = [-5, 3, 2, 1, -3, -3, 7, 2, 2]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[-1]

    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + [p] + R

quick_sort(E)

# Counting Sort

def counting_sort(arr):
    if not arr:
        return

    maxx = max(arr)
    counts = [0] * (maxx + 1)

    for x in arr:
        counts[x] += 1

    i = 0
    for c in range(len(counts)):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1


