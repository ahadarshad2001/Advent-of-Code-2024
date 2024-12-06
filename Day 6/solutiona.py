def count_distinct_positions(grid):
    # Directions: up, right, down, left (clockwise)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_map = {'^': 0, '>': 1, 'v': 2, '<': 3}

    # Find the starting position and direction
    rows = len(grid)
    cols = len(grid[0])
    start_row = start_col = -1
    direction = 0  # Default direction is up (^) if not found otherwise
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in direction_map:
                start_row, start_col = r, c
                direction = direction_map[grid[r][c]]
                break
        if start_row != -1:
            break

    # Set to track visited positions
    visited = set()
    visited.add((start_row, start_col))
    
    row, col = start_row, start_col
    
    while True:
        # Move forward in the current direction
        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]

        # Check if the guard is leaving the map
        if not (0 <= next_row < rows and 0 <= next_col < cols):
            break
        
        # Check if there's an obstacle
        if grid[next_row][next_col] == '#':
            # Turn right (90 degrees)
            direction = (direction + 1) % 4
        else:
            # Move to the next position
            row, col = next_row, next_col
            visited.add((row, col))

    # The number of distinct positions visited
    return len(visited)


# Read the grid from the input.txt file
def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read lines and remove any extra whitespace (like newlines)
        grid = [line.strip() for line in file.readlines()]
    return grid

# File path to the input.txt file
file_path = "input.txt"

# Read the grid from the file
grid = read_grid_from_file(file_path)

# Call the function with the grid
result = count_distinct_positions(grid)
print(f"Distinct positions visited: {result}")
