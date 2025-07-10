from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]  

        for i in range(n - 2):  
            lo, hi = i + 1, n - 1
            while lo < hi:
                cur_sum = nums[i] + nums[lo] + nums[hi]

                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum

                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    lo += 1
                else:
                    hi -= 1

        return closest_sum


sol = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 1))  




class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def f(x):
            if x in memo:
                return memo[x]
            memo[x] = f(x - 1) + f(x - 2)
            return memo[x]

        return f(n)


sol = Solution()
print(sol.fib(10))  




class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev, cur = 0, 1
        for _ in range(2, n + 1):
            prev, cur = cur, prev + cur

        return cur
sol = Solution()
print(sol.fib(10))  

    


class Solution:
    def climStairs(self, n: int) -> int:
        
        memo = {1:1, 2:2}
        def f(n):   
            if n in memo:
                return memo[n]
            else:
                memo[n] = f(n-2) + f(n-1)
                return memo[n]
            
        return f(n)
    



class Solution:
    def climStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n-1]


sol = Solution()
print(sol.climStairs(5))  


