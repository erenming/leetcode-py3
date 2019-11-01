from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count_fresh = 0
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    count_fresh += 1
        if count_fresh == 0:
            return 0

        count = 0
        # up down left right
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while len(q) != 0:
            count += 1
            size = len(q)
            for _ in range(size):
                point = q.popleft()
                for dir in directions:
                    x = point[0] + dir[0]
                    y = point[1] + dir[1]
                    if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] in [0, 2]:
                        continue
                    grid[x][y] = 2
                    count_fresh -= 1
                    q.append((x, y))
        if count_fresh > 0:
            return -1
        else:
            return count - 1


if __name__ == '__main__':
    print(Solution().orangesRotting([[1,2]]))
