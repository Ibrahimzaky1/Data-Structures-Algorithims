class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num

        while l <= r:
            m = (l + r) // 2
            m_squared = m * m

            if num == m_squared:
                return True
            elif m_squared < num:
                l = m + 1
            else:
                r = m - 1

        return False


s = Solution()
print(s.isPerfectSquare(16))   # True
print(s.isPerfectSquare(14))   # False
print(s.isPerfectSquare(1))    # True
print(s.isPerfectSquare(808201))  # True (899^2)
print(s.isPerfectSquare(808202))  # False



from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for p in piles:
                hours += ceil(p / k)
            return hours <= h
        
        l = 1
        r = max(piles)

        while l < r:
            k = (l + r) // 2
            if k_works(k):
                r = k
            else:
                l = k + 1

        return l

s = Solution()
print(s.minEatingSpeed([3, 6, 7, 11], 8))   
print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))  
print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))  




from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


def build_list(values):
    dummy = ListNode()
    cur = dummy
    for val in values:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


s = Solution()
head = build_list([1, 1, 2, 3, 3])
new_head = s.deleteDuplicates(head)
print_list(new_head)  






from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print("Original list:")
print_list(n1)

s = Solution()
reversed_head = s.reverseList(n1)

print("Reversed list:")
print_list(reversed_head)




from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        cur = d 

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 if list1 else list2
        return d.next


def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

list1 = build_list([1, 3, 5])
list2 = build_list([2, 4, 6])

s = Solution()
merged = s.mergeTwoLists(list1, list2)

print("Merged list:")
print_list(merged)



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(n1):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1

        if s1_counts == s2_counts:
            return True
        
        for i in range(n1, n2):
            s2_counts[ord(s2[i]) - 97] += 1
            s2_counts[ord(s2[i-n1]) - ord('a')] -= 1
            if s1_counts == s2_counts:
                return True
            
        return False

sol = Solution()
result = sol.checkInclusion("ab", "eidbaooo")
print("Result:", result)




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
    
    