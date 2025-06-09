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


s = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = s.merge(intervals)
print(result)  # Output: [[1, 6], [8, 10], [15, 18]]

                



        
         
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        i, j = 0, 0
        UP, RIGHT, DOWN, LEFT, = 0, 1, 2, 3
        direction = RIGHT

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1

        while len(ans) != m*n:
            if direction == RIGHT :
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i+1, j-1
                RIGHT_WALL -= 1
                direction = DOWN

            elif direction == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                DOWN_WALL -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                LEFT_WALL += 1
                direction = UP
            else:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                UP_WALL += 1
                direction = RIGHT

        return ans

sol = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sol.spiralOrder(matrix))                 



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit


        



from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sol = Solution()
sol.rotate(matrix)


print(matrix)





class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count

jewels = "aA"
stones = "aAAbbbb"

sol = Solution()
result = sol.numJewelsInStones(jewels, stones)
print(result)



from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for c in magazine:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1

        return True

            
sol = Solution()
print(sol.canConstruct("aab", "baa"))   # Output: True
print(sol.canConstruct("aab", "ab"))    # Output: False





class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for num in nums:
            if num in h:
                return True
            else:
                h.add(num)

        return False
    
    
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 4]))    # False
print(sol.containsDuplicate([1, 2, 3, 1]))    # True






from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)
        return s_dict == t_dict


sol = Solution()
print(sol.isAnagram("listen", "silent"))  # Output: True





from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        # Check columns
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        # Check 3x3 sub-boxes
        starts = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]
        
        for i, j in starts:
            s = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)

        return True
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

sol = Solution()
print(sol.isValidSudoku(board))  # Output: True



from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        for c in text:
            if c in 'balloon':
                counter[c] += 1

        return min(
            counter['b'],
            counter['a'],
            counter['l'] // 2,
            counter['o'] // 2,
            counter['n']
        )


s = Solution()
print(s.maxNumberOfBalloons("loonbalxballpoon"))  # Output: 2








from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                length = 1
                next_num = num + 1
                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)

        return longest


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4 (sequence: 1, 2, 3, 4)





from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        max_count = -1
        ans = -1

        for key, val in counter.items():
            if val > max_count:
                max_count = val
                ans = key

        return ans


s = Solution()
print(s.majorityElement([3, 2, 3]))  # Output: 3
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2






    

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


    


