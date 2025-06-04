

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0 
        r = n - 1
        max_area = 0

        while l < r:
            w = r - l  # ✅ Corrected width
            h = min(height[l], height[r])
            a = w * h
            max_area = max(max_area, a)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

# Example usage
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49






from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        L = 0
        R = n - 1

        while L < R:
            if not s[L].isalnum():
                L += 1  # Fixed typo here
                continue

            if not s[R].isalnum():
                R -= 1
                continue

            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1

        return True

# Example usage:
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(sol.isPalindrome("race a car"))                      # Output: False







from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            if nums[i] > 0:
                break  # No valid triplet can sum to 0 if the smallest number is > 0
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicates for nums[i]

            lo, hi = i + 1, n - 1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif summ < 0:
                    lo += 1
                else:
                    hi -= 1

        return answer

# 🔹 Example usage:
sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]









from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l + 1, r + 1]  # 1-based index
            elif summ < target:
                l += 1
            else:
                r -= 1

# 🔹 Example usage:
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]





from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        l, r = 0, n - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

# Example usage:
s = ["h", "e", "l", "l", "o"]
Solution().reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']



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

                              



