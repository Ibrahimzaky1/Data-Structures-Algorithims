  from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num

            if ans == num:
                count += 1
            else:
                count -= 1

        return ans


s = Solution()
print(s.majorityElement([3, 2, 3]))  # Output: 3
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2


    





class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}
        stk = []

        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[c]:
                        return False
        return not stk
    

s = Solution()
print(s.isValid("()"))         
print(s.isValid("()[]{}"))     
print(s.isValid("(]"))         
print(s.isValid("([)]"))       
print(s.isValid("{[]}")) 


from typing import List

class Solution:
    def dailyTemperatures(self, temperature: List[int]) -> List[int]:
        n = len(temperature)
        answer = [0] * n
        stk = []  # (temp, index)

        for i, t in enumerate(temperature):
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()
                answer[stk_i] = i - stk_i
            stk.append((t, i))

        return answer

# Example usage
s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  
# Output: [1, 1, 4, 2, 1, 1, 0, 0]











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


