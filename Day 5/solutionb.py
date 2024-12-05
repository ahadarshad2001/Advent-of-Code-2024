from collections import defaultdict, deque

def parse_input(filename):
    """
    Parses the input file into ordering rules and updates.
    """
    with open(filename, 'r') as file:
        lines = file.read().strip().split("\n")

    # Separate rules and updates
    rule_lines = []
    update_lines = []
    reading_updates = False

    for line in lines:
        if line == "":
            reading_updates = True
            continue
        if not reading_updates:
            rule_lines.append(line)
        else:
            update_lines.append(line)

    # Parse rules
    rules = []
    for rule_line in rule_lines:
        x, y = map(int, rule_line.split("|"))
        rules.append((x, y))

    # Parse updates
    updates = []
    for update_line in update_lines:
        updates.append(list(map(int, update_line.split(","))))

    return rules, updates


def is_valid_update(update, rules):
    """
    Checks if an update is valid based on the ordering rules.
    """
    for x, y in rules:
        if x in update and y in update:
            # Check if x appears before y
            if update.index(x) > update.index(y):
                return False
    return True


def topological_sort(pages, rules):
    """
    Orders the pages using topological sorting based on the given rules.
    """
    # Create graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order


def find_middle_page(update):
    """
    Finds the middle page of the given update.
    """
    mid_index = len(update) // 2
    return update[mid_index]


def main():
    input_file = "input.txt"
    rules, updates = parse_input(input_file)

    # Separate valid and invalid updates
    invalid_updates = []
    for update in updates:
        if not is_valid_update(update, rules):
            invalid_updates.append(update)

    # Correct the invalid updates
    corrected_updates = []
    for update in invalid_updates:
        corrected_updates.append(topological_sort(update, rules))

    # Find the middle page of each corrected update and sum them
    middle_sum = sum(find_middle_page(update) for update in corrected_updates)

    print(f"The sum of middle page numbers of corrected updates is: {middle_sum}")


if __name__ == "__main__":
    main()
