# Implementing the solution as described to calculate the sum of the scores of all trailheads.

from collections import deque

def read_input(file_path):
    """Reads the topographic map from the input file."""
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip())) for line in f]

def get_neighbors(x, y, grid):
    """Returns valid neighbors for a position on the grid."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbors.append((nx, ny))
    return neighbors

def bfs(grid, start):
    """Performs BFS to find all reachable '9' positions from a trailhead."""
    queue = deque([start])
    visited = set()
    visited.add(start)
    reachable_nines = set()
    
    while queue:
        x, y = queue.popleft()
        current_height = grid[x][y]
        
        for nx, ny in get_neighbors(x, y, grid):
            if (nx, ny) not in visited and grid[nx][ny] == current_height + 1:
                visited.add((nx, ny))
                queue.append((nx, ny))
                if grid[nx][ny] == 9:
                    reachable_nines.add((nx, ny))
    
    return len(reachable_nines)

def calculate_trailhead_scores(grid):
    """Calculates the sum of scores for all trailheads."""
    total_score = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:  # Found a trailhead
                score = bfs(grid, (x, y))
                total_score += score
    return total_score

# File path for the input data
file_path = '/mnt/data/input.txt'

# Read the topographic map and compute the result
topographic_map = read_input(file_path)
result = calculate_trailhead_scores(topographic_map)
result
