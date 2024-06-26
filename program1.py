class Solution:
    def scan_island(self, grid, row, col, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W' or visited[row][col]:
            return
        visited[row][col] = True
        self.scan_island(grid, row + 1, col, visited)
        self.scan_island(grid, row - 1, col, visited)
        self.scan_island(grid, row, col + 1, visited)
        self.scan_island(grid, row, col - 1, visited)

    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L' and not visited[i][j]:
                    self.scan_island(grid, i, j, visited)
                    island_count += 1
        return island_count
