from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)
        i = 0

        while i < min_length:
            current_char = strs[0][i]
            for s in strs:
                if s[i] != current_char:
                    return strs[0][:i]
            i += 1

        return strs[0][:min_length]

# Test the function locally
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""





from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 0 coins to make amount 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    break
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
sol = Solution()
print(sol.coinChange([1, 2, 5], 11))  # Output: 3
print(sol.coinChange([2], 3))         # Output: -1










from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0: 0}

        def min_coins(amt):
            if amt in memo:
                return memo[amt]

            minn = float('inf')
            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    break
                minn = min(minn, 1 + min_coins(diff))  # FIXED this line

            memo[amt] = minn
            return minn

        result = min_coins(amount)
        return result if result < float('inf') else -1
sol = Solution()
print(sol.coinChange([1, 2, 5], 11))  # Output: 3 (5 + 5 + 1)
print(sol.coinChange([2], 3))         # Output: -1 (not possible)






class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sum
    
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6







from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {n - 1: True}

        def can_reach(i):
            if i in memo:
                return memo[i]

            furthest = min(i + nums[i], n - 1)
            for next_i in range(i + 1, furthest + 1):
                if can_reach(next_i):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return can_reach(0)

sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4]))  # Output: True (You can reach the last index)
print(sol.canJump([3, 2, 1, 0, 4]))  # Output: False (You get stuck at index 3)



from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1  # The index we want to reach

        for i in range(n - 1, -1, -1):
            if i + nums[i] >= target:
                target = i  # We can reach the current target from index i

        return target == 0  # If we can reach from index 0, return True

# Example usage:
sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4]))  # Output: True
print(sol.canJump([3, 2, 1, 0, 4]))  # Output: False











from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # dp[i] stores the length of the LIS ending at index i

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:  # FIXED: compare with nums[j]
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4 (LIS: [2, 3, 7, 101])
