from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        answer = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                lo, hi = j + 1, n - 1

                while lo < hi:
                    summ = nums[i] + nums[j] + nums[lo] + nums[hi]

                    if summ == target:
                        answer.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1

                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1

                    elif summ < target:
                        lo += 1
                    else:
                        hi -= 1

        return answer


sol = Solution()
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))




class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i+1, n-1
            while lo < hi:
                cur_sum = nums[i] + nums[0] + nums[hi]
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum

                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    lo += 1
                else:
                    hi -= 1

        return closest_sum
    




from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]
        for color in nums:
            counts[color] += 1

        R, W, B = counts
        nums[:R] = [0] * R
        nums[R:R + W] = [1] * W
        nums[R + W:] = [2] * B



sol = Solution()
nums = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums)
print(nums)  


