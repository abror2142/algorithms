"""
    This Solution is only for the Special case of the problem:
        Find Number of possible paths to get to the bottom-right
        cell of the grid from top-left cell inside (m, n) gird.
"""

def pathNaive(grid):
    if grid[0] == 0 or grid[1] == 0:
        return 0;

    if(grid[0] == 1 and grid[1] == 1):
        return 1;
    
    grid1 = (grid[0]-1, grid[1])
    grid2 = (grid[0], grid[1]-1)

    return pathNaive(grid1) + pathNaive(grid2)


def pathOptimized(grid, memo={}): 
    if grid in memo:
        return memo[grid]

    if grid[0] == 0 or grid[1] == 0:
        return 0
    
    if grid[0] == 1 and grid[1] == 1:
        return 1
    
    grid1 = (grid[0]-1, grid[1])
    grid2 = (grid[0], grid[1]-1)

    memo[grid] = pathOptimized(grid1, memo) + pathOptimized(grid2, memo)
    return memo[grid]


grid = (4, 4) # Le'ts use tuple!
print("\t>>>>Number of Paths In Grid Python Implementation<<<<")
print("Naive Algorithm:     grid=", grid, "=>", pathNaive(grid))
print("Optimized Algorithm: grid=", grid, "=>", pathOptimized(grid))