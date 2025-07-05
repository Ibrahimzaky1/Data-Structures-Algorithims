from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        p_que = deque()
        p_seen = set()
        a_que = deque()
        a_seen = set()

        for j in range(n):
            p_que.append((0, j))
            p_seen.add((0, j))
            a_que.append((m - 1, j))
            a_seen.add((m - 1, j))

        for i in range(m):
            p_que.append((i, 0))
            p_seen.add((i, 0))
            a_que.append((i, n - 1))
            a_seen.add((i, n - 1))

        def bfs(que, seen):
            while que:
                i, j = que.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    r, c = i + di, j + dj
                    if 0 <= r < m and 0 <= c < n and (r, c) not in seen and heights[r][c] >= heights[i][j]:
                        seen.add((r, c))
                        que.append((r, c))

        bfs(p_que, p_seen)
        bfs(a_que, a_seen)

        result = list(p_seen & a_seen)
        return result


sol = Solution()
print(sol.pacificAtlantic([
  [1, 2, 2, 3, 5],
  [3, 2, 3, 4, 4],
  [2, 4, 5, 3, 1],
  [6, 7, 1, 4, 5],
  [5, 1, 1, 2, 4]
]))
