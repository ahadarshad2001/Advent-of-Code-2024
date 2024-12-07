from itertools import product

def evaluate_expression(numbers, operators):
    """
    Evaluate the expression formed by placing the given operators between the numbers.
    Evaluation is done strictly from left to right.
    """
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result

def solve_bridge_repair(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().split('\n')

    total_calibration_result = 0

    for line in lines:
        # Parse the input line
        target, nums = line.split(':')
        target = int(target.strip())
        numbers = list(map(int, nums.strip().split()))

        # Determine the number of operators needed
        num_operators = len(numbers) - 1

        # Generate all combinations of operators
        possible_operators = product(['+', '*'], repeat=num_operators)

        # Check if any combination of operators produces the target value
        for operators in possible_operators:
            if evaluate_expression(numbers, operators) == target:
                total_calibration_result += target
                break

    return total_calibration_result

# File path to the input data
input_file = "input.txt"
result = solve_bridge_repair(input_file)
print(f"Total Calibration Result: {result}")
