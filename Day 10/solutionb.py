def read_input(file_path):
    """Reads the topographic map from the input file."""
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip())) for line in f]

def get_neighbors(x, y, grid):
    """Returns valid neighbors (up, down, left, right) for the given cell."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):  # Within bounds
            neighbors.append((nx, ny))
    return neighbors

def dfs(grid, x, y, visited):
    """Performs DFS to count all distinct hiking trails starting from (x, y)."""
    if grid[x][y] == 9:  # Reached a height of 9, this is a valid trail.
        return 1
    
    total_paths = 0
    visited.add((x, y))  # Mark the current cell as visited
    
    for nx, ny in get_neighbors(x, y, grid):
        if (nx, ny) not in visited and grid[nx][ny] == grid[x][y] + 1:
            total_paths += dfs(grid, nx, ny, visited)
    
    visited.remove((x, y))  # Backtrack: unmark the cell
    return total_paths

def calculate_trailhead_ratings(grid):
    """Calculates the sum of ratings for all trailheads."""
    total_rating = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:  # Found a trailhead
                total_rating += dfs(grid, x, y, set())
    return total_rating

# Main Execution
# Provide the path to your input file
file_path = 'input.txt'
try:
    topographic_map = read_input(file_path)  # Reading the input map
    rating_result = calculate_trailhead_ratings(topographic_map)
    print("Sum of trailhead ratings:", rating_result)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print("An error occurred:", str(e))
