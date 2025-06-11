

from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t in '+-*/':
                b, a = stk.pop(), stk.pop()

                if t == '+':
                    stk.append(a + b)
                elif t == '-':
                    stk.append(a - b)
                elif t == '*':
                    stk.append(a * b)
                else:  # division with truncation toward zero
                    stk.append(int(a / b))

            else:
                stk.append(int(t))  # convert token to int

        return stk[0]

# Example usage
s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
print(s.evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # Output: 22


class MinStack:
    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
        elif self.min_stk[-1] < val:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
    

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2




class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1

            else:
                left = middle + 1

        return -1
    
s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))   
print(s.search([-1, 0, 3, 5, 9, 12], 2))


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        return l  
    
s = Solution()
print(s.searchInsert([1,3,5,6], 5))  # Output: 2
print(s.searchInsert([1,3,5,6], 2))  # Output: 1
print(s.searchInsert([1,3,5,6], 7))  # Output: 4
print(s.searchInsert([1,3,5,6], 0))  # Output: 0


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            i = mid // cols
            j = mid % cols
            mid_val = matrix[i][j]

            if mid_val == target:
                return True
            elif target < mid_val:
                right = mid - 1
            else:
                left = mid + 1

        return False


s = Solution()
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

print(s.searchMatrix(matrix, 3))    # True
print(s.searchMatrix(matrix, 13))   # False
