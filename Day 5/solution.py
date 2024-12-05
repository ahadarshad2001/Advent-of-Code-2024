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


def find_middle_page(update):
    """
    Finds the middle page of the given update.
    """
    mid_index = len(update) // 2
    return update[mid_index]


def main():
    input_file = "input.txt"
    rules, updates = parse_input(input_file)

    valid_updates = []
    for update in updates:
        if is_valid_update(update, rules):
            valid_updates.append(update)

    # Find the middle page of each valid update and sum them
    middle_sum = sum(find_middle_page(update) for update in valid_updates)

    print(f"The sum of middle page numbers of valid updates is: {middle_sum}")


if __name__ == "__main__":
    main()
