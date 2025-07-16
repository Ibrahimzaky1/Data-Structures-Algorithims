from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        smallest = [float('inf')]

        def backtrack(i=0, jumped=0):
            if i >= n:
                return
            if i == n - 1:
                smallest[0] = min(smallest[0], jumped)
                return

            max_jump = nums[i]
            max_reachable_index = min(i + max_jump, n - 1)

            for new_index in range(max_reachable_index, i, -1):
                backtrack(new_index, jumped + 1)

        backtrack()
        return smallest[0]


sol = Solution()
nums = [2, 3, 1, 1, 4]
print("Minimum jumps:", sol.jump(nums))

    






from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        smallest = 0
        n = len(nums)
        end, far = 0, 0

        for i in range(n - 1):
            far = max(far, i + nums[i])
            if i == end:
                smallest += 1
                end = far

        return smallest

sol = Solution()
nums = [2, 3, 1, 1, 4]
print("Minimum jumps:", sol.jump(nums))





from typing import List

class Solution:
    def hIndex(self, citation: List[int]) -> int:
        n = len(citation)
        paper_counts = [0] * (n + 1)

        for c in citation:
            paper_counts[min(n, c)] += 1

        h = n
        papers = paper_counts[n]

        while h > 0 and papers < h:
            h -= 1
            papers += paper_counts[h]

        return h


sol = Solution()
print(sol.hIndex([3, 0, 6, 1, 5]))  



class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        negative = num < 0
        num = abs(num)
        remainders = []

        while num > 0:
            remainder = num % 7
            remainders.append(str(remainder))
            num //= 7

        base7 = ''.join(reversed(remainders))
        return '-' + base7 if negative else base7


sol = Solution()
print(sol.convertToBase7(100))   
print(sol.convertToBase7(-7))    
print(sol.convertToBase7(0))     








class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans += 1
            n = n & (n - 1)
        return ans


sol = Solution()
print(sol.hammingWeight(11))    
print(sol.hammingWeight(128))    
print(sol.hammingWeight(4294967293))  




class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)

        while b:
            without_carry = a ^ b
            carry = (a & b) << 1
            a, b = without_carry, carry

        return bin(a)[2:]


sol = Solution()
print(sol.addBinary("11", "1"))       
print(sol.addBinary("1010", "1011"))  










from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for x in nums:
            a ^= x
        return a

sol = Solution()
print(sol.singleNumber([2, 2, 1]))        
print(sol.singleNumber([4, 1, 2, 1, 2]))  
print(sol.singleNumber([1]))             
