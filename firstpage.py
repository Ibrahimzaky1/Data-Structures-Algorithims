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




from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]

s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))   # 1
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
print(s.findMin([11, 13, 15, 17]))  # 11





from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        min_i = l

        
        if target >= nums[0] and target <= nums[min_i - 1]:
            l, r = 0, min_i - 1
        else:
            l, r = min_i, n - 1

        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1


s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))  # Output: 4
print(s.search([4,5,6,7,0,1,2], 3))  # Output: -1
print(s.search([1], 0))             # Output: -1
print(s.search([1, 3], 3))          # Output: 1


class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n

        while L < R:
            M = (L+R) // 2
            if isBadVersion(m):
                R = M
            else:
                L = M + 1

        return L





def isBadVersion(version: int) -> bool:
    return version >= 4  

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n

        while L < R:
            M = (L + R) // 2
            if isBadVersion(M):  
                R = M
            else:
                L = M + 1

        return L


s = Solution()
print(s.firstBadVersion(5))  # Output: 4 (since version 4 is the first bad one)





class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num

        while l <= r:
            m = (l + r) // 2
            m_squared = m * m

            if num == m_squared:
                return True
            elif m_squared < num:
                l = m + 1
            else:
                r = m - 1

        return False


s = Solution()
print(s.isPerfectSquare(16))   # True
print(s.isPerfectSquare(14))   # False
print(s.isPerfectSquare(1))    # True
print(s.isPerfectSquare(808201))  # True (899^2)
print(s.isPerfectSquare(808202))  # False

