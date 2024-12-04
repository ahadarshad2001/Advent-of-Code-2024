def load_grid_from_file(filename):
    """
    Load the word search grid from a file.
    Each line in the file represents a row in the grid.
    """
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def count_x_mas_occurrences(grid):
    """
    Count occurrences of the X-MAS pattern in the grid.
    """
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Helper function to check if a pattern matches "MAS" or "SAM"
    def is_mas(sequence):
        return sequence == "MAS" or sequence == "SAM"

    # Traverse the grid
    for row in range(1, rows - 1):  # Avoid edges
        for col in range(1, cols - 1):  # Avoid edges
            # Check for the "X-MAS" pattern centered at grid[row][col]
            center = grid[row][col]
            if center != "A":
                continue

            # Extract diagonals
            top_left = grid[row - 1][col - 1]
            bottom_right = grid[row + 1][col + 1]
            top_right = grid[row - 1][col + 1]
            bottom_left = grid[row + 1][col - 1]

            # Check if diagonals form "MAS" or "SAM"
            if is_mas(top_left + center + bottom_right) and is_mas(top_right + center + bottom_left):
                count += 1

    return count

if __name__ == "__main__":
    # Load the grid from the file
    input_file = "input.txt"
    grid = load_grid_from_file(input_file)

    # Count X-MAS occurrences
    total_count = count_x_mas_occurrences(grid)

    # Output the result
    print(f"The X-MAS pattern appears {total_count} times in the grid.")
