A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# Find the number of nodes
n = max(max(u, v) for u, v in A) + 1

# Initialize n x n matrix with 0s
M = []
for i in range(n):
    M.append([0] * n)

# Fill adjacency matrix
for u, v in A:
    M[u][v] = 1

# Output
print("Adjacency list:", A)
print("Adjacency matrix:")
for row in M:
    print(row)

from collections import defaultdict

D = defaultdict(list)

for  u, v in A:
    D[u].append(v)


def dfs_recursive(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)

print(D)

source = 0 

seen = set()
seen.add(source)
dfs_recursive(source)


source = 0 

seen = set()
seen.add(source)
stack = [source]

while stack:
    node = stack.pop()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)


source = 0

from collections import deque

seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)



class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        
    def __str__(self):
        return f'Node({self.value})'
    def display(self):
        connections = [node.value for node in self.neighbors]
        return f'{self.value} is connected to: {connections}'
    
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)

A.display()

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1

        result.reverse()
        return result




####################### LESSON 13 ########################

#Sliding Window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            sett.add(s[r])
            w = r - l + 1
            longest = max(longest, w)

        return longest


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[1]

        max_avg = cur_sum / k
        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]

            avg = cur_sum / k
            max_avg = max(max_avg. avg)

        return max_avg


