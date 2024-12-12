from collections import deque

def calculate_area_and_perimeter(grid, visited, sr, sc):
    rows, cols = len(grid), len(grid[0])
    tp = grid[sr][sc]
    area = 0
    perm = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(sr, sc)])
    visited[sr][sc] = True

    while queue:
        r, c = queue.popleft()
        area += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == tp:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                else:
                    perm += 1
            else:
                perm += 1

    return area, perm

with open("input.txt", "r") as f:
    lines = f.readlines()
    grid = [list(row.rstrip("\n")) for row in lines]
    print(grid)
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area, perm = calculate_area_and_perimeter(grid, visited, r, c)
                total_price += area * perm

    print(total_price)