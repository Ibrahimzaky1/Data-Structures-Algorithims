from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stk and height < stk[-1][0]:
                h, j = stk.pop()
                w = i - j
                a = h * w
                max_area = max(max_area, a)
                start = j

            stk.append((height, start))

        while stk:
            h, j = stk.pop()
            w = n - j
            max_area = max(max_area, h * w)

        return max_area


sol = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))  





from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x, y = m - 1, n - 1

        for z in range(m + n - 1, -1, -1):
            if x < 0:
                nums1[z] = nums2[y]
                y -= 1
            elif y < 0:
                break
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)  








from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1

        return n

nums = [3, 2, 2, 3]
val = 3

sol = Solution()
k = sol.removeElement(nums, val)
print("New length:", k)
print("Modified list:", nums[:k])  







from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 1

        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1

        return j


sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
length = sol.removeDuplicates(nums)
print("Length after removing duplicates:", length)
print("Modified array:", nums[:length])







from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        count = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[j] = nums[i]
                j += 1

        return j


sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
length = sol.removeDuplicates(nums)
print("Length after removing duplicates:", length)
print("Modified array:", nums[:length])

    








from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        n = len(prices)

        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            if i == n - 1:
                break
            lo = prices[i]
            i += 1

            
            while i < n and prices[i] >= prices[i - 1]:
                i += 1
            hi = prices[i - 1]

            profit += hi - lo

        return profit


sol = Solution()
prices = [7,1,5,3,6,4]
print("Max Profit:", sol.maxProfit(prices))
