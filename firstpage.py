
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
    

# Example usage
nums = [-7, -3, 2, 3, 11]
solution = Solution()
print(solution.sortedSquares(nums))  # Output: [4,]()

                              


from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]  # fix 1: get the starting number
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            if start != nums[i]:
                ans.append(f"{start}->{nums[i]}")
            else:
                ans.append(str(nums[i]))

            i += 1  # fix 2: move to the next number

        return ans

# Example usage
solution = Solution()
print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))














from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i - 1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]

        return [l * r for l, r in zip(l_arr, r_arr)]

# Example usage:
sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

# Example usage
s = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = s.merge(intervals)
print(result)  # Output: [[1, 6], [8, 10], [15, 18]]

                



        
         
        
