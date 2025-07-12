from typing import List

class SolutionMemo:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {0: 0, 1: 0}

        def min_cost(i):
            if i in memo:
                return memo[i]
            memo[i] = min(cost[i - 1] + min_cost(i - 1),
                          cost[i - 2] + min_cost(i - 2))
            return memo[i]

        return min_cost(n)


cost1 = [10, 15, 20]
sol_memo = SolutionMemo()
print("Memoization result:", sol_memo.minCostClimbingStairs(cost1))  







class SolutionDP:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]


cost2 = [10, 15, 20]
sol_dp = SolutionDP()
print("DP result:", sol_dp.minCostClimbingStairs(cost2))  




from typing import List
class SolutionMemo:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        memo = {0: nums[0], 1: max(nums[0], nums[1])}
        
        def helper(i):
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + helper(i - 2), helper(i - 1))
            return memo[i]
        
        return helper(n - 1)


nums1 = [2, 7, 9, 3, 1]
sol_memo = SolutionMemo()
print("Memoization Result:", sol_memo.rob(nums1))  



class SolutionDP:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        prev = nums[0]
        curr = max(nums[0], nums[1])
        
        for i in range(2, n):
            prev, curr = curr, max(nums[i] + prev, curr)
        
        return curr


nums2 = [2, 7, 9, 3, 1]
sol_dp = SolutionDP()
print("DP Result:", sol_dp.rob(nums2))  






class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def paths(i, j):
            if i == j == 0:
                return 1
            elif i < 0 or j < 0 or i == m or j == n:
                return 0
            else:
                return paths(i, j-1) + paths(i-1, j)
        
        return paths(m-1, n-1)
            




from typing import Tuple

class SolutionMemo:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {(0, 0): 1}
        
        def paths(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            memo[(i, j)] = paths(i - 1, j) + paths(i, j - 1)
            return memo[(i, j)]

        return paths(m - 1, n - 1)


sol1 = SolutionMemo()
print("Memoization Result:", sol1.uniquePaths(3, 7))  



class SolutionDP:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                val = 0
                if i > 0:
                    val += dp[i - 1][j]
                if j > 0:
                    val += dp[i][j - 1]
                dp[i][j] = val

        return dp[m - 1][n - 1]

sol2 = SolutionDP()
print("DP Result:", sol2.uniquePaths(3, 7))  











from typing import List

class SolutionMemo:
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
                candidate = min_coins(diff)
                if candidate != float('inf'):
                    minn = min(minn, 1 + candidate)

            memo[amt] = minn
            return minn

        result = min_coins(amount)
        return result if result < float('inf') else -1


class SolutionDP:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    break
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] < float('inf') else -1



coins = [1, 2, 5]
amount = 11

sol1 = SolutionMemo()
print("Memoization Result:", sol1.coinChange(coins, amount))  

sol2 = SolutionDP()
print("Tabulation Result:", sol2.coinChange(coins, amount))   










from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sum


sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", sol.maxSubArray(nums))  











from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {n - 1: True}

        def can_reach(i):
            if i in memo:
                return memo[i]

            max_jump = nums[i]
            for jump in range(1, max_jump + 1):
                if i + jump < n and can_reach(i + jump):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return can_reach(0)



sol = Solution()
nums = [2, 3, 1, 1, 4]
print("Can jump to end:", sol.canJump(nums))  

nums2 = [3, 2, 1, 0, 4]
print("Can jump to end:", sol.canJump(nums2))  

        




from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1

        for i in range(n - 1, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= target:
                target = i

        return target == 0



sol = Solution()
nums = [2, 3, 1, 1, 4]
print("Can jump to end:", sol.canJump(nums))  

nums2 = [3, 2, 1, 0, 4]
print("Can jump to end:", sol.canJump(nums2))  








from typing import List

class Solution:
    def LengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)



sol = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of LIS:", sol.LengthOfLIS(nums))  








from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        @cache
        def longest(i, j):
            if i == m or j == n:
                return 0
            elif text1[i] == text2[j]:
                return 1 + longest(i + 1, j + 1)
            else:
                return max(longest(i, j + 1), longest(i + 1, j))

        return longest(0, 0)



sol = Solution()
text1 = "abcde"
text2 = "ace"
print("Length of LCS:", sol.longestCommonSubsequence(text1, text2)) 






class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]



sol = Solution()
text1 = "abcde"
text2 = "ace"
print("Length of LCS:", sol.longestCommonSubsequence(text1, text2))  

