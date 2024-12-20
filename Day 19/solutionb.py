def count_ways(design, patterns_set, memo):
    if design in memo:
        return memo[design]
    if not design:
        return 1
    total = 0
    for pattern in patterns_set:
        if design.startswith(pattern):
            total += count_ways(design[len(pattern):], patterns_set, memo)
    memo[design] = total
    return total

def main():
    try:
        with open('input.txt', 'r') as file:
            lines = [line.strip() for line in file]
    except FileNotFoundError:
        print(0)
        return

    if not lines:
        print(0)
        return

    # Split patterns
    patterns_line = lines[0]
    patterns = [p.strip() for p in patterns_line.split(',') if p.strip()]
    patterns_set = set(patterns)

    # Find index of first blank line
    try:
        blank_index = lines.index('')
    except ValueError:
        blank_index = 1

    # Remaining lines are designs
    designs = lines[blank_index+1:] if blank_index+1 < len(lines) else []
    possible_designs = 0
    total_ways = 0
    for design in designs:
        ways = count_ways(design, patterns_set, {})
        if ways > 0:
            possible_designs += 1
            total_ways += ways
    print(total_ways)

if __name__ == "__main__":
    main()
