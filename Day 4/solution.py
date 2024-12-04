def load_grid_from_file(filename):
    """
    Load the word search grid from a file.
    Each line in the file represents a row in the grid.
    """
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def count_word_occurrences(grid, word):
    """
    Count occurrences of a word in a grid in all possible directions.
    """
    word_length = len(word)
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Directions: (row_delta, col_delta)
    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Down-Right
        (1, -1), # Down-Left
        (-1, 1), # Up-Right
        (-1, -1) # Up-Left
    ]

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                # Check if the word fits in the current direction
                if 0 <= row + (word_length - 1) * dr < rows and \
                   0 <= col + (word_length - 1) * dc < cols:
                    # Extract the word in this direction
                    extracted = ''.join(grid[row + i * dr][col + i * dc] for i in range(word_length))
                    if extracted == word:
                        count += 1

    return count

if __name__ == "__main__":
    # Load the grid from the file named "input.txt"
    input_file = "input.txt"
    grid = load_grid_from_file(input_file)

    # Word to search
    word_to_find = "XMAS"

    # Count occurrences of the word
    total_count = count_word_occurrences(grid, word_to_find)

    # Output the result
    print(f"The word '{word_to_find}' appears {total_count} times in the grid.")
