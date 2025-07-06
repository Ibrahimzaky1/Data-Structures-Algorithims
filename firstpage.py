from typing import List, Optional

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node({self.val})"

class Solution:
    def CloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        start = node
        o_to_n = {}
        stk = [start]
        visited = set()
        visited.add(start)

        while stk:
            node = stk.pop()
            if node not in o_to_n:
                o_to_n[node] = Node(val=node.val)

            for nei in node.neighbors:
                if nei not in o_to_n:
                    o_to_n[nei] = Node(val=nei.val)
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)

        for old_node, new_node in o_to_n.items():
            for nei in old_node.neighbors:
                new_node.neighbors.append(o_to_n[nei])

        return o_to_n[start]


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]


solution = Solution()
cloned_node1 = solution.CloneGraph(node1)

from collections import deque

def print_graph(node):
    visited = set()
    q = deque([node])
    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        print(f"Node {curr.val} neighbors: {[n.val for n in curr.neighbors]}")
        for neighbor in curr.neighbors:
            q.append(neighbor)

print("Original graph:")
print_graph(node1)

print("\nCloned graph:")
print_graph(cloned_node1)







from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        m, n = len(grid), len(grid[0])
        num_fresh = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    q.append((i,j))
                elif grid[i][j] == FRESH:
                    num_fresh += 1

        if num_fresh == 0:
            return 0
        
        num_minutes = -1
        while q:
            q_size = len(q)
            num_minutes += 1
            for _ in range(q_size):
                i, j = q.popleft()
                for r, c in [(i, j+1), (i+1,j), (i,j-1), (i-1,j)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        num_fresh -= 1
                        q.append((r,c))

        return num_minutes if num_fresh == 0 else -1


grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

solution = Solution()
result = solution.orangesRotting(grid)
print("Minutes to rot all oranges:", result)




import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        total_cost = 0
        seen = set()
        min_heap = [(0, 0)]  

        while len(seen) < n:
            dist, i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            total_cost += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    nei_dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (nei_dist, j))

        return total_cost


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
solution = Solution()
result = solution.minCostConnectPoints(points)
print("Minimum cost to connect all points:", result)
