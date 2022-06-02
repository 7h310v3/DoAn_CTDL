import numpy as np


def possible(grid, y, x):
    l = len(grid)
    for i in range(l):
        if grid[y][i] == 1:
            return False
    for i in range(l):
        if grid[i][x] == 1:
            return False

    for i in range(l):
        for j in range(l):
            if grid[i][j] == 1:
                if abs(i - y) == abs(j - x):
                    return False
    return True

def solve(grid):
    l = len(grid)

    for y in range(l):
        for x in range(l):
            if grid[y][x] == 0:
                if possible(grid, y, x):
                    grid[y][x] = 1
                    solve(grid)
                    if sum(sum(a) for a in grid) == l:
                        return grid
                    grid[y][x] = 0

    return grid

def main():
    N = 8
    grid = np.zeros([N, N], dtype=int)
    grid = grid.tolist()
    
    Solution = solve(grid)
    print(np.matrix(Solution))

if __name__ == "__main__":
    main()
