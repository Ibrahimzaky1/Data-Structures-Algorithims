from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

def print_tree(root):
    """Helper function to print tree in-order."""
    if not root:
        return
    print_tree(root.left)
    print(root.val, end=' ')
    print_tree(root.right)


root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7, TreeNode(6), TreeNode(9))

print("Original tree in-order:")
print_tree(root)
print()

sol = Solution()
inverted_root = sol.invertTree(root)

print("Inverted tree in-order:")
print_tree(inverted_root)
print()



class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
    






from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False

            return 1 + max(left_height, right_height)

        height(root)
        return balanced[0]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

sol = Solution()
print("Is balanced:", sol.isBalanced(root))

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)

print("Is balanced:", sol.isBalanced(root2))






import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)

            if largest != next_largest:
                heapq.heappush(stones, largest - next_largest)

        return -stones[0] if stones else 0


sol = Solution()
print(sol.lastStoneWeight([2,7,4,1,8,1]))  

        



import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))  

        