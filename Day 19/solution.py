from collections import Counter

def can_form_design(towel_patterns, design):
    """
    Determine if the given design can be formed using the available towel patterns.
    
    :param towel_patterns: List of towel patterns.
    :param design: String representing the desired design.
    :return: True if the design can be formed, False otherwise.
    """
    dp = [False] * (len(design) + 1)
    dp[0] = True  # Base case: empty design is always possible

    for i in range(1, len(design) + 1):
        for pattern in towel_patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]

    return dp[len(design)]

def count_possible_designs(towel_patterns, designs):
    """
    Count how many designs can be formed using the available towel patterns.
    
    :param towel_patterns: List of towel patterns.
    :param designs: List of desired designs.
    :return: Integer count of possible designs.
    """
    return sum(1 for design in designs if can_form_design(towel_patterns, design))

def main():
    # Read input from input.txt
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()

    # Parse towel patterns
    towel_patterns = lines[0].split(', ')

    # Parse designs
    designs = lines[2:]

    # Count possible designs
    possible_count = count_possible_designs(towel_patterns, designs)

    # Output the result
    print(f"Number of possible designs: {possible_count}")

if __name__ == "__main__":
    main()
