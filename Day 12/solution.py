from collections import deque

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def calculate_area_and_perimeter(grid, visited, start_row, start_col):
    rows, cols = len(grid), len(grid[0])
    plant_type = grid[start_row][start_col]
    area = 0
    perimeter = 0

    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True

    while queue:
        row, col = queue.popleft()
        area += 1

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            # Check if the neighbor is within bounds
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == plant_type:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                else:
                    perimeter += 1
            else:
                # If out of bounds, it contributes to the perimeter
                perimeter += 1

    return area, perimeter

def calculate_total_price(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    total_price = 0

    for row in range(rows):
        for col in range(cols):
            if not visited[row][col]:
                area, perimeter = calculate_area_and_perimeter(grid, visited, row, col)
                total_price += area * perimeter

    return total_price

def main():
    input_file = "input.txt"  # Replace with your input file name
    grid = read_input(input_file)
    total_price = calculate_total_price(grid)
    print(f"Total price of fencing all regions: {total_price}")

if __name__ == "__main__":
    main()
